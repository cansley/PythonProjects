# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myDiag.ui'
#
# Created: Mon Sep  8 08:52:09 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dSomeWindow(object):
    def setupUi(self, dSomeWindow):
        dSomeWindow.setObjectName(_fromUtf8("dSomeWindow"))
        dSomeWindow.resize(281, 252)
        self.pushButton = QtGui.QPushButton(dSomeWindow)
        self.pushButton.setGeometry(QtCore.QRect(90, 210, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listView = QtGui.QListView(dSomeWindow)
        self.listView.setGeometry(QtCore.QRect(10, 10, 261, 192))
        self.listView.setObjectName(_fromUtf8("listView"))

        self.retranslateUi(dSomeWindow)
        QtCore.QMetaObject.connectSlotsByName(dSomeWindow)

    def retranslateUi(self, dSomeWindow):
        dSomeWindow.setWindowTitle(_translate("dSomeWindow", "This is my Dialog", None))
        self.pushButton.setText(_translate("dSomeWindow", "PushButton", None))

