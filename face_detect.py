import boto3
import image_helpers
from pprint import pprint

import pyscreenshot as ImageGrab
import time

client = boto3.client('rekognition')

# imgfilename = './images/image.jpg'

# imgbytes = image_helpers.get_image_from_file(imgfilename)

# rekres = client.detect_faces(Image={'Bytes': imgbytes})

# # pprint(rekres)
# numfaces = len(rekres['FaceDetails'])
# print('Found', numfaces, end='')
# if numfaces == 1:
#     print(' face')
# else:
#     print(' faces')

cont = 0

while True:
    im = ImageGrab.grab(bbox=(50, 50, 510, 510))
    im.save('./assets/fullscreen' + str(cont) + '.jpg')

    time.sleep(3)

    imgfilename = './assets/fullscreen' + str(cont) + '.jpg'

    imgbytes = image_helpers.get_image_from_file(imgfilename)

    rekres = client.detect_faces(Image={'Bytes': imgbytes})

    numfaces = len(rekres['FaceDetails'])
    print('Found', numfaces, end='')
    if numfaces == 1:
        print(' face')
    else:
        print(' faces')
    cont += 1
    time.sleep(5)
