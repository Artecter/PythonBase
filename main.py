from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from base import base_method

import sys


def add_label():
    base_method()


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Python Base")
    window.setGeometry(300, 250, 350, 200)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Работает!")
    main_text.move(100, 100)
    main_text.adjustSize()

    btn = QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText("Нажать!")
    btn.setFixedWidth(200)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
    base_method()