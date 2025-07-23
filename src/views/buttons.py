import os
import sys
import time 
import subprocess
import webbrowser
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLineEdit, QLabel,
    QSpinBox, QFileDialog, QTextEdit,
    QVBoxLayout, QHBoxLayout, QTableWidget, QProgressDialog, QMessageBox, 
)
from PyQt6.QtCore import pyqtSignal, Qt
from src.views.show_stats import StatsTableAdapter

class ButtonsView(QWidget):
    # emits (submissions_dir: str, exts: list[str], workers: int)
    run_requested = pyqtSignal(str, list, int)
    # emits (submissions_dir: str, int )
    run_asm_requested = pyqtSignal(str, int)
    # emits (submissions_dir: str)
    run_int_requested = pyqtSignal(str, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.submissions_dir = None

        # Widgets
        self.folder_input = QLineEdit()
        self.folder_input.setMaximumWidth(200)
        self.browse_btn = QPushButton("Browse...")
        self.browse_btn.clicked.connect(self._on_browse)

        self.ext_input = QLineEdit()
        self.ext_input.setMaximumWidth(200)

        self.workers_input = QSpinBox()
        self.workers_input.setMinimum(1)
        self.workers_input.setValue(1)

        self.run_btn = QPushButton("Run compilers")
        self.run_btn.clicked.connect(self._on_run)

        self.run_asm_btn = QPushButton("Run .asm")
        self.run_asm_btn.clicked.connect(self._on_run_asm)

        self.run_int_btn = QPushButton("Run .int")
        self.run_int_btn.clicked.connect(self._on_run_int)

        self.open_results_btn = QPushButton("Results")
        self.open_results_btn.clicked.connect(self.open_results_folder)

        self.results_view = QTextEdit()
        self.results_view.setReadOnly(True)

        self.stats_table = QTableWidget()
        self.stats_table.setColumnCount(3)
        self.stats_table.setHorizontalHeaderLabels([
            "User", "Total", "Successful"
        ])
        self.stats_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.check_plagiarism_btn = QPushButton("Check Plagiarism")
        self.check_plagiarism_btn.clicked.connect(self._on_check_plagiarism)

        self._run_start_time = None
        
        # Layout
        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Submission folder:"))
        row1.addWidget(self.folder_input)
        row1.addWidget(self.browse_btn)
        row1.addStretch()

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Source extension:"))
        row2.addWidget(self.ext_input)
        row2.addStretch()

        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Threads:"))
        row3.addWidget(self.workers_input)
        row3.addWidget(self.run_btn)
        row3.addWidget(self.run_asm_btn)
        row3.addWidget(self.run_int_btn)
        row3.addStretch()

        # Row 4: Results button (centered)
        row4 = QHBoxLayout()
        row4.addStretch()
        row4.addWidget(self.open_results_btn)
        row4.addStretch()

        # Bottom row: Check Plagiarism button (right-aligned)
        bottom_row = QHBoxLayout()
        bottom_row.addStretch()
        bottom_row.addWidget(self.check_plagiarism_btn)

        layout = QVBoxLayout(self)
        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)
        layout.addLayout(row4)
        layout.addWidget(self.results_view)
        layout.addWidget(self.stats_table)
        layout.addLayout(bottom_row)


    def _on_browse(self):
        d = QFileDialog.getExistingDirectory(self, "Select Submissions Folder")
        if d:
            self.submissions_dir = d
            self.folder_input.setText(d)

    def _on_run(self):
        self.clear_stats_table()
        d = self.folder_input.text().strip()
        if not d:
            return
        self.submissions_dir = d

        self.run_btn.setEnabled(False)
        self.run_asm_btn.setEnabled(False)
        self.run_int_btn.setEnabled(False)
        self.results_view.clear()

        exts = self.ext_input.text().split()
        workers = self.workers_input.value()
        self._run_start_time = time.time() 
        self.run_requested.emit(d, exts, workers)
    
    def _on_run_asm(self):
        if not self.submissions_dir:
            QMessageBox.warning(self, "Error", "Please select or run a batch first.")
            return

        self.clear_stats_table()
        self.results_view.clear()
        self.run_btn.setEnabled(False)
        self.run_asm_btn.setEnabled(False)
        self.run_int_btn.setEnabled(False)

        workers = self.workers_input.value()
        self._run_start_time = time.time()   
        self.run_asm_requested.emit(self.submissions_dir, workers)
    

    def _on_run_int(self):
        print("Run .int button clicked")
        if not self.submissions_dir:
            QMessageBox.warning(self, "Error", "Please select a folder first.")
            return
        self.clear_stats_table()
        self.results_view.clear()
        self.run_btn.setEnabled(False)
        self.run_asm_btn.setEnabled(False)
        self.run_int_btn.setEnabled(False)
        self._run_start_time = time.time()  # <-- Start timer here
        self.run_int_requested.emit(self.submissions_dir, self.workers_input.value())

    def show_results(self, results):
        import json
        elapsed = None
        if self._run_start_time is not None:
            elapsed = time.time() - self._run_start_time
            self._run_start_time = None
        msg = json.dumps(results, indent=2)
        if elapsed is not None:
            msg += f"\n\n Elapsed time: {elapsed:.2f} seconds"
        self.results_view.setPlainText(msg)

        self.run_btn.setEnabled(True)
        self.run_asm_btn.setEnabled(True)
        self.run_int_btn.setEnabled(True)

    def show_stats_table(self, stats, result_type="compiler"):
        """
        Show statistics in the table, using StatsTableAdapter.
        result_type: "compiler" for compile stats, "assembly" for asm run stats.
        """
        StatsTableAdapter.show_stats(self.stats_table, stats, result_type)

    def clear_stats_table(self):
        self.stats_table.clearContents()
        self.stats_table.setRowCount(0)

    def show_wait_dialog(self):
        self.wait_dialog = QProgressDialog(
            "Processing, please wait...", None, 0, 0, self
        )
        self.wait_dialog.setWindowTitle("Processing")
        self.wait_dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.wait_dialog.setMinimumDuration(0)
        self.wait_dialog.setCancelButton(None)
        self.wait_dialog.show()

    def close_wait_dialog(self):
        if hasattr(self, 'wait_dialog') and self.wait_dialog:
            self.wait_dialog.close()
            self.wait_dialog = None

    def open_results_folder(self):
        if not self.submissions_dir:
            QMessageBox.warning(self, "Error", "Please select or run a batch first.")
            return
        results_dir = os.path.join(self.submissions_dir, 'results')
        if not os.path.isdir(results_dir):
            QMessageBox.warning(self, "Error", "Results folder does not exist.")
            return
        try:
            if sys.platform.startswith('darwin'):
                subprocess.call(['open', results_dir])
            elif sys.platform.startswith('win'):
                os.startfile(results_dir)
            else:
                subprocess.call(['xdg-open', results_dir])
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not open folder: {e}")

    def set_plagiarism_controller(self, controller):
        self.plagiarism_controller = controller
        controller.plagiarism_checked.connect(self._on_plagiarism_result)

    def _on_check_plagiarism(self):
        if not self.submissions_dir:
            QMessageBox.warning(self, "Error", "Please select or run a batch first.")
            return
        self.check_plagiarism_btn.setEnabled(False)
        self.show_wait_dialog()
        self.results_view.clear()
        self.plagiarism_controller.check(self.submissions_dir)

    def _on_plagiarism_result(self, result):
        self.check_plagiarism_btn.setEnabled(True)
        self.close_wait_dialog()
        if "error" in result:
            self.results_view.setPlainText("Moss error:\n" + result["error"])
            return

        url = result.get("url", "")
        
        if url:
            reply = QMessageBox.information(
                self,
                "Plagiarism Report Ready",
                "The Moss report is ready!\n\nDo you want to open it in your browser?",
                QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Cancel
            )
            if reply == QMessageBox.StandardButton.Open:
                webbrowser.open(url)
