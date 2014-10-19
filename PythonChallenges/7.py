__author__ = 'cxa70'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ast

app = QCoreApplication([])
image = QImage("oxygen.png")
image.size()
sz = image.size()
y = sz.height()/2
val = ''

for x in range(0, sz.width(), 7):
    px = QColor(image.pixel(x, y))
    val += chr(px.getRgb()[0])

start_idx = val.find('[')
end_idx = val.find(']')
stub = val[start_idx:end_idx+1]
lvl = ast.literal_eval(stub)
slvl = ""
for x in lvl:
    slvl += chr(x)

print(val[:start_idx-1] + ': ' + slvl)
