from PyQt6.QtCore import QThread, pyqtSignal
from src.controllers.int_controller import IntController

class IntWorker(QThread):
    """
    Worker thread that runs IntController logic and emits result_ready(summary_dict).
    """
    result_ready = pyqtSignal(dict)

    def __init__(self, submissions_dir: str, timeout, workers):
        super().__init__()
        self.submissions_dir = submissions_dir
        self.timeout = timeout
        self.workers = workers

    def run(self):
        try:
            controller = IntController(
                submissions_dir=self.submissions_dir,
                timeout=self.timeout,
                workers=self.workers
            )
            summary = controller.run()
            self.result_ready.emit(summary)
        except Exception as e:
            print("EXCEPTION IN IntWorker.run:", e)
