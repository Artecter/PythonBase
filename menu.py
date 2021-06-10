from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Python Base")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)
        self.new_text.setText("Работает!")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Работает!")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажать!")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect()

    def add_text(self, text):
        self.new_text.setText(text)


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()