import os, time
import shutil
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal, QTimer

from video.videoAdapter import VideoAdapter
from audio.audioAdapter import AudioAdapter
from video.utils.wpm import plotWPMGraph
from emotionsAnalysis.fileAnalysis import analyze_text_emotions
from emotionsAnalysis.fileAnalysis import analyze_audio_emotions
from faceEmotionDetector.editEmotionsCsv import keep_duplicates


import video.utils.handVisualizer as handVisualizer
import video.utils.emotionvisualiser as emotionvisualiser

import logging

# get the directory of this script
path = os.path.dirname(os.path.abspath(__file__))

WindowUI, WindowBase = uic.loadUiType(
    os.path.join(path, 'templates', 'recordWindow.ui'))

class RecordWindow(WindowBase, WindowUI):
    def __init__(self, parent=None):
        WindowBase.__init__(self, parent)
        self.setupUi(self)

        # own variables
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0)
        self.numberOfWords = 0
        self.video = VideoAdapter()
        self.audio = AudioAdapter(self)
        self.recording = False
        self.audioInitialized = False
        self.videoInitialized = True
        # setup
        self.startStopButton.clicked.connect(self.onStartStopButtonPress)
        self.video.changePixmap.connect(self.setFrame)
        self.video.start()

    def setFrame(self, frame):
        w = self.videoScreen.width() - 1
        h = self.videoScreen.height() - 1
        pixmap = QPixmap.fromImage(frame)
        self.videoScreen.setPixmap(pixmap.scaled(w,h,QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation))
        self.videoScreen.setMinimumSize(1,1)

    def onStartStopButtonPress(self):
        if self.recording:
            if not(self.videoInitialized) or not(self.audioInitialized):
                time.sleep(1)
            self.stopRecording()
        else:
            self.startRecording()
        self.recording = not self.recording

    def startRecording(self):
        logging.info('start recording pressed')
        self.video.startRecording()
        self.videoInitialized = True
        self.audio.start()
        self.videoInitialized = True
        self.startStopButton.setText("stop recording")
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(100)
        self.time.start()

    def stopRecording(self):
        # handle words per minute
        logging.info('stop recording pressed')
        with open(os.path.join('outputFiles', 'wordsPerMinute.txt'), 'w') as wpmFile:
            wordsPerMinute = self.numberOfWords*60000/self.time.elapsed()
            comment = wpm(wordsPerMinute)
            wpmFile.write(comment)
            self.numberOfWords = 0
            logging.info('wpm file written')

        self.timer.stop()
        self.video.stopRecording()
        self.audio.stopRecording()
        self.analyzeAudio(wordsPerMinute)
        self.moveOutput()
        self.startStopButton.setText('start recording')

    def putText(self,stuff):
        logging.info('detected: ' + stuff)
        self.numberOfWords += len(stuff.split())

    def timerEvent(self):
        elapsedTime = QtCore.QTime.fromMSecsSinceStartOfDay(self.time.elapsed())

        self.timerWindow.setText(elapsedTime.toString("mm:ss:zzz")[:8])

    def analyzeAudio(self, wordsPerMinute):
        logging.info('starting analyzeAudio')
        audioFile = os.path.join('outputFiles', 'output.wav')
        textFile = os.path.join('outputFiles', 'output.txt')
        analyze_text_emotions(textFile)
        analyze_audio_emotions(audioFile)
        plotWPMGraph(wordsPerMinute)
        keep_duplicates()

    def moveOutput(self):
        workingDir = os.getcwd()
        outputDir = os.path.join(workingDir, 'outputFiles')
        folderName = 'presentation' + str(datetime.now().strftime("%d%m%Y-%H%M%S"))
        newFolder = os.path.join(workingDir, 'presentations', folderName)

        handVisualizer.visualiser(outputDir)
        emotionvisualiser.visualiser(outputDir)
        os.mkdir(newFolder)

        files = os.listdir(outputDir)

        for f in files:
            if f != ".gitignore" and f != "version.txt":
                shutil.move(os.path.join(outputDir, f), newFolder)

        versionFile = open(os.path.join(outputDir, 'version.txt'), "w")
        versionFile.write(folderName)
        versionFile.close()

def wpm(wordsPerMinute):
    string = "Your WPM score (= words per minute) is {:.3f}.\n".format(wordsPerMinute)
    string += (
        "With the WPM (= words per minute) we can determine, if you talk too fast or too slow.\n"
        "An average person speaks about 100 - 130 words per minute.\n")

    if wordsPerMinute > 130:
        string += (
            "As you can see, your WPM is above the average speaking rate of a person.\n"
            "Speeking too fast will make it harder for your audience to understand you.\n"
            "Also this can be an indication, that you are too nervous in your presentation.\n"
            "Remember to take regular speech breaks, so that the audience can process what they heard!")
    elif wordsPerMinute < 110:
        string += (
            "As you can see, your WPM is below the average speaking rate of a person.\n"
            "It's mostly better to talk too slow, rather than to fast.\n"
            "However, talking too slow may cause your listeners to get bored quickly and not to pay\n"
            "attention to your presentation.")
    else:
        string += "Your speaking speed is balanced!"

    return string
