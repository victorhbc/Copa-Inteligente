import boto3
import image_helpers
from pprint import pprint
import pyscreenshot as ImageGrab
import time
import urllib.request

client = boto3.client('rekognition')

count = 0

url = 'http://192.168.15.38:8080/shot.jpg'

while True:
    img_name = './assets/fullscreen' + str(count) + '.jpg'
    urllib.request.urlretrieve(url, img_name)

    time.sleep(1)

    imgbytes = image_helpers.get_image_from_file(img_name)
    rek_res = client.detect_faces(Image={'Bytes': imgbytes})

    num_faces = len(rek_res['FaceDetails'])
    print('Found', num_faces, end='')
    if num_faces == 1:
        print(' face')
    else:
        print(' faces')
    count += 1
    time.sleep(1)
