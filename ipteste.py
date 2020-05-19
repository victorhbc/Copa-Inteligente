import pyscreenshot as ImageGrab
import time

cont = 0

while True:
    time.sleep(3)
    im = ImageGrab.grab(bbox=(50, 50, 510, 510))
    im.save('./assets/fullscreen' + str(cont) + '.jpg')
    cont += 1
