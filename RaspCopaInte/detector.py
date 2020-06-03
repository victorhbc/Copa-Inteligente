######## Webcam Human Detection Using Tensorflow-trained Classifier #########

# Import packages
import os
import argparse
import cv2
import numpy as np
import sys
import time
import importlib.util
import firebase_admin
from datetime import datetime
from threading import Thread
from performance_tracking import PerformanceTracker
from firebase_admin import credentials
from utils.VideoStream import VideoStream
from database.firebase_interface import FirebaseInterface

cred = credentials.Certificate("database/credentials.json")
firebase_admin.initialize_app(cred)
interface = FirebaseInterface()


def sendDataToFirebase(num_people):
    docTitle = datetime.today().strftime('%Y-%m-%d')
    currentHour = datetime.today().strftime('%H:%M')
    docData = {currentHour: {"num_people": num_people}}
    interface.addOrUpdateData("kitchen_data", docTitle, docData)
    interface.addOrUpdateData(
        "performance", "performance", PerformanceTracker.getCurrentPerformanceStatus())


def getParameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('--modeldir', help='Folder the .tflite file is located in',
                        default='models')
    parser.add_argument('--graph', help='Name of the .tflite file, if different than detect.tflite',
                        default='detect.tflite')
    parser.add_argument('--labels', help='Name of the labelmap file, if different than labelmap.txt',
                        default='labelmap.txt')
    parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects',
                        default=0.5)
    parser.add_argument('--resolution', help='Desired webcam resolution in WxH. If the webcam does not support the resolution entered, errors may occur.',
                        default='640x480')
    parser.add_argument('--sleep', help='Set the number of seconds between each detection',
                        default=60)
    parser.add_argument('--cameraip', help='IP from the camera')
    parser.add_argument(
        '--showlog', help='True to show log or False to do not show log', default=False)
    return parser.parse_args()


def main():
    # If tensorflow is not installed, import interpreter from tflite_runtime, else import from regular tensorflow
    pkg = importlib.util.find_spec('tensorflow')
    if pkg is None:
        from tflite_runtime.interpreter import Interpreter
    else:
        from tensorflow.lite.python.interpreter import Interpreter

    args = getParameters()
    MODEL_NAME = args.modeldir
    GRAPH_NAME = args.graph
    LABELMAP_NAME = args.labels
    SLEEP_TIME = args.sleep
    CAMERA_IP = args.cameraip
    SHOW_LOG = args.showlog
    MIN_CONF_THRESHOLD = args.threshold

    resW, resH = args.resolution.split('x')
    imW, imH = int(resW), int(resH)

    # Get path to current working directory
    CWD_PATH = os.getcwd()

    # Path to .tflite file, which contains the model that is used for object detection
    PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, GRAPH_NAME)

    # Path to label map file
    PATH_TO_LABELS = os.path.join(CWD_PATH, MODEL_NAME, LABELMAP_NAME)

    # Load the label map
    with open(PATH_TO_LABELS, 'r') as f:
        labels = [line.strip() for line in f.readlines()]

    # Have to do a weird fix for label map if using the COCO "starter model" from
    # https://www.tensorflow.org/lite/models/object_detection/overview
    # First label is '???', which has to be removed.
    if labels[0] == '???':
        del(labels[0])

    # Load the Tensorflow Lite model and get details
    interpreter = Interpreter(model_path=PATH_TO_CKPT)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]

    floating_model = (input_details[0]['dtype'] == np.float32)

    input_mean = 127.5
    input_std = 127.5

    # Initialize frame rate calculation
    # freq = cv2.getTickFrequency()

    # Initialize video stream
    videostream = VideoStream(
        resolution=(imW, imH), framerate=30, camera_ip=CAMERA_IP).start()
    time.sleep(1)

    # Start time
    startTime = time.time()

    # Mean of people
    people_mean = 0
    while True:
        try:
            # Grab frame from video stream
            frame1 = videostream.read()

            # Acquire frame and resize to expected shape [1xHxWx3]
            frame = frame1.copy()
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resized = cv2.resize(frame_rgb, (width, height))
            input_data = np.expand_dims(frame_resized, axis=0)

            # Normalize pixel values if using a floating model (i.e. if model is non-quantized)
            if floating_model:
                input_data = (np.float32(input_data) - input_mean) / input_std

            # Perform the actual detection by running the model with the image as input
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()

            # Retrieve detection results
            # Bounding box coordinates of detected objects
            
            # boxes = interpreter.get_tensor(output_details[0]['index'])[0]
            classes = interpreter.get_tensor(output_details[1]['index'])[
                0]  # Class index of detected objects
            scores = interpreter.get_tensor(output_details[2]['index'])[
                0]  # Confidence of detected objects

            # Current people detected
            current_num_people = 0

            # Loop over all detections and draw detection box if confidence is above minimum threshold
            for i in range(len(scores)):
                if scores[i] > MIN_CONF_THRESHOLD and scores[i] <= 1.0 and labels[int(classes[i])] == 'person':
                    current_num_people += 1

            # Update people mean
            people_mean = (people_mean + current_num_people) / 2

            if SHOW_LOG:
                print("Current people mean: " + str(people_mean))

            result = time.localtime() # pega o valor do tempo atual
            result = result.tm_hour

            # If should send information to Firebase
            if (time.time() - startTime > SLEEP_TIME) & ((result >= 7) & (result <= 18)): #compara se ja se passaram 1 minuto e o horario do funcionando é das 11 ~ 14
                # Update start time
                print('Informação enviada para o servidor do Firebase')
                print('Tempo decorrido: ' + str(time.time() - startTime))
                print('Horario atual: ' + str(result))

                startTime = time.time()
                sendDataToFirebase(round(people_mean))
        except:
            print('Camera não encontrada')
            videostream.stop() #reiniciar camera
            time.sleep(5)
            videostream = VideoStream(
            resolution=(imW, imH), framerate=30, camera_ip=CAMERA_IP).start()
            time.sleep(5)
    # Clean up
    videostream.stop()


if __name__ == '__main__':
    main()
