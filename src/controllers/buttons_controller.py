# src/controllers/buttons_controller.py
from PyQt6.QtCore import QObject
from src.controllers.batch_controller import BatchController
from src.controllers.batch_worker import BatchWorker

class ButtonsController(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.view = main_window.buttons_view
        self.view.run_requested.connect(self.handle_run)
        self.worker = None  # Keep a reference

    def handle_run(self, submissions_dir, exts, workers):
        print("handle_run called (threaded)")
        # Start batch in a worker thread
        self.worker = BatchWorker(submissions_dir, exts, workers)
        self.worker.result_ready.connect(self.view.show_results)
        self.worker.start()