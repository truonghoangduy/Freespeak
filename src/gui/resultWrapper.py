import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal, QTimer

from gui.resultScreen import Ui_Form as myUi


class ResultWindow(object):
    def __init__(self,path,name,parent = None):
        super(ResultWindow, self).__init__()
        self.ui = myUi()
        self.path = path
        self.name = name
        self.text = self.extractText()


    def setupUi(self, Form):
        self.ui.setupUi(Form)
        self.ui.titleLabel.setText('Presentation ' + self.name)
        self.ui.pictureLabel.setPixmap(QtGui.QPixmap(self.path+'\\handposPlot.png'))
        self.ui.faceScatter.setPixmap(QtGui.QPixmap(self.path+'\\emotionsPlot.png'))
        self.ui.speechPie.setPixmap(QtGui.QPixmap(self.path+'\\speech_emotions_analysis.png'))
        self.ui.scorePic.setPixmap(QtGui.QPixmap(self.path+'\\text_emotions.png'))
        self.ui.facePieChart.setPixmap(QtGui.QPixmap(self.path+'\\facialEmotionsChart.png'))
        self.ui.score.setText(self.text[0])
        explanation = ''
        for i in range(1,len(self.text)):
            explanation += self.text[i]
        self.ui.explanationText.setText(explanation)


    def extractText(self):
        lines = []
        with open (self.path +'\\' + 'textEmotionsExplanation.txt', 'rt') as file:
            for line in file:
                    lines.append(line)
        return lines