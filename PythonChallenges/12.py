__author__ = 'cxa70'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# download the image from: http://www.pythonchallenge.com/pc/return/evil1.jpg
app = QCoreApplication([])

stuff = ""
bytes = b""
with open("evil2.gfx", "rb") as f:

    byte = f.read(1)
    while byte != b"":
        bytes += byte
        byte = f.read(1)

files = [('jpg', bytes[0::5]), ('png', bytes[1::5]), ('gif', bytes[2::5]), ('png', bytes[3::5]), ('jpg', bytes[4::5])]

for i in range(5):
    open('evil2-%d.%s' % (i, files[i][0]), 'wb').write(files[i][1])