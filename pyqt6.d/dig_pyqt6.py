#!/usr/bin/env python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.setGeometry(100, 100, 300, 200)

        label = QLabel("Hello, World!", self)
        label.move(50, 50)

    def show(self):
        super().show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWorld()
    window.show()
    sys.exit(app.exec())
