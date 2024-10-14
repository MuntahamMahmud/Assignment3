#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QWidget, QGridLayout
)
from PyQt6.QtCore import Qt

class BotControlApp(QWidget):
    def __init__(self):
        self.layoutH=QHBoxLayout()
        self.layoutV=QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.front_button=QPushButton("FRONT")
        self.grid_layout.addWidget(self.front_button,)
        self.front_button.clicked.connect(self.front,0,1)

        self.back_button=QPushButton("BACK")
        self.grid_layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.back,2,1)

        self.right_button=QPushButton("RIGHT")
        self.grid_layout.addWidget(self.right_button)
        self.right_button.clicked.connect(self.right,1,2)

        self.left_button=QPushButton("LEFT")
        self.grid_layout.addWidget(self.left_button)
        self.left_button.clicked.connect(self.left,1,0)
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BotControlApp()
    window.show()
    sys.exit(app.exec())