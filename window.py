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
        # TextBox
        self.text_box = QtWidgets.QPlainTextEdit(self)
        self.text_box.move(10, 75)
        self.main_text.setFixedWidth(100)
        # Button
        self.button = QtWidgets.QPushButton(self)
        self.button.move(10, 40)
        self.button.setText("Нажать!")
        self.button.clicked.connect(self.add_label)

    def add_label(self):
        self.text_box.setPlainText("Бр!")
        text = "Бр"
        self.main_text.setText(text)
        self.main_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


def main():
    if __name__ == "__main__":
        application()


main()

