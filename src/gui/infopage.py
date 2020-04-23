# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\infopage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoPage(object):
    def setupUi(self, InfoPage):
        InfoPage.setObjectName("InfoPage")
        InfoPage.resize(1076, 898)
        self.centralwidget = QtWidgets.QWidget(InfoPage)
        self.centralwidget.setObjectName("centralwidget")
        self.InfoPageTab = QtWidgets.QTabWidget(self.centralwidget)
        self.InfoPageTab.setGeometry(QtCore.QRect(0, 0, 1076, 898))
        self.InfoPageTab.setObjectName("InfoPageTab")
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.textBrowser = QtWidgets.QTextBrowser(self.About)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1076, 721))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.About)
        self.pushButton.setGeometry(QtCore.QRect(294, 759, 541, 41))
        self.pushButton.setObjectName("pushButton")
        self.InfoPageTab.addTab(self.About, "")
        self.Tipps = QtWidgets.QWidget()
        self.Tipps.setObjectName("Tipps")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Tipps)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 1076, 898))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.InfoPageTab.addTab(self.Tipps, "")
        InfoPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InfoPage)
        self.statusbar.setObjectName("statusbar")
        InfoPage.setStatusBar(self.statusbar)

        self.retranslateUi(InfoPage)
        self.InfoPageTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InfoPage)

    def retranslateUi(self, InfoPage):
        _translate = QtCore.QCoreApplication.translate
        InfoPage.setWindowTitle(_translate("InfoPage", "Info Page"))
        self.About.setToolTip(_translate("InfoPage", "<html><head/><body><p><br/></p></body></html>"))
        self.textBrowser.setHtml(_translate("InfoPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.14286pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#656565;\">About our program:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Public speaking is nowadays a common task in our daily life performed by every type of individual in every kind of domain possible, such as presentations and seminars by students or pitches by innovators.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">However, this type of task requires skill and cannot be mastered by everyone with ease. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Furthermore, the fear of public speaking is very common and sometimes hard to overcome. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Nonetheless, it is part of our education and our work life and therefore inevitable. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">That is where our presentation trainer comes in! </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The trainer is an application that helps people with difficulties in public speaking and overcome their fear </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">by providing sophisticated training as a preparation for their incoming presentation.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">It records speech and movements of the speaker in a video and analyses his/her speak pattern.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">A rating will be given at the end along with tips of improvements.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.14286pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#656565;\">Features:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> - Records voice and video</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> - Analyzes voice emotions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> - Analyzes text sentiment</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> - Analyzes facial expression</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> - Analyzes gesture (please make sure to keep a distance to your computer so that our program can analyze your hand movements through the camera!)</span></p></body></html>"))
        self.pushButton.setText(_translate("InfoPage", "SKIP"))
        self.InfoPageTab.setTabText(self.InfoPageTab.indexOf(self.About), _translate("InfoPage", "About"))
        self.Tipps.setWhatsThis(_translate("InfoPage", "<html><head/><body><p><span style=\" font-size:9pt;\">eeeh</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("InfoPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.14286pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">For blablalba we asked some professionals to name the most important aspects while holding a presentation!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">On this page, we listed all of them:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.InfoPageTab.setTabText(self.InfoPageTab.indexOf(self.Tipps), _translate("InfoPage", "Tipps"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoPage = QtWidgets.QMainWindow()
    ui = Ui_InfoPage()
    ui.setupUi(InfoPage)
    InfoPage.show()
    sys.exit(app.exec_())
