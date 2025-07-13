import sys
from PyQt6.QtWidgets import QApplication
from src.views.main_window import MainWindow
from src.controllers.buttons_controller import ButtonsController
from src.services.plagiarism_service import PlagiarismService
from src.controllers.plagiarism_controller import PlagiarismController
import os

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
    window.controller = controller 
    
    moss_path = os.path.abspath("scripts/moss")
    plag_service = PlagiarismService(moss_path)
    plag_controller = PlagiarismController(plag_service)
    window.buttons_view.set_plagiarism_controller(plag_controller)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
