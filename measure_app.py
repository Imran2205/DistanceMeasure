import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QWidget
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtCore import Qt
import time
from python_ui.distance_measure_app_ui import Ui_MainWindow as MeasureAppUI
from utils.req_functions import distance_calculator
from datetime import datetime
import numpy as np
import pyaudio
from core.blast_detection.keras_yamnet.yamnet import YAMNet, class_names
from core.blast_detection.keras_yamnet.preprocessing import preprocess_input
from copy import deepcopy


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class App(QWidget):
    signal = QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.title = 'File Dialog'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

    def init_ui_save_file(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.save_file_dialog()

    def save_file_dialog(self):
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                "Config Files (*.csv);;All Files (*)")
        if file_name:
            self.signal.emit(file_name)


class MeasureApp(QMainWindow, MeasureAppUI):
    def __init__(self, parent=None):
        super(MeasureApp, self).__init__(parent)
        self.setupUi(self)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFixedSize(850, 600)
        self.pushButton_start.clicked.connect(self.start_timer)
        self.pushButton_stop.clicked.connect(self.stop_timer)
        self.pushButton_measure.clicked.connect(self.measure_dist)
        self.pushButton_stop.setEnabled(False)
        self.pushButton_save.clicked.connect(self.add_row_to_table)
        self.app_save_file = App()
        self.app_save_file.signal.connect(self.export_csv_file)
        self.pushButton_export_data.clicked.connect(self.save_csv)
        self.actionClear_Data.triggered.connect(self.clear_data)
        self.timer_thread = None
        self.explosion_detection_thread = ExplosionDetectionThread()
        self.label_sound_prediction.setText("")
        self.explosion_detection_thread.audio_signal.connect(self.set_sudio_info)
        self.explosion_detection_thread.explosion_signal.connect(self.stop_timer)
        self.milliseconds2 = 0
        self.play = 0
        self.tot_time = 0
        self.row_count_order_table = 0
        self.data_dict = {}
        self.create_table()

    def set_sudio_info(self, pred):
        self.label_sound_prediction.setText(pred)

    def clear_data(self):
        self.timer_thread = None
        self.milliseconds2 = 0
        self.play = 0
        self.tot_time = 0
        self.row_count_order_table = 0
        self.data_dict = {}
        self.create_table()
        self.lcdNumber_time.setProperty("value", 0)
        self.lcdNumber_distance.setProperty("value", 0)
        self.lineEdit_name.setText("")

    def save_csv(self):
        self.app_save_file.init_ui_save_file()

    def export_csv_file(self, file_name):
        csv_file_name = file_name[0]
        data_lines = []
        header = []
        for head in self.data_dict[list(self.data_dict.keys())[0]].keys():
            header.append(str(head))
        data_lines.append(
            ",".join(header)
        )
        for row in self.data_dict.keys():
            row_line = []
            for col in self.data_dict[row].keys():
                row_line.append(
                    str(self.data_dict[row][col])
                )
            data_lines.append(
                ",".join(row_line)
            )
        with open(csv_file_name, 'w') as f:
            f.write("\n".join(data_lines))

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Info.")
        dlg.setText(f"Data exported to {csv_file_name}")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            pass

    def add_row_to_table(self):
        if self.play == 0:
            name = self.lineEdit_name.text()
            time_ms = self.lcdNumber_time.value()
            temp = self.doubleSpinBox_temp.value()
            rel_h = self.spinBox_humidity.value()
            pres = self.spinBox_pressure.value()
            dist = self.lcdNumber_distance.value()
            if name and time_ms and temp and rel_h and pres and dist:
                self.tableWidget.setRowCount(self.row_count_order_table)
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
                    'Required Time(ms)': time_ms,
                    'Temperature(C)': temp,
                    'Relative Humidity(%)': rel_h,
                    'Pressure(pascal)': pres,
                    'Distance(m)': dist
                }
            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Warning!")
                dlg.setText("There is no valid data to be saved...")
                button = dlg.exec()

                if button == QMessageBox.StandardButton.Ok:
                    pass

    def create_table(self):
        self.tableWidget.clear()
        self.row_count_order_table = 1
        self.tableWidget.setRowCount(self.row_count_order_table)
        self.tableWidget.setColumnCount(6)
        row = self.row_count_order_table - 1
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem("Name"))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("Required Time(ms)"))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem("Temperature(C)"))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("Relative Humidity(%)"))
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Pressure(pascal)"))
        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem("Distance(m)"))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.row_count_order_table = self.row_count_order_table + 1
        # self.tableWidget_order_table.move(0, 0)

    def measure_dist(self):
        if self.play == 0:
            req_time = self.lcdNumber_time.value()
            rh = self.spinBox_humidity.value()
            temp = self.doubleSpinBox_temp.value()
            pressure = self.spinBox_pressure.value()
            distance, _ = distance_calculator(
                pressure_pascal=pressure,
                temp_cel=temp,
                rh_perc=rh,
                t_ms=req_time
            )
            self.lcdNumber_distance.setProperty("value", distance)

    def keyPressEvent(self, event):
        # print(event.key())
        if event.key() == Qt.Key.Key_Shift and self.play == 0:
            self.start_timer()
        elif event.key() == Qt.Key.Key_Alt and self.play == 1:
            self.stop_timer()
        elif event.key() == Qt.Key.Key_Control and self.play == 0:
            self.measure_dist()
        elif event.key() == Qt.Key.Key_S and self.play == 0:
            self.add_row_to_table()
        elif event.key() == Qt.Key.Key_Delete:
            self.clear_data()

    def start_timer(self):
        if self.play == 0:
            self.label_sound_prediction.setText("")
            date_time_str = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
            self.lineEdit_name.setText(f"Event_{date_time_str}")
            self.timer_thread = TimerThreadClass()
            self.timer_thread.timer_signal.connect(self.run_time)
            self.explosion_detection_thread.reset()
            self.explosion_detection_thread.start_audio()
            self.milliseconds2 = int(round(time.time() * 1000))
            self.explosion_detection_thread.start()
            self.timer_thread.start()
            self.play = 1
            self.pushButton_start.setEnabled(False)
            self.pushButton_stop.setEnabled(True)
            self.lcdNumber_distance.setProperty("value", 0)
            self.lineEdit_name.setEnabled(False)
            self.tableWidget.setEnabled(False)
            self.doubleSpinBox_temp.setEnabled(False)
            self.spinBox_humidity.setEnabled(False)
            self.spinBox_pressure.setEnabled(False)

    def stop_timer(self):
        if self.play == 1:
            self.timer_thread.terminate()
            self.timer_thread = None
            self.play = 0
            self.pushButton_start.setEnabled(True)
            self.pushButton_stop.setEnabled(False)
            self.lineEdit_name.setEnabled(True)
            self.tableWidget.setEnabled(True)
            self.doubleSpinBox_temp.setEnabled(True)
            self.spinBox_humidity.setEnabled(True)
            self.spinBox_pressure.setEnabled(True)
            self.explosion_detection_thread.stop()
            self.explosion_detection_thread.stop_audio()

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


