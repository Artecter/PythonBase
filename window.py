# 21.06.2021 Copyright Zeggoz

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from data import Data
from convert import csv_write as write
from convert import pdf_write as pdf
import sys


class Window(QMainWindow):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
        super(Window, self).__init__()

        self.setWindowTitle("Python Base")
        self.setGeometry(300, 250, 600, 700)
        self.setWindowIcon(QtGui.QIcon("menu.ico"))
        self.main_txt = QtWidgets.QLabel(self)
        self.txt = QtWidgets.QLabel(self)
        self.enum_btn = QtWidgets.QPushButton(self)
        self.add_btn = QtWidgets.QPushButton(self)
        self.change_btn = QtWidgets.QPushButton(self)
        self.delete_btn = QtWidgets.QPushButton(self)
        self.exit_btn = QtWidgets.QPushButton(self)
        self.contxt_box = QtWidgets.QTextEdit(self)
        self.contxt_box.setFixedWidth(500)
        self.contxt_box.setFixedHeight(150)
        self.contxt_box.hide()
        self.contxt_txt = QtWidgets.QLabel(self)
        self.contxt_txt.move(200, 40)
        self.contxt_btn = QtWidgets.QPushButton(self)
        self.contxt_btn.setText("Далее")
        self.contxt_btn.adjustSize()
        self.contxt_btn.move(250, 200)
        self.contxt_btn.hide()
        self.number_txt = QtWidgets.QLabel(self)
        self.number_txt.setText(f"{self.data[0][0]} №")
        self.number_txt.move(300, 1)
        self.number_txt.hide()
        self.number_box = QtWidgets.QTextEdit(self)
        self.number_box.move(360, 1)
        self.number_box.setFixedWidth(50)
        self.number_box.hide()
        self.number_btn = QtWidgets.QPushButton(self)
        self.number_btn.move(410, 1)
        self.number_btn.setText("-заполнить")
        self.number_btn.adjustSize()
        self.number_btn.clicked.connect(self.fill)
        self.number_btn.hide()

    def fill(self):
        list1 = list()
        for i in self.data[int(self.number_box.toPlainText())][1:]:
            list1.append(i)
        self.contxt_box.setText('\n'.join(list1))

    def choice(self):
        self.contxt_box.move(1000, 1000)
        self.main_txt = QtWidgets.QLabel(self)
        self.main_txt.setText("Выберите: ")
        self.main_txt.move(50, 10)
        self.main_txt.adjustSize()
        self.txt = QtWidgets.QLabel(self)
        self.txt.setText("Пусто: ")
        self.txt.move(200, 5)
        self.txt.adjustSize()
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
        self.contxt_txt.setText("")

    def enum(self):
        self.contxt_box.hide()
        self.txt.setText('')
        self.txt.setText(Data(self.data).enum())
        self.txt.show()
        self.txt.adjustSize()
        self.contxt_txt.setText('')
        self.contxt_btn.hide()
        self.number_box.hide()
        self.number_txt.hide()
        self.number_btn.hide()

    def data_add(self):
        self.data = Data(self.data).add(self.contxt_box.toPlainText().split('\n'))
        self.txt.setText('')
        self.txt.adjustSize()
        self.choice()
        self.contxt_btn.hide()
        self.number_box.hide()
        self.number_txt.hide()
        self.number_btn.hide()

    def add(self):
        self.number_box.show()
        self.number_txt.show()
        self.number_btn.show()
        self.txt.setText("Добавление: ")
        self.txt.adjustSize()
        self.contxt_box.move(300, 40)
        self.contxt_box.setFixedWidth(100)
        text = '\n'.join(self.data[0][1:])
        self.contxt_box.setPlainText("")
        self.contxt_txt.setText(text)
        self.contxt_txt.adjustSize()
        self.contxt_box.show()
        self.contxt_btn.setText("Добавить")
        self.contxt_btn.show()
        self.contxt_btn.clicked.connect(self.data_add)

    def data_change(self):
        self.data = Data(self.data).change(int(self.number_box.toPlainText()),
                                           list(self.contxt_box.toPlainText().split('\n')))
        self.txt.setText("")
        self.txt.adjustSize()
        self.choice()
        self.contxt_btn.hide()
        self.number_box.hide()
        self.number_txt.hide()
        self.number_btn.hide()

    def change(self):
        self.number_box.show()
        self.number_txt.show()
        self.number_btn.show()
        self.txt.setText("Изменение: ")
        self.txt.adjustSize()
        self.contxt_box.move(300, 40)
        self.contxt_box.setFixedWidth(100)
        text = '\n'.join(self.data[0][1:])
        self.contxt_box.setPlainText("")
        self.contxt_txt.setText(text)
        self.contxt_txt.adjustSize()
        self.contxt_box.show()
        self.contxt_btn.setText("Изменить")
        self.contxt_btn.show()
        self.contxt_btn.clicked.connect(self.data_change)

    def data_delete(self):
        self.data = Data(self.data).delete(int(self.number_box.toPlainText()))
        self.txt.setText('')
        self.txt.adjustSize()
        self.choice()
        self.contxt_btn.hide()
        self.number_box.hide()
        self.number_txt.hide()
        self.number_btn.hide()

    def delete(self):
        self.number_box.show()
        self.number_txt.show()
        self.number_btn.show()
        self.txt.setText("Удаление: ")
        self.txt.adjustSize()
        self.contxt_box.move(300, 40)
        self.contxt_box.setFixedWidth(100)
        text = '\n'.join(self.data[0][1:])
        self.contxt_box.setPlainText("")
        self.contxt_txt.setText(text)
        self.contxt_txt.adjustSize()
        self.contxt_box.show()
        self.contxt_btn.setText("Удаление")
        self.contxt_btn.show()
        self.contxt_btn.clicked.connect(self.data_delete)

    def exit(self):
        self.contxt_box.hide()
        self.txt.setText("Выход: ")
        self.txt.adjustSize()
        self.contxt_btn.hide()
        self.contxt_txt.setText("")
        write(self.filename, self.data)
        # pdf(self.filename)
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
