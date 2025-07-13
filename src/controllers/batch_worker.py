# src/controllers/batch_worker.py
from PyQt6.QtCore import QThread, pyqtSignal
from src.controllers.batch_controller import BatchController

class BatchWorker(QThread):
    result_ready = pyqtSignal(object)  

    def __init__(self, submissions_dir: str, exts: list[str], workers: int):
        super().__init__()
        self.submissions_dir = submissions_dir
        self.exts = exts
        self.workers = workers

    def run(self):
        print("BatchWorker running in thread:", self.currentThreadId())
        try:
            controller = BatchController(self.submissions_dir, self.exts, self.workers)
            results = controller.run()
            self.result_ready.emit(results)
        except Exception as e:
            print("EXCEPTION IN BatchWorker.run:", e)
