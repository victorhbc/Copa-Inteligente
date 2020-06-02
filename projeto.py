import boto3
from pprint import pprint
import pyscreenshot as ImageGrab
import time
import urllib.request
from firebase import firebase
import datetime

firebase = firebase.FirebaseApplication(
    "https://venturus-b5e60.firebaseio.com/", None)

client = boto3.client('rekognition')

count = 0

url = 'http://192.168.15.38:8080/shot.jpg'

while True:
    img_name = './assets/fullscreen' + str(count) + '.jpg'
    urllib.request.urlretrieve(url, img_name)

    with open(img_name, 'rb') as source_image:
        source_bytes = source_image.read()

    response = client.detect_labels(Image={'Bytes': source_bytes})

    resp = response['Labels']

    index = 0
    people = 0

    while index < len(resp):
        if resp[index]['Name'] == 'Person':
            people = resp[index]
        index += 1

    if people == 0:
        print(people)
    else:
        people = str(people).count("BoundingBox")
        print(people)

    data = {
        'People': people,
        'Time': datetime.datetime.now()
    }

    result = firebase.post('/venturus-b5e60/Info', data)
    print(result)

    count += 1
    time.sleep(4)
