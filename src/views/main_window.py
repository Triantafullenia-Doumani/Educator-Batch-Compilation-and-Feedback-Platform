from PyQt6.QtWidgets import QMainWindow
from src.views.buttons import ButtonsView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Professor Batch Grader")
        self.resize(800, 600)
        # UI component
        self.buttons_view = ButtonsView(self)
        self.setCentralWidget(self.buttons_view)

# src/views/buttons.py
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QSpinBox, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import pyqtSignal