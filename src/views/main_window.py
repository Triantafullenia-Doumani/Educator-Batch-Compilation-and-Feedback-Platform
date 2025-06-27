# src/views/main_window.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from src.views.buttons import ButtonsView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Professor Batch Grader")
        self.resize(800, 600)

        container = QWidget()
        layout = QVBoxLayout(container)

        self.buttons_view = ButtonsView()
        layout.addWidget(self.buttons_view)

        self.setCentralWidget(container)
