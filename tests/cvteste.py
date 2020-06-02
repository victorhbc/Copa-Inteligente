# import cv2
# import numpy as np
# import urllib

# url = 'http://192.168.15.38:8080/shot.jpg'
# # img_res = urllib.request.urlopen(url)
# img_res = cv2.VideoCapture("http://192.168.15.38:8080/shot.jpg")
# img_np = np.array(bytearray(img_res.read()), dtype=np.uint8)
# img = cv2.indecode(img_np, -1)
# cv2.imshow('test', img)
# cv2.waitKey(10)

import urllib.request

# from PIL import Image
# import requests
# from io import BytesIO

url = 'http://192.168.15.38:8080/shot.jpg'
# response = requests.get(url)
# img = Image.open(BytesIO(response.content))


urllib.request.urlretrieve(url, "local-filename.jpg")
