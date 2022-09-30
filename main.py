import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets, QtGui


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    app = QApplication(sys.argv)
    pixmap = QtGui.QPixmap(resource_path("resources/icon.png"))
    splash = QtWidgets.QSplashScreen(pixmap)
    splash.show()
    from measure_app import MeasureApp
    app.processEvents()
    m_a = MeasureApp()
    m_a.show()
    splash.finish(m_a)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()