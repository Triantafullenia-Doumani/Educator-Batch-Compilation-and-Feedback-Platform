from PyQt6.QtCore import QThread, pyqtSignal
from src.controllers.batch_controller import BatchController

class BatchWorker(QThread):
    result_ready = pyqtSignal(list)

    def __init__(self, submissions_dir: str, exts: list[str], workers: int):
        super().__init__()
        self.submissions_dir = submissions_dir
        self.exts = exts
        self.workers = workers

    def run(self):
        # Runs grading logic in a separate thread
        controller = BatchController(self.submissions_dir, self.exts, self.workers)
        results = controller.run()
        self.result_ready.emit(results)
