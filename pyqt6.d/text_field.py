#!/usr/bin/env python
#@file: text_field.py
import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

text_field = QLineEdit()
layout.addWidget(text_field)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
