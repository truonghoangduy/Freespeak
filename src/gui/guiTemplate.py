# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1076, 898)
        font = QtGui.QFont()
        font.setPointSize(14)
        Form.setFont(font)
        Form.setStyleSheet("\n"
"background-color: rgb(186, 186, 186);")
        self.startStopButton = QtWidgets.QPushButton(Form)
        self.startStopButton.setGeometry(QtCore.QRect(20, 810, 1041, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startStopButton.sizePolicy().hasHeightForWidth())
        self.startStopButton.setSizePolicy(sizePolicy)
        self.startStopButton.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.startStopButton.setFont(font)
        self.startStopButton.setAutoDefault(False)
        self.startStopButton.setDefault(False)
        self.startStopButton.setFlat(False)
        self.startStopButton.setObjectName("startStopButton")
        self.output = QtWidgets.QLabel(Form)
        self.output.setGeometry(QtCore.QRect(20, 680, 1041, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output.setFont(font)
        self.output.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.output.setObjectName("output")
        self.timerLabel = QtWidgets.QLabel(Form)
        self.timerLabel.setGeometry(QtCore.QRect(30, 490, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timerLabel.setFont(font)
        self.timerLabel.setObjectName("timerLabel")
        self.timer = QtWidgets.QLabel(Form)
        self.timer.setGeometry(QtCore.QRect(30, 550, 241, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.timer.setFont(font)
        self.timer.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.timer.setText("")
        self.timer.setObjectName("timer")
        self.wpmLabel = QtWidgets.QLabel(Form)
        self.wpmLabel.setGeometry(QtCore.QRect(300, 500, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wpmLabel.setFont(font)
        self.wpmLabel.setObjectName("wpmLabel")
        self.wordsPerMin = QtWidgets.QLabel(Form)
        self.wordsPerMin.setGeometry(QtCore.QRect(300, 550, 241, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.wordsPerMin.setFont(font)
        self.wordsPerMin.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.wordsPerMin.setText("")
        self.wordsPerMin.setObjectName("wordsPerMin")
        self.videoScreen = QtWidgets.QLabel(Form)
        self.videoScreen.setGeometry(QtCore.QRect(20, 20, 1021, 461))
        self.videoScreen.setAlignment(QtCore.Qt.AlignCenter)
        self.videoScreen.setObjectName("videoScreen")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.startStopButton.setText(_translate("Form", "Start Recording"))
        self.output.setText(_translate("Form", "Press \"Start Recording\" to start..."))
        self.timerLabel.setText(_translate("Form", "Timer"))
        self.wpmLabel.setText(_translate("Form", "Words per minute"))
        self.videoScreen.setText(_translate("Form", "Please wait for the camera to load..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

