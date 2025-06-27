import sys
from PyQt6.QtWidgets import QApplication
from src.views.main_window import MainWindow
from src.controllers.buttons_controller import ButtonsController

def main():
    print("main() started")
    app = QApplication(sys.argv)
    # try to load your QSS but ignore errors
    try:
        with open("styles/style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass
    window = MainWindow()
    controller = ButtonsController(window)
    window.controller = controller  # attach to window, for lifetime
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
