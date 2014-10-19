__author__ = 'cxa70'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# download the image from: http://www.pythonchallenge.com/pc/return/cave.jpg
app = QCoreApplication([])
original = QImage("cave.jpg")
o_width = original.size().width()
o_height = original.size().height()
odd = QImage(o_width/2, o_height/2, original.format())
even = QImage(o_width/2, o_height/2, original.format())

for x in range(o_width):
    for y in range(o_height):
        if x % 2 == 0 and y % 2 == 0:
            even.setPixel(x/2, y/2, original.pixel(x, y))
            #even.putpixel((x / 2, y / 2), image.getpixel((x, y)))
        elif x % 2 == 0 and y % 2 == 1:
            odd.setPixel(x/2, (y-1)/2, original.pixel(x, y))
            #odd.putpixel((x / 2, (y - 1) / 2), image.getpixel((x, y)))
        elif x % 2 == 1 and y % 2 == 0:
            even.setPixel((x-1)/2, y/2, original.pixel(x, y))
            #even.putpixel(((x - 1) / 2, y / 2), image.getpixel((x, y)))
        else:
            odd.setPixel((x-1)/2, (y-1)/2, original.pixel(x, y))
            #odd.putpixel(((x - 1) / 2, (y - 1) / 2), image.getpixel((x, y)))

even.save("even.jpg")
odd.save("odd.jpg")