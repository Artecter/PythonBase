# 21.06.2021 Copyright Zeggoz

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from data import Data
from convert import csv_write as write
import sys


class Window(QMainWindow):
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data
        super(Window, self).__init__()

        self.setWindowTitle("Python Base")
        self.setGeometry(300, 250, 450, 200)
        # MainText
        self.main_text = QtWidgets.QLabel(self)
        # Text
        self.text = QtWidgets.QLabel(self)
        # Button1
        self.button1 = QtWidgets.QPushButton(self)
        # Button2
        self.button2 = QtWidgets.QPushButton(self)
        # Button3
        self.button3 = QtWidgets.QPushButton(self)
        # Button4
        self.button4 = QtWidgets.QPushButton(self)
        # Button5
        self.button5 = QtWidgets.QPushButton(self)
        # TextBox1
        self.text_box1 = QtWidgets.QTextEdit(self)
        self.text_box1.hide()
        # ContextText
        self.context_text = QtWidgets.QLabel(self)
        self.context_text.move(200, 40)
        # ContextButton
        self.context_button = QtWidgets.QPushButton(self)
        self.context_button.setText("Далее")
        self.context_button.adjustSize()
        self.context_button.move(200, 120)
        self.context_button.hide()
        # for changes
        self.number = int()
        self.new_info = list()

    def delete_data(self):
        Data(self.data).delete(self.number)
        self.choice()
        self.context_text.setText(f"Удалено {self.data[0][0]} №{self.number}")
        self.context_text.adjustSize()

    def add_data(self):
        new_info = list()
        Data(self.data).add(self.data, new_info)
        self.choice()
        self.context_text.setText(f"Добавлено {self.data[0][0]} №{self.number}")
        self.context_text.adjustSize()

    def choice(self):
        # Textbox1
        self.text_box1.move(1000, 1000)
        # MainText
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Выберите: ")
        self.main_text.move(50, 10)
        self.main_text.adjustSize()
        # Text
        self.text = QtWidgets.QLabel(self)
        self.text.setText("")
        self.text.move(200, 10)
        self.text.adjustSize()
        # Button1
        self.button1.move(25, 25)
        self.button1.setText("Список")
        self.button1.clicked.connect(self.enum)
        # Button2
        self.button2.move(25, 50)
        self.button2.setText("Добавление")
        self.button2.clicked.connect(self.add)
        # Button3
        self.button3.move(25, 75)
        self.button3.setText("Изменение")
        self.button3.clicked.connect(self.change)
        # Button4
        self.button4.move(25, 100)
        self.button4.setText("Удаление")
        self.button4.clicked.connect(self.delete)
        # Button5
        self.button5.move(25, 125)
        self.button5.setText("Выход")
        self.button5.clicked.connect(self.exit)
        # ContextText
        self.context_text.setText("")

    def enum(self):
        # Textbox1
        self.text_box1.hide()
        self.text.setText(Data(self.data).enum())
        self.text.adjustSize()
        # ContextText
        self.context_text.setText("")
        # ContextButton
        self.context_button.hide()

    def add(self):
        # Textbox1
        self.text_box1.move(1000, 1000)
        self.text.setText("Добавление: ")
        self.text.adjustSize()
        # TextBox1
        self.text_box1.move(200, 75)
        self.text_box1.setFixedWidth(100)
        self.text_box1.setPlainText("1")
        # ContextText
        self.context_text.setText("Поле:")
        # TextBox1
        self.text_box1.show()
        # ContextButton
        self.context_button.show()

    def change(self):
        # Textbox1
        self.text_box1.move(1000, 1000)
        self.text.setText("Изменение: ")
        self.text.adjustSize()
        # TextBox1
        self.text_box1.move(200, 75)
        self.text_box1.setFixedWidth(100)
        self.text_box1.setPlainText("1")
        # ContextText
        self.context_text.setText(f"{self.data[0][0]} №")
        # TextBox1
        self.text_box1.show()
        # ContextButton
        self.context_button.show()

    def delete(self):
        # Text
        self.text.setText("Удаление: ")
        self.text.adjustSize()
        # TextBox1
        self.text_box1.move(200, 75)
        self.text_box1.setFixedWidth(100)
        self.text_box1.setPlainText("1")
        # ContextText
        self.context_text.setText(f"{self.data[0][0]} №")
        # TextBox1
        self.text_box1.show()
        #
        self.number = int(self.text_box1.toPlainText())
        # ContextButton
        self.context_button.show()
        self.context_button.clicked.connect(self.delete_data)

    def exit(self):
        # Textbox1
        self.text_box1.move(1000, 1000)
        self.text.setText("Выход: ")
        self.text.adjustSize()
        # Context_Button
        self.context_button.hide()
        # Context_Text
        self.context_text.setText("")
        # Data Export
        write(self.filename, self.data)
        # Window Close
        self.closeEvent()

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
