import pyscreenshot as ImageGrab
import time

cont = 0
im = ImageGrab.grab(bbox=(5, 60, 640, 510))
im.save('./assets/fullscreen' + str(cont) + '.jpg')