class ExplosionDetectionThread(QtCore.QThread):
    explosion_signal = QtCore.pyqtSignal('PyQt_PyObject')
    audio_signal = QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self, parent=None):
        super(ExplosionDetectionThread, self).__init__(parent)
        self.thread_active = True
        self.class_labels = True
        self.format = pyaudio.paFloat32
        self.channels = 1
        self.rate = 16000
        self.win_size_sec = 0.175
        self.chunk = int(self.win_size_sec * self.rate)
        self.mic = None
        self.model = YAMNet(weights=resource_path("resources/yamnet.h5"))
        self.yamnet_classes = class_names("resources/yamnet_class_map.csv")
        # self.classes = [k for k in range(len(self.yamnet_classes))]
        self.classes = [
            494, 0, 132, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430
        ]
        self.silent_data = np.load("resources/room_silence.npy")
        self.audio = None
        self.stream = None
        # self.classes_lab = self.yamnet_classes[self.classes]

    def stop(self):
        self.thread_active = False
        # self.wait()

    def reset(self):
        self.thread_active = True

    def start_audio(self):
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=self.format,
            input_device_index=self.mic,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )

    def stop_audio(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def run(self):
        current_class = 0
        run_loop = True
        while run_loop:
            if not self.thread_active:
                break
            if not self.stream:
                break
            data = preprocess_input(np.fromstring(
                self.stream.read(self.chunk), dtype=np.float32), self.rate)
            curr_size = data.shape[0]
            pad_data = data
            if curr_size < 96:
                pad_data = deepcopy(self.silent_data)
                for j in range(20, 22, curr_size):
                    pad_data[j:j + curr_size, 0:64] = data

            prediction = self.model.predict(np.expand_dims(pad_data, 0), verbose=0)[0][self.classes]
            current_class = self.classes[np.argmax(prediction)]
            current_class_name = self.yamnet_classes[current_class]
            prediction_strength = np.max(prediction)
            prediction_string = "{}({}): {:.4f}".format(current_class_name, current_class, prediction_strength)
            self.audio_signal.emit(prediction_string)
            if 420 <= current_class <= 430:
                if prediction_strength >= 0.3:
                    self.explosion_signal.emit(True)
                    run_loop = False


def main():
    app = QApplication(sys.argv)
    pixmap = QtGui.QPixmap(resource_path("resources/icon.png"))
    splash = QtWidgets.QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    m_a = MeasureApp()
    m_a.show()
    splash.finish(m_a)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
