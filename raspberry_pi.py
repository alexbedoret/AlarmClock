#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import ColorEightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
matrix_0 = ColorEightByEight(address=0x70)
matrix_1 = ColorEightByEight(address=0x72)
matrix_2 = ColorEightByEight(address=0x71)
matrix_3 = ColorEightByEight(address=0x74)

data = [0,7,0,3,0,6,1,3,0,5,2,3,0,4,3,3,0,3,4,3,0,2,5,3,0,1,6,3,0,0,7,3,1,7,0,3,1,6,1,3,1,5,2,3,1,4,3,3,1,3,4,3,1,2,5,3,1,1,6,3,1,0,7,3,2,7,0,3,2,6,1,3,2,5,2,3,2,4,3,3,2,3,4,3,2,2,5,3,2,1,6,3,2,0,7,3,3,7,0,3,3,6,1,3,3,5,2,3,3,4,3,3,3,3,4,3,3,2,5,3,3,1,6,3,3,0,7,3,0,7,0,3,0,6,1,3,0,5,2,3,0,4,3,3,0,3,4,3,0,2,5,3,0,1,6,3,0,0,7,3,1,7,0,3,1,6,1,3,1,5,2,3,1,4,3,3,1,3,4,3,1,2,5,3,1,1,6,1,1,0,7,1,2,7,0,3,2,6,1,1,2,5,2,1,2,4,3,3,2,3,4,3,2,2,5,3,2,1,6,3,2,0,7,3,3,7,0,3,3,6,1,3,3,5,2,3,3,4,3,3,3,3,4,3,3,2,5,3,3,1,6,3,3,0,7,3,0,7,0,3,0,6,1,3,0,5,2,3,0,4,3,3,0,3,4,3,0,2,5,3,0,1,6,3,0,0,7,3,1,7,0,3,1,6,1,3,1,5,2,3,1,4,3,3,1,3,4,3,1,2,5,1,1,1,6,4,1,0,7,4,2,7,0,1,2,6,1,4,2,5,2,4,2,4,3,1,2,3,4,3,2,2,5,3,2,1,6,3,2,0,7,3,3,7,0,3,3,6,1,3,3,5,2,3,3,4,3,3,3,3,4,3,3,2,5,3,3,1,6,3,3,0,7,3,0,7,0,3,0,6,1,3,0,5,2,3,0,4,3,3,0,3,4,3,0,2,5,3,0,1,6,3,0,0,7,3,1,7,0,3,1,6,1,3,1,5,2,3,1,4,3,3,1,3,4,3,1,2,5,1,1,1,6,4,1,0,7,4,2,7,0,4,2,6,1,4,2,5,2,4,2,4,3,1,2,3,4,3,2,2,5,3,2,1,6,3,2,0,7,3,3,7,0,3,3,6,1,3,3,5,2,3,3,4,3,3,3,3,4,3,3,2,5,3,3,1,6,3,3,0,7,3,0,7,0,3,0,6,1,3,0,5,2,3,0,4,3,3,0,3,4,3,0,2,5,3,0,1,6,3,0,0,7,3,1,7,0,3,1,6,1,3,1,5,2,3,1,4,3,3,1,3,4,3,1,2,5,3,1,1,6,1,1,0,7,4,2,7,0,4,2,6,1,4,2,5,2,1,2,4,3,3,2,3,4,3,2,2,5,3,2,1,6,3,2,0,7,3,3,7,0,3,3,6,1,3,3,5,2,3,3,4,3,3,3,3,4,3,3,2,5,3,3,1,6,3,3,0,7,3,0,7,0,3,0,6,1,3,0,5,2,3,0,4,3,3,0,3,4,3,0,2,5,3,0,1,6,3,0,0,7,3,1,7,0,3,1,6,1,3,1,5,2,3,1,4,3,3,1,3,4,3,1,2,5,3,1,1,6,3,1,0,7,1,2,7,0,4,2,6,1,1,2,5,2,3,2,4,3,3,2,3,4,3,2,2,5,3,2,1,6,3,2,0,7,3,3,7,0,3,3,6,1,3,3,5,2,3,3,4,3,3,3,3,4,3,3,2,5,3,3,1,6,3,3,0,7,3,0,7,0,3,0,6,1,3,0,5,2,3,0,4,3,3,0,3,4,3,0,2,5,3,0,1,6,3,0,0,7,3,1,7,0,3,1,6,1,3,1,5,2,3,1,4,3,3,1,3,4,3,1,2,5,3,1,1,6,3,1,0,7,3,2,7,0,1,2,6,1,3,2,5,2,3,2,4,3,3,2,3,4,3,2,2,5,3,2,1,6,3,2,0,7,3,3,7,0,3,3,6,1,3,3,5,2,3,3,4,3,3,3,3,4,3,3,2,5,3,3,1,6,3,3,0,7,3,0,7,0,3,0,6,1,3,0,5,2,3,0,4,3,3,0,3,4,3,0,2,5,3,0,1,6,3,0,0,7,3,1,7,0,3,1,6,1,3,1,5,2,3,1,4,3,3,1,3,4,3,1,2,5,3,1,1,6,3,1,0,7,3,2,7,0,3,2,6,1,3,2,5,2,3,2,4,3,3,2,3,4,3,2,2,5,3,2,1,6,3,2,0,7,3,3,7,0,3,3,6,1,3,3,5,2,3,3,4,3,3,3,3,4,3,3,2,5,3,3,1,6,3,3,0,7,3]
size = len(data)

print "Press CTRL+Z to exit"

iter = 0

# Continually update the 8x8 display one pixel at a time
while(True):
  iter += 1

  for x in range(0, 8):
    for y in range(0, 8):
      grid.setBicolorPixel(x, y, iter % 4 )
      time.sleep(0.02)

  
    for i in range(0,size):
      value = data[i]

      time.sleep(0.1)

      matrix  = value
      value   = data[i]
      column  = value
      value   = data[i]
      row     = value
      value   = data[i]
      led     = value

      color = led
      
      if matrix == 0:
          matrix_0.setBicolorPixel(column,row,0)
          matrix_0.setBicolorPixel(column,row,color)

      elif matrix == 1: 
          matrix_1.setBicolorPixel(column,row,0)
          matrix_1.setBicolorPixel(column,row,color)

      elif matrix == 2:
          matrix_2.setBicolorPixel(column,row,0)
          matrix_2.setBicolorPixel(column,row,color)

      elif matrix == 3:
          matrix_3.setBicolorPixel(column,row,0)
          matrix_3.setBicolorPixel(column,row,color)
