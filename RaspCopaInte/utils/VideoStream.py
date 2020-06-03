# Define VideoStream class to handle streaming of video from webcam in separate processing thread
# Source - Adrian Rosebrock, PyImageSearch: https://www.pyimagesearch.com/2015/12/28/increasing-raspberry-pi-fps-with-python-and-opencv/
import cv2
from threading import Thread


class VideoStream:
    """Camera object that controls video streaming from the Picamera"""

    def __init__(self, camera_ip, resolution=(640, 480), framerate=30):
        try:
            # # Initialize the PiCamera and the camera image stream
            # self.stream = cv2.VideoCapture(0) 

            # If the video should be capture from a IP camera
            if camera_ip:
                self.stream = cv2.VideoCapture(camera_ip)

            # ret = self.stream.set(4, resolution[1])

            # Read first frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

            if self.grabbed:
                # Variable to control when the camera is stopped
                self.stopped = False
            else:
                raise Exception("Camera is not connected")
        except:
            print('A camera não está conectada')

    def start(self):
        # Start the thread that reads frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the camera is stopped, stop the thread
            if self.stopped:
                # Close camera resources
                self.stream.release()
                return

            # Otherwise, grab the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # Return the most recent frame
        return self.frame

    def stop(self):
        # Indicate that the camera and thread should be stopped
        self.stopped = True
