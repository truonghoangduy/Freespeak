import os
import sys
import shutil
from datetime import datetime
from os.path import dirname, abspath
import video.utils.handVisualizer as handVisualizer
import video.utils.emotionvisualiser as emotionvisualiser
import gui.resultWrapper as Res

from PyQt5 import QtCore, QtGui, QtWidgets



OUTPUTFOLDER = dirname(abspath(__file__)) + '\\outputFiles'
FOLDERNAME = str(datetime.now().strftime("%d%m%Y-%H%M%S"))
NEWFOLDER = dirname(abspath(__file__)) +'\\presentations\\presentation'+ FOLDERNAME

handVisualizer.visualiser(OUTPUTFOLDER)
emotionvisualiser.visualiser(OUTPUTFOLDER)
os.mkdir(NEWFOLDER)

files = os.listdir(OUTPUTFOLDER)

for f in files:
    shutil.move(OUTPUTFOLDER + '\\' + f, NEWFOLDER)

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
result = Res.ResultWindow(NEWFOLDER,FOLDERNAME)
result.setupUi(Form)
Form.show()
sys.exit(app.exec_())



