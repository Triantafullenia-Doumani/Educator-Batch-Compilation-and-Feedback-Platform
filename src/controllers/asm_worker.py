from PyQt6.QtCore import QThread, pyqtSignal
from src.controllers.asm_controller import AsmController

class AsmWorker(QThread):
    """
    Worker thread that runs AsmController logic and emits result_ready(summary_dict).
    """
    result_ready = pyqtSignal(dict)

    def __init__(self, submissions_dir: str, jar_path: str, timeout: int = 15, workers: int = 4):
        super().__init__()
        self.submissions_dir = submissions_dir
        self.jar_path = jar_path
        self.timeout = timeout
        self.workers = workers

    def run(self):
        print("AsmWorker running in thread:", self.currentThreadId())
        try:
            controller = AsmController(
                submissions_dir=self.submissions_dir,
                jar_path=self.jar_path,
                timeout=self.timeout,
                workers=self.workers
            )
            summary = controller.run()
            self.result_ready.emit(summary)
        except Exception as e:
            print("EXCEPTION IN AsmWorker.run:", e)
