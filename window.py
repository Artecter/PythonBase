# 21.06.2021 Copyright Zeggoz

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from data import Data
from convert import csv_write as write
import sys


class Window(QMainWindow):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
        super(Window, self).__init__()

        self.setWindowTitle("Python Base")
        self.setGeometry(300, 250, 450, 300)
        self.setWindowIcon(QtGui.QIcon("menu.ico"))
        self.main_text = QtWidgets.QLabel(self)
        self.text = QtWidgets.QLabel(self)
        self.enum_btn = QtWidgets.QPushButton(self)
        self.add_btn = QtWidgets.QPushButton(self)
        self.change_btn = QtWidgets.QPushButton(self)
        self.delete_btn = QtWidgets.QPushButton(self)
        self.exit_btn = QtWidgets.QPushButton(self)
        self.context_box = QtWidgets.QTextEdit(self)
        self.context_box.hide()
        self.context_text = QtWidgets.QLabel(self)
        self.context_text.move(200, 40)
        self.context_btn = QtWidgets.QPushButton(self)
        self.context_btn.setText("Далее")
        self.context_btn.adjustSize()
        self.context_btn.move(250, 250)
        self.context_btn.hide()
        self.number = int()
        self.new_info = list()
        self.number_txt = QtWidgets.QTextEdit(self)
        self.number_txt.hide()
        self.number_box = QtWidgets.QTextEdit(self)
        self.number_box.hide()

    def choice(self):
        self.context_box.move(1000, 1000)
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Выберите: ")
        self.main_text.move(50, 10)
        self.main_text.adjustSize()
        self.text = QtWidgets.QLabel(self)
        self.text.setText("Пусто: ")
        self.text.move(200, 10)
        self.text.adjustSize()
        self.enum_btn.move(25, 25)
        self.enum_btn.setText("Список")
        self.enum_btn.clicked.connect(self.enum)
        self.add_btn.move(25, 50)
        self.add_btn.setText("Добавление")
        self.add_btn.clicked.connect(self.add)
        self.change_btn.move(25, 75)
        self.change_btn.setText("Изменение")
        self.change_btn.clicked.connect(self.change)
        self.delete_btn.move(25, 100)
        self.delete_btn.setText("Удаление")
        self.delete_btn.clicked.connect(self.delete)
        self.exit_btn.move(25, 125)
        self.exit_btn.setText("Выход")
        self.exit_btn.clicked.connect(self.exit)
        self.context_text.setText("")

    def enum(self):
        self.context_box.hide()
        self.text.setText("")
        self.text.setText(Data(self.data).enum())
        self.text.show()
        self.text.adjustSize()
        self.context_text.setText("")
        self.context_btn.hide()

    def add_data(self):
        self.data = Data(self.data).add(self.context_box.toPlainText().split('\n'))
        self.text.setText("Добавлено!")
        self.choice()
        self.context_btn.hide()

    def add(self):
        self.number = 1
        self.context_box.hide()
        self.text.setText("Добавление: ")
        self.text.adjustSize()
        self.context_box.move(300, 40)
        self.context_box.setFixedWidth(100)
        text = '\n'.join(self.data[0][1:])
        self.context_box.setPlainText("")
        self.context_box.adjustSize()
        self.context_text.setText(text)
        self.context_text.adjustSize()
        self.context_box.show()
        self.context_btn.setText("Добавить")
        self.context_btn.show()
        self.context_btn.clicked.connect(self.add_data)

    def change(self):
        self.number = 1
        self.context_box.hide()
        self.text.setText("Изменение: ")
        self.text.adjustSize()
        self.context_box.move(300, 40)
        self.context_box.setFixedWidth(100)
        text = '\n'.join(self.data[0][1:])
        self.context_box.setPlainText(text)
        self.context_box.adjustSize()
        self.context_text.setText(text)
        self.context_text.adjustSize()
        self.context_box.show()
        self.context_btn.setText("Изменить")
        self.context_btn.show()
        self.context_btn.clicked.connect(self.add_data)

    def delete(self):
        # Text
        self.text.setText("Удаление: ")
        self.text.adjustSize()
        self.context_box.move(200, 75)
        self.context_box.setFixedWidth(100)
        self.context_box.setPlainText("1")
        self.context_text.setText(f"{self.data[0][0]} №")
        self.context_box.show()
        self.number = int(self.context_box.toPlainText())
        self.context_btn.show()

    def exit(self):
        # Textbox1
        self.context_box.hide()
        self.text.setText("Выход: ")
        self.text.adjustSize()
        self.context_btn.hide()
        self.context_text.setText("")
        write(self.filename, self.data)
        exit(0)

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


def application(filename, data):

    app = QApplication(sys.argv)
    window = Window(filename, data)

    window.choice()
    window.show()
    sys.exit(app.exec_())
