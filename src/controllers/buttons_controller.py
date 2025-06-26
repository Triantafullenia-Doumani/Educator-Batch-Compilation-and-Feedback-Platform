from PyQt6.QtCore import QObject
from src.controllers.batch_worker import BatchWorker

class ButtonsController(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.view = main_window.buttons_view
        self._worker = None
        self.view.run_requested.connect(self.start_batch)

    def start_batch(self, submissions_dir: str, exts: list[str], workers: int):
        self.view.run_btn.setEnabled(False)
        self.view.results_view.clear()

        self._worker = BatchWorker(submissions_dir, exts, workers)
        self._worker.result_ready.connect(self.on_results)
        self._worker.finished.connect(self.on_finished)
        self._worker.start()

    def on_results(self, results: list[dict]):
        self.view.show_results(results)

    def on_finished(self):
        self.view.run_btn.setEnabled(True)
        self._worker = None
