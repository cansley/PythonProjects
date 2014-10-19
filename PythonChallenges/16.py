__author__ = 'cxa70'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# download the image from: http://www.pythonchallenge.com/pc/return/mozart.html : mozart.gif
app = QCoreApplication([])
img = QImage('mozart.gif')

w = img.size().width()
h = img.size().height()

magenta = qRgb(255, 0, 255)
bars = []
for y in range(h):
    for x in range(w-5):
        pixel = img.pixel(x, y)
        opixel = img.pixel(x+4, y)
        if pixel == magenta and opixel == magenta:
            bars.append((x, y))

newImg = QImage(w, h, img.format())

for y in range(h):
    for x in range(w):
        newImg.setPixel((x + w - bars[y][0]) % w, y, img.pixel(x, y))

newImg.save("newMozart.png")
print('done')
