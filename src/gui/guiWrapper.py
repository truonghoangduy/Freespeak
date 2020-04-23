import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal, QTimer
from gui.guiTemplate import Ui_Form as myUi

from video.videoAdapter import VideoAdapter
from audio.audioAdapter import AudioAdapter
from emotionsAnalysis.file_analysis import analyze_text_emotions
from emotionsAnalysis.file_analysis import analyze_audio_emotions
from faceEmotionDetector.editEmotionsCsv import keep_duplicates

class MainWindow(object):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = myUi()

        # own variables
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)
        self.numberOfWords = 0
        self.video = VideoAdapter()
        self.audio = AudioAdapter(self)
        self.recording = False

    def setupUi(self, Form):
        self.ui.setupUi(Form)
        self.ui.startStopButton.clicked.connect(self.onStartStopButtonPress)
        self.video.changePixmap.connect(self.setFrame)
        self.video.start()

    def setFrame(self, frame):
        self.ui.videoScreen.setPixmap(QPixmap.fromImage(frame))

    def translateUi(self, Form):
        self.ui.translateUi(Form)

    def start(self):
      app = QtWidgets.QApplication(sys.argv)
      Form = QtWidgets.QWidget()
      ui = MainWindow()
      ui.setupUi(Form)
      timer = QTimer()
      timer.timeout.connect(lambda: None)
      timer.start(100)
      Form.show()
      sys.exit(app.exec_())

    def onStartStopButtonPress(self):
        if self.recording:
            self.stopRecording()
        else:
            self.startRecording()
        self.recording = not self.recording

    def startRecording(self):
        self.video.startRecording()
        self.audio.start()
        self.ui.startStopButton.setText("stop recording")
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1)

    def stopRecording(self):
        self.timer.stop()
        self.video.stopRecording()
        self.audio.stopRecording()
        self.ui.startStopButton.setText("start recording")
        self.analyzeAudio()

    def putText(self,stuff):
        self.ui.output.setText(stuff)
        self.numberOfWords += len(stuff.split())

    def timerEvent(self):
        self.time = self.time.addMSecs(1)
        self.ui.timer.setText(self.time.toString("mm:ss:zzz"))
        elapsedTime = self.time.elapsed()
        #print("words per min" + str((self.numberOfWords*60000)/elapsedTime))
        self.ui.wordsPerMin.setText(str((self.numberOfWords*60000)/elapsedTime))

    def analyzeAudio(self):
        audioFile = "outputFiles\\output.wav"
        textFile = "outputFiles\\output.txt"
        analyze_text_emotions(textFile)
        analyze_audio_emotions(audioFile)
        keep_duplicates()
