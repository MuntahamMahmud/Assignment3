#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QWidget, QGridLayout
)
from PyQt6.QtCore import Qt

class BotController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bot Controller")
        self.setGeometry(100, 100, 400, 300)

        # Initialize Meulas
        self.meulas = 10

        # Create the main layout
        main_layout = QVBoxLayout()

        # Top section: Meulas and Increase button
        top_layout = QHBoxLayout()
        self.meulas_label = QLabel(f"Remaining Meulas: {self.meulas}")
        self.meulas_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.increase_button = QPushButton("Increase Meulas")
        self.increase_button.clicked.connect(self.increase_meulas)
        top_layout.addWidget(self.meulas_label)
        top_layout.addWidget(self.increase_button)
        main_layout.addLayout(top_layout)

        # Grid layout for movement buttons
        grid_layout = QGridLayout()

        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(lambda: self.move_bot("Forward"))

        self.left_button = QPushButton("Left")
        self.left_button.clicked.connect(lambda: self.move_bot("Left"))

        self.right_button = QPushButton("Right")
        self.right_button.clicked.connect(lambda: self.move_bot("Right"))

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(lambda: self.move_bot("Back"))

        # Add buttons to the grid layout
        grid_layout.addWidget(self.forward_button, 0, 1)
        grid_layout.addWidget(self.left_button, 1, 0)
        grid_layout.addWidget(self.right_button, 1, 2)
        grid_layout.addWidget(self.back_button, 2, 1)
        main_layout.addLayout(grid_layout)

        # Message label at the bottom
        self.message_label = QLabel("Message: ")
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.message_label)

        # Set the main widget and layout
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def move_bot(self, direction):
        """Handle bot movement and update Meulas."""
        if direction in ["Forward", "Back"]:
            if self.meulas >= 1:
                self.meulas -= 1
                self.update_meulas()
                self.message_label.setText(f"Bot is moving {direction}")
            else:
                self.message_label.setText("Not enough Meulas!")
        elif direction in ["Left", "Right"]:
            if self.meulas >= 2:
                self.meulas -= 2
                self.update_meulas()
                self.message_label.setText(f"Bot rotated to the {direction}")
            else:
                self.message_label.setText("Not enough Meulas!")

    def increase_meulas(self):
        """Increase Meulas by 1."""
        self.meulas += 1
        self.update_meulas()

    def update_meulas(self):
        """Update the Meulas label."""
        self.meulas_label.setText(f"Remaining Meulas: {self.meulas}")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BotController()
    window.show()
    sys.exit(app.exec())
