# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1076, 898)
        Form.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 0, 581, 191))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.infoButton = QtWidgets.QPushButton(Form)
        self.infoButton.setGeometry(QtCore.QRect(20, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.infoButton.setFont(font)
        self.infoButton.setObjectName("infoButton")
        self.appButton = QtWidgets.QPushButton(Form)
        self.appButton.setGeometry(QtCore.QRect(60, 330, 400, 400))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.appButton.setFont(font)
        self.appButton.setStyleSheet("")
        self.appButton.setObjectName("appButton")
        self.galleryButton = QtWidgets.QPushButton(Form)
        self.galleryButton.setGeometry(QtCore.QRect(590, 330, 400, 400))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.galleryButton.setFont(font)
        self.galleryButton.setStyleSheet("")
        self.galleryButton.setObjectName("galleryButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Presentation Trainer"))
        self.infoButton.setText(_translate("Form", "i"))
        self.appButton.setText(_translate("Form", "APP"))
        self.galleryButton.setText(_translate("Form", "GALLERY"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
