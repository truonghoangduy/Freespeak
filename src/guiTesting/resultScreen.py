import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic

# get the directory of this script
path = os.path.dirname(os.path.abspath(__file__))

WindowUI, WindowBase = uic.loadUiType(
    os.path.join(path, 'templates', 'resultScreen.ui'))

class ResultScreen(WindowBase, WindowUI):
    def __init__(self, parent=None):
        WindowBase.__init__(self, parent)
        self.setupUi(self)
        self.scaledImages = []
        self.version = None
        self.tabWidget.currentChanged.connect(lambda: self.load())

    def load(self):
        if self.version is not None:
            self.path = os.path.join('presentations', self.version)
            #self.titleLabel.setText(self.version)

            # hand positions tab
            self.setPixmapScaled(self.handImage, 'handposPlot.png')
            with open (os.path.join(self.path, 'handGesturesAdvicer.txt'), 'r') as file:
                text = file.read()
                self.handsText.setText(text)

           # face expression tab
            self.setPixmapScaled(self.faceExpressionPieChart, 'facialEmotionsChart.png')
            self.setPixmapScaled(self.faceExpressionScatter, 'emotionsPlot.png')
            with open (os.path.join(self.path, 'facialExpressionsAdvices.txt'), 'r') as file:
                text = file.read()
                self.faceExpressionTips.setText(text)

            # text emotion tab
            self.setPixmapScaled(self.textEmotionImage, 'textEmotions.png')

            with open (os.path.join(self.path, 'textEmotionsExplanation.txt'), 'r') as file:
                text = file.read()
                self.textEmotionText.setText(text)

            # speech emotion tab
            self.setPixmapScaled(self.speechEmotionImage, 'speechEmotionsChart.png')
            with open (os.path.join(self.path, 'speechEmotionsTippsAndAdvices.txt'), 'r') as file:
                text = file.read()
                self.speechEmotionText.setText(text)

            # WPM tab
            self.setPixmapScaled(self.wpmImage, 'wpmGraph.png')
            with open (os.path.join(self.path, 'wordsPerMinute.txt'), 'r') as file:
                text = file.read()
                self.wpmText.setText(text)

    # for initial picture setting
    # images are then automatically rescaled in the future
    def setPixmapScaled(self, destination, filename):
        pixmap = QtGui.QPixmap(os.path.join(self.path, filename))
        self.resizePixmap(destination, pixmap)
        self.scaledImages.append((destination, pixmap))

    # rescaling a single image
    def resizePixmap(self, destination, pixmap):
        w = destination.width() - 1
        h = destination.height() - 1
        destination.setPixmap(pixmap.scaled(w,h,QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))
        destination.setMinimumSize(1,1)

    # gets called every time user resizes window
    def resizeEvent(self, event):
        QtWidgets.QWidget.resizeEvent(self, event)
        for (destination, pixmap) in self.scaledImages:
            self.resizePixmap(destination,pixmap)
