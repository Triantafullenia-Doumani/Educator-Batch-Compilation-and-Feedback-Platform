# src/controllers/buttons_controller.py
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QMessageBox
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

        # 1) Clear any old stats immediately
        self.view.clear_stats_table()

        # 2) Pre-validate that at least one source file matches in the tree
        root = Path(submissions_dir)
        found = False
        for student in root.iterdir():
            if not student.is_dir():
                continue
            for ext in exts:
                if list(student.glob(f"*{ext}")):
                    found = True
                    break
            if found:
                break

        if not found:
            # Show error, re-enable Run button, and leave stats table empty
            QMessageBox.warning(
                self.view,
                "No sources found",
                f"No files with extension(s) {', '.join(exts)} were found."
            )
            self.view.run_btn.setEnabled(True)
            return

        # 3) If valid, proceed
        self.view.show_wait_dialog()
        self.worker = BatchWorker(submissions_dir, exts, workers)
        self.worker.result_ready.connect(self._handle_batch_done)
        self.worker.start()

    def _handle_batch_done(self, results):
        self.view.close_wait_dialog()
        print("_handle_batch_done CALLED with:", type(results), results)
        self.view.show_results(results)

        # Build stats
        results_folder = Path(self.view.folder_input.text()) / "results"
        stats_service = BatchStatsService(results_folder)
        stats = stats_service.gather_stats()
        print("Stats generated:", stats)

        # Populate table
        self.view.show_stats_table(stats)
