# & "C:/Program Files/Python38/python.exe" c:/Users/Josh/Desktop/testeboto/proj.py --time 2
import boto3
from pprint import pprint
import pyscreenshot as ImageGrab
import time
import urllib.request
import datetime
import os
import sys
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from database.firebase_interface import FirebaseInterface
import threading
import argparse

url = '[URL]/shot.jpg'
client = boto3.client('rekognition')
cred = credentials.Certificate('database/credentials.json')
firebase_admin.initialize_app(cred)
interface = FirebaseInterface()

def analyse():
  args = getParameters()
  threading.Timer(int(args.time), analyse).start()
  img_name = './assets/frame' + str(analyse.count) + '.jpg'
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

  sendDataToFirebase(people)
  analyse.count += 1


def sendDataToFirebase(num_people):
  docTitle = datetime.today().strftime('%Y-%m-%d')
  currentHour = datetime.today().strftime('%H:%M')
  docData = {currentHour: {"num_people": num_people}}
  interface.addOrUpdateData("kitchen_data", docTitle, docData)


def getParameters():
  parser = argparse.ArgumentParser()
  parser.add_argument('--time', help='Set the number of seconds between each detection',
                      default=60)
  return parser.parse_args()


def main():
  analyse.count = 0
  analyse()


if __name__ == '__main__':
  main()