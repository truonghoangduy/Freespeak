from PyQt5 import QtWidgets
from guiTesting.recordWindow import RecordWindow
from PyQt5.QtCore import QTimer

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)

    mainWindow = RecordWindow()

    mainWindow.show()

    sys.exit(app.exec_())
