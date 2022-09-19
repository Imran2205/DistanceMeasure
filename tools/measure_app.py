import sys
import _init_paths
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
import time
from python_ui.distance_measure_app_ui import Ui_MainWindow as MeasureAppUI
from utils.req_functions import distance_calculator


class MeasureApp(QMainWindow, MeasureAppUI):
    def __init__(self, parent=None):
        super(MeasureApp, self).__init__(parent)
        self.setupUi(self)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFixedSize(800, 600)
        self.pushButton_start.clicked.connect(self.start_timer)
        self.pushButton_stop.clicked.connect(self.stop_timer)
        self.pushButton_measure.clicked.connect(self.measure_dist)
        self.pushButton_stop.setEnabled(False)
        self.timer_thread = None
        self.milliseconds2 = 0
        self.play = 0
        self.tot_time = 0

    def measure_dist(self):
        req_time = self.lcdNumber_time.value()
        rh = self.spinBox_humidity.value()
        temp = self.doubleSpinBox_temp.value()
        pressure = self.spinBox_pressure.value()
        distance = distance_calculator(
            pressure_pascal=pressure,
            temp_cel=temp,
            rh_perc=rh,
            t_ms=req_time
        )
        self.lcdNumber_distance.setProperty("value", round(distance))

    def keyPressEvent(self, event):
        print(event.text())
        if event.key() == Qt.Key.Key_Up and self.play == 0:
            self.start_timer()
        elif event.key() == Qt.Key.Key_Down and self.play == 1:
            self.stop_timer()
        elif event.key() == Qt.Key.Key_Return and self.play == 0:
            self.measure_dist()

    def start_timer(self):
        self.timer_thread = TimerThreadClass()
        self.timer_thread.timer_signal.connect(self.run_time)
        self.milliseconds2 = int(round(time.time() * 1000))
        self.timer_thread.start()
        self.play = 1
        self.pushButton_start.setEnabled(False)
        self.pushButton_stop.setEnabled(True)
        self.lcdNumber_distance.setProperty("value", 0)

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
