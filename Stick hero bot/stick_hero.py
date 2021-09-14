#CoDeD By AnAnT

from ppadb.client import Client
from PIL import Image
import numpy
import time
adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
if len(devices) == 0:
    print('no device attached')
    quit()
device = devices[0]
while True:
  try:
    def looper():
      image = device.screencap()
      with open('screen.png', 'wb') as f:
        f.write(image)
      image = Image.open('screen.png')
      image = numpy.array(image, dtype=numpy.uint8)
      pixels = [list(i[:3]) for i in image[2000]]
      black = True
      transistions = []
      for i, pixel in enumerate(pixels):
        r, g, b = [int(i) for i in pixel]
        # print(r, g, b)
        if black==True and (r+g+b)>50:
          black = False
          transistions.append(i)
          continue
        if black==False and (r+g+b)==0:
          black=True
          transistions.append(i)
          continue
      return transistions
    val=0
    counter = 2
    while counter>0:
      transistions = looper()
      print(transistions)
      target1 = transistions[-2]
      target2 = transistions[-1]
      try:
        start = transistions[-3]
      except:
        start = target1
        target1 = target2
        target2 = 1080
      gap = target1-start
      distance = int((gap+(target2-target1)//2)*0.96)
      device.shell(f'input touchscreen swipe 500 500 500 500 {distance}')
      timer = (target2/500)+0.5
      print(timer)
      time.sleep(timer)
      if distance==val:
        counter-=1
      val=distance
    device.shell(f'input tap 860 1760')
    time.sleep(1)
  except:
    continue
