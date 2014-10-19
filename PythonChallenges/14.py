__author__ = 'cxa70'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QCoreApplication([])
img = QImage("wire.png")
o = QImage(100, 100, img.format())

# spiral wrap pixels into new 100x100 png
#directional directives, 1, 0 means increment x by 1, and y by 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y, z = -1, 0, 0

for i in range(200):
    d = dirs[i % 4]  # gets one of the 4 directives in sequential order
    for j in range(100 - (i+1) // 2):  # not sure about this syntax...
        x += d[0]
        y += d[1]
        pixel = img.pixel(z, 0)
        o.setPixel(x, y, pixel)
        z += 1

o.save("14.png")
# results in "cat" image. using this in url tells us name is uzi....next url is uzi