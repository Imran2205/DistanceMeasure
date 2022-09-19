import sys
import _init_paths
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
import time
from python_ui.distance_measure_app_ui import Ui_MainWindow as MeasureAppUI
from utils.req_functions import distance_calculator
from datetime import datetime


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
        self.pushButton_save.clicked.connect(self.add_row_to_table)
        self.timer_thread = None
        self.milliseconds2 = 0
        self.play = 0
        self.tot_time = 0
        self.row_count_order_table = 0
        self.create_table()
        self.data_dict = {}

    def add_row_to_table(self):
        name = self.lineEdit_name.text()
        time_ms = self.lcdNumber_time.value()
        temp = self.doubleSpinBox_temp.value()
        rel_h = self.spinBox_humidity.value()
        pres = self.spinBox_pressure.value()
        dist = self.lcdNumber_distance.value()
        if name and time_ms and temp and rel_h and pres and dist:
            self.tableWidget.setRowCount(self.row_count_order_table)
            self.tableWidget.setColumnCount(6)
            row = self.row_count_order_table - 1
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(time_ms)))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(temp)))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(rel_h)))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(pres)))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(dist)))
            self.row_count_order_table = self.row_count_order_table + 1
            self.data_dict[name] = {
                'Name': name,
                'Time(ms)': time_ms,
                'Temperature(C)': temp,
                'Relative Humidity(%)': rel_h,
                'Pressure(pascal)': pres,
                'Distance(m)': dist
            }

    def create_table(self):
        self.tableWidget.clear()
        self.row_count_order_table = 1
        self.tableWidget.setRowCount(self.row_count_order_table)
        self.tableWidget.setColumnCount(6)
        row = self.row_count_order_table - 1
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Name"))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("Time(ms)"))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem("Temperature(C)"))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("Relative Humidity(%)"))
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Pressure(pascal)"))
        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem("Distance(m)"))
        self.row_count_order_table = self.row_count_order_table + 1
        # self.tableWidget_order_table.move(0, 0)

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
        date_time_str = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
        self.lineEdit_name.setText(f"event_{date_time_str}")
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
