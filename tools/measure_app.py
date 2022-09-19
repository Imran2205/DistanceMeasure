import sys

import _init_paths
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
import time
from python_ui.distance_measure_app_ui import Ui_MainWindow as MeasureAppUI


class MeasureApp(QMainWindow, MeasureAppUI):
    def __init__(self, parent=None):
        super(MeasureApp, self).__init__(parent)
        self.setupUi(self)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.pushButton_start.clicked.connect(self.start_timer)
        self.pushButton_stop.clicked.connect(self.stop_timer)
        self.pushButton_stop.setEnabled(False)
        self.timer_thread = None
        self.milliseconds2 = 0
        self.play = 0
        self.tot_time = 0

    def keyPressEvent(self, event):
        print(event.text())
        if event.key() == Qt.Key.Key_Up and self.play==0:
            self.start_timer()
        elif event.key() == Qt.Key.Key_Down and self.play==1:
            self.stop_timer()

    def start_timer(self):
        self.timer_thread = TimerThreadClass()
        self.timer_thread.timer_signal.connect(self.run_time)
        self.milliseconds2 = int(round(time.time() * 1000))
        self.timer_thread.start()
        self.play = 1
        self.pushButton_start.setEnabled(False)
        self.pushButton_stop.setEnabled(True)

    def stop_timer(self):
        self.timer_thread.terminate()
        self.timer_thread = None
        self.play = 0
        self.pushButton_start.setEnabled(True)
        self.pushButton_stop.setEnabled(False)

    def run_time(self, t):
        if self.play == 1:
            self.tot_time = t - self.milliseconds2
            self.lcdNumber_time.setProperty("value", self.tot_time)


class TimerThreadClass(QtCore.QThread):
    timer_signal = QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self, parent=None):
        super(TimerThreadClass, self).__init__(parent)

    def run(self):
        while 1:
            milliseconds = int(round(time.time() * 1000))
            self.timer_signal.emit(milliseconds)
            time.sleep(0.0005)


def main():
    app = QApplication(sys.argv)
    m_a = MeasureApp()
    m_a.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
