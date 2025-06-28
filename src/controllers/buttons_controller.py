from PyQt6.QtCore import QObject
from src.controllers.batch_worker import BatchWorker
from src.services.batch_stats_service import BatchStatsService
from pathlib import Path

class ButtonsController(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.view = main_window.buttons_view
        self.view.run_requested.connect(self.handle_run)
        self.worker = None

    def handle_run(self, submissions_dir, exts, workers):
        print("handle_run called")
        self.view.show_wait_dialog()        
        self.worker = BatchWorker(submissions_dir, exts, workers)
        self.worker.result_ready.connect(self._handle_batch_done)
        self.worker.start()


    def _handle_batch_done(self, results):
        self.view.close_wait_dialog()
        print("_handle_batch_done CALLED with:", type(results), results)
        self.view.show_results(results)
        results_folder = Path(self.view.folder_input.text()) / "results"
        print("Looking for stats in:", results_folder)
        try:
            files_found = list(results_folder.glob("compiler_output_*.json"))
            print("Files found:", files_found)
        except Exception as e:
            print("Error listing files:", e)
        stats_service = BatchStatsService(results_folder)
        stats = stats_service.gather_stats()
        print("Stats generated:", stats)
        self.view.show_stats_table(stats)

