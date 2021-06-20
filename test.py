from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Python Base")
        self.setGeometry(300, 250, 350, 200)
        # MainText
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Пусто")
        self.main_text.move(10, 10)
        self.main_text.adjustSize()
        # TextBox1
        self.text_box1 = QtWidgets.QTextEdit(self)
        self.text_box1.move(10, 75)
        self.text_box1.setFixedWidth(100)
        self.text_box1.setPlainText("1")
        # TextBox2
        self.text_box2 = QtWidgets.QTextEdit(self)
        self.text_box2.move(110, 75)
        self.text_box2.setFixedWidth(100)
        self.text_box2.setPlainText("2")
        # Button
        self.button = QtWidgets.QPushButton(self)
        self.button.move(10, 40)
        self.button.setText("Нажать!")
        self.button.clicked.connect(self.add_label)

    def add_label(self):
        self.main_text.setText(str(int(self.text_box1.toPlainText()) + int(self.text_box2.toPlainText())))
        self.main_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


application()