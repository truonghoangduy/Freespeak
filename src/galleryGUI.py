# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'galleryGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from os.path import abspath,dirname
import gui.resultWrapper as Res
from threading import Thread


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1076, 898)
        Form.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, -10, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.presentationsList = QtWidgets.QListWidget(Form)
        self.presentationsList.setGeometry(QtCore.QRect(0, 129, 1076, 711))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.presentationsList.setFont(font)
        self.presentationsList.setStyleSheet("background-color: rgb(160,160,160);")
        self.presentationsList.setObjectName("presentationsList")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.backButton.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "Saved presentations"))
        self.folderName = dirname(abspath(__file__)) + '\presentations'
        for f,g,h in os.walk(self.folderName):
            if f != self.folderName:
                self.presentationsList.addItem(f[len(self.folderName):])
        self.presentationsList.itemClicked.connect(self.item_click)    

    def item_click(self,item):
        global newWindow 
        newWindow = QtWidgets.QWidget()
        result = Res.ResultWindow(self.folderName + item.text(),item.text()[13:],self)
        result.setupUi(newWindow)
        newWindow.show()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
