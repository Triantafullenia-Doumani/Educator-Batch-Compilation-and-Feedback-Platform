from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QMessageBox
from pathlib import Path
from src.controllers.batch_worker import BatchWorker
from src.services.batch_stats_service import BatchStatsService
from src.services.asm_stats_service import AsmStatsService  
from src.services.int_stats_service import IntStatsService
from src.controllers.asm_worker import AsmWorker
from src.controllers.int_worker import IntWorker
from src.views.show_stats import StatsTableAdapter 
from src.services.int_service import IntService    
from src.services.stats_saver import StatsSaver


class ButtonsController(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.view = main_window.buttons_view

        # Connect all signals (now expects 'workers' for asm & int)
        self.view.run_requested.connect(self.handle_run)
        self.view.run_asm_requested.connect(self.handle_run_asm)
        self.view.run_int_requested.connect(self.handle_run_int)

        self.batch_worker = None
        self.asm_worker   = None
        self.int_worker   = None

    def handle_run(self, submissions_dir, exts, workers):
        self.view.clear_stats_table()
        self.view.show_wait_dialog()
        self.view.run_btn.setEnabled(False)
        self.view.run_asm_btn.setEnabled(False)
        self.view.run_int_btn.setEnabled(False)

        root = Path(submissions_dir)
        if not any(root.glob(f"*/*{ext}") for ext in exts):
            QMessageBox.warning(
                self.view,
                "No sources found",
                f"No files with extension(s) {', '.join(exts)} were found."
            )
            self.view.close_wait_dialog()
            self.view.run_btn.setEnabled(True)
            self.view.run_asm_btn.setEnabled(True)
            self.view.run_int_btn.setEnabled(True)
            return

        self.batch_worker = BatchWorker(submissions_dir, exts, workers)
        self.batch_worker.result_ready.connect(self._handle_batch_done)
        self.batch_worker.start()

    def _handle_batch_done(self, results):
        self.view.close_wait_dialog()
        self.view.show_results(results)
        self.view.run_btn.setEnabled(True)
        self.view.run_asm_btn.setEnabled(True)
        self.view.run_int_btn.setEnabled(True)

        # Show and save compiler stats
        submissions_dir = Path(self.view.folder_input.text())
        results_folder = submissions_dir / "results/compiler_results"
        stats = BatchStatsService(results_folder).gather_stats()
        self.view.show_stats_table(stats, result_type="compiler")

        # --- Save compiler stats ---
        StatsSaver.save(
            stats,
            submissions_dir / "results" / "statistics" / "compiler_stats.json"
        )


    def handle_run_asm(self, submissions_dir, workers):
        self.view.clear_stats_table()
        self.view.results_view.clear()
        self.view.show_wait_dialog()
        self.view.run_btn.setEnabled(False)
        self.view.run_asm_btn.setEnabled(False)
        self.view.run_int_btn.setEnabled(False)

        project_root = Path(__file__).parents[2]
        jar_path = str(project_root / "lib" / "rars_46ab74d.jar")

        self.asm_worker = AsmWorker(submissions_dir, jar_path, timeout = 5, workers = workers)  
        self.asm_worker.result_ready.connect(self._on_asm_done)
        self.asm_worker.start()

    def _on_asm_done(self, summary: dict):
        self.view.close_wait_dialog()
        self.view.show_results(summary)
        self.view.run_btn.setEnabled(True)
        self.view.run_asm_btn.setEnabled(True)
        self.view.run_int_btn.setEnabled(True)

        # Show and save assembly stats
        submissions_dir = Path(self.view.folder_input.text())
        assembly_results_folder = submissions_dir / "results/assembly_results"
        stats = AsmStatsService(assembly_results_folder).gather_stats()
        self.view.show_stats_table(stats, result_type="assembly")

        # --- Save assembly stats ---
        StatsSaver.save(
            stats,
            submissions_dir / "results" / "statistics" / "assembly_stats.json"
        )


    # --- UPDATED: now expects workers param from signal ---
    def handle_run_int(self, submissions_dir, workers):
        print("handle_run_int CALLED")
        self.view.clear_stats_table()
        self.view.results_view.clear()
        self.view.show_wait_dialog()
        self.view.run_btn.setEnabled(False)
        self.view.run_asm_btn.setEnabled(False)
        self.view.run_int_btn.setEnabled(False)

        self.int_worker = IntWorker(submissions_dir, timeout = 5, workers = workers)
        self.int_worker.result_ready.connect(self._on_int_done)
        self.int_worker.start()

    def _on_int_done(self, summary):
        self.view.close_wait_dialog()
        self.view.show_results(summary)
        self.view.run_btn.setEnabled(True)
        self.view.run_asm_btn.setEnabled(True)
        self.view.run_int_btn.setEnabled(True)

        # Show and save int stats
        submissions_dir = Path(self.view.folder_input.text())
        int_results_folder = submissions_dir / "results/intermediate_results"
        stats = IntStatsService(int_results_folder).gather_stats()
        StatsTableAdapter.show_stats(self.view.stats_table, stats, result_type="intermediate")

        # --- Save int stats ---
        StatsSaver.save(
            stats,
            submissions_dir / "results" / "statistics" / "int_stats.json"
        )
