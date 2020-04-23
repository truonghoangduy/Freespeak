from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from guiTesting.guiManager import GuiManager
import qdarkstyle
import logging

if __name__ == "__main__":
    logging.basicConfig(level='INFO')

    import sys
    app = QtWidgets.QApplication(sys.argv)

    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)

    mainWindow = GuiManager()

    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    mainWindow.show()

    sys.exit(app.exec_())
