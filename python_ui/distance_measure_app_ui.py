# Form implementation generated from reading ui file '.\ui\distance_measure_app_ui.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui\\icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setMinimumSize(QtCore.QSize(100, 0))
        self.label_11.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.comboBox_serial_ports = QtWidgets.QComboBox(self.frame)
        self.comboBox_serial_ports.setObjectName("comboBox_serial_ports")
        self.gridLayout_3.addWidget(self.comboBox_serial_ports, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 4, 0, 1, 5)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 10, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 3, 1, 1)
        self.lcdNumber_distance = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber_distance.setMinimumSize(QtCore.QSize(150, 50))
        self.lcdNumber_distance.setMaximumSize(QtCore.QSize(150, 50))
        self.lcdNumber_distance.setDigitCount(7)
        self.lcdNumber_distance.setObjectName("lcdNumber_distance")
        self.gridLayout_2.addWidget(self.lcdNumber_distance, 1, 10, 1, 1)
        self.doubleSpinBox_temp = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_temp.setMinimum(-100.0)
        self.doubleSpinBox_temp.setMaximum(100.0)
        self.doubleSpinBox_temp.setProperty("value", 25.0)
        self.doubleSpinBox_temp.setObjectName("doubleSpinBox_temp")
        self.gridLayout_2.addWidget(self.doubleSpinBox_temp, 2, 1, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_2.addWidget(self.pushButton_stop, 1, 7, 1, 2)
        self.label_sound_prediction = QtWidgets.QLabel(self.frame_2)
        self.label_sound_prediction.setText("")
        self.label_sound_prediction.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_sound_prediction.setObjectName("label_sound_prediction")
        self.gridLayout_2.addWidget(self.label_sound_prediction, 3, 0, 1, 12)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 6, 1, 2)
        self.spinBox_pressure = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_pressure.setMinimum(70000)
        self.spinBox_pressure.setMaximum(150000)
        self.spinBox_pressure.setProperty("value", 101325)
        self.spinBox_pressure.setObjectName("spinBox_pressure")
        self.gridLayout_2.addWidget(self.spinBox_pressure, 2, 8, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 5, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_save.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_save.setMaximumSize(QtCore.QSize(16777215, 35))
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout_2.addWidget(self.pushButton_save, 2, 10, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 2)
        self.pushButton_start = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_start.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_start.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_2.addWidget(self.pushButton_start, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 6, 1, 1)
        self.pushButton_measure = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_measure.setMinimumSize(QtCore.QSize(80, 60))
        self.pushButton_measure.setMaximumSize(QtCore.QSize(60, 60))
        self.pushButton_measure.setObjectName("pushButton_measure")
        self.gridLayout_2.addWidget(self.pushButton_measure, 1, 9, 1, 1)
        self.lcdNumber_time = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber_time.setMinimumSize(QtCore.QSize(150, 50))
        self.lcdNumber_time.setMaximumSize(QtCore.QSize(150, 50))
        self.lcdNumber_time.setSmallDecimalPoint(False)
        self.lcdNumber_time.setDigitCount(7)
        self.lcdNumber_time.setProperty("value", 0.0)
        self.lcdNumber_time.setObjectName("lcdNumber_time")
        self.gridLayout_2.addWidget(self.lcdNumber_time, 1, 3, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setMinimumSize(QtCore.QSize(20, 0))
        self.label_6.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_name.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_2.addWidget(self.lineEdit_name, 1, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 11, 1, 1)
        self.doubleSpinBox_humidity = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_humidity.setMaximum(100.0)
        self.doubleSpinBox_humidity.setProperty("value", 60.0)
        self.doubleSpinBox_humidity.setObjectName("doubleSpinBox_humidity")
        self.gridLayout_2.addWidget(self.doubleSpinBox_humidity, 2, 4, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 5)
        self.toolButton_refresh = QtWidgets.QToolButton(self.frame)
        self.toolButton_refresh.setObjectName("toolButton_refresh")
        self.gridLayout_3.addWidget(self.toolButton_refresh, 0, 2, 1, 1)
        self.label_connection_status = QtWidgets.QLabel(self.frame)
        self.label_connection_status.setMinimumSize(QtCore.QSize(350, 0))
        self.label_connection_status.setMaximumSize(QtCore.QSize(350, 16777215))
        self.label_connection_status.setText("")
        self.label_connection_status.setObjectName("label_connection_status")
        self.gridLayout_3.addWidget(self.label_connection_status, 0, 4, 1, 1)
        self.plainTextEdit_serial_log = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_serial_log.setMinimumSize(QtCore.QSize(0, 30))
        self.plainTextEdit_serial_log.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEdit_serial_log.setObjectName("plainTextEdit_serial_log")
        self.gridLayout_3.addWidget(self.plainTextEdit_serial_log, 1, 0, 1, 5)
        self.pushButton_serial_connect = QtWidgets.QPushButton(self.frame)
        self.pushButton_serial_connect.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_serial_connect.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_serial_connect.setObjectName("pushButton_serial_connect")
        self.gridLayout_3.addWidget(self.pushButton_serial_connect, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.pushButton_export_data = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export_data.setObjectName("pushButton_export_data")
        self.gridLayout.addWidget(self.pushButton_export_data, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClear_Data = QtGui.QAction(MainWindow)
        self.actionClear_Data.setObjectName("actionClear_Data")
        self.menuMenu.addAction(self.actionClear_Data)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MeasureDistance"))
        self.label_11.setText(_translate("MainWindow", "Serial Port"))
        self.label.setText(_translate("MainWindow", "Temperature"))
        self.label_3.setText(_translate("MainWindow", "Distance"))
        self.label_2.setText(_translate("MainWindow", "Humidity"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.label_4.setText(_translate("MainWindow", "Time"))
        self.label_10.setText(_translate("MainWindow", "Pressure"))
        self.label_7.setText(_translate("MainWindow", "%"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.label_9.setText(_translate("MainWindow", "ms"))
        self.pushButton_measure.setText(_translate("MainWindow", "Measure"))
        self.label_6.setText(_translate("MainWindow", "C"))
        self.label_8.setText(_translate("MainWindow", "m"))
        self.toolButton_refresh.setText(_translate("MainWindow", "..."))
        self.pushButton_serial_connect.setText(_translate("MainWindow", "Connect"))
        self.pushButton_export_data.setText(_translate("MainWindow", "Export Data to CSV"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionClear_Data.setText(_translate("MainWindow", "Clear Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
