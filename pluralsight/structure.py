from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
import sys
from myDiag import Ui_dSomeWindow
from enum import Enum


class Color(Enum):
    Red = 1
    Green = 2
    Blue = 3


class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_dSomeWindow()
        self.ui.setupUi(self)


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        self.label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")
        line_edit.setPlaceholderText("Enter your text here...")

        layout.addWidget(self.label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.change_text_label)
        self.setFocus()

    def change_text_label(self, text):
        self.label.setText(text)



app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()