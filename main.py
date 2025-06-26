import sys
from PyQt6.QtWidgets import QApplication
from src.views.main_window import MainWindow
from src.controllers.buttons_controller import ButtonsController

def main():
    app = QApplication(sys.argv)
    # Load stylesheet
    try:
        with open("styles/style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: style.qss not found, running without stylesheet.")

    # Instantiate UI and controller
    window = MainWindow()
    ButtonsController(window)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()