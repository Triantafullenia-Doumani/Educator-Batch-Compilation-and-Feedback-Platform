# src/views/buttons.py
import os
import sys
import subprocess
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLineEdit, QLabel,
    QSpinBox, QFileDialog, QTextEdit,
    QVBoxLayout, QHBoxLayout, QTableWidgetItem, QTableWidget, QProgressDialog, QMessageBox
)
from PyQt6.QtCore import pyqtSignal, Qt

class ButtonsView(QWidget):
    # emits (submissions_dir: str, exts: list[str], workers: int)
    run_requested = pyqtSignal(str, list, int)

    def __init__(self, parent=None):
        super().__init__(parent)

        # keep track of last selected folder
        self.submissions_dir = None

        # 1. Create widgets
        self.folder_input = QLineEdit()
        self.folder_input.setMaximumWidth(200)
        self.browse_btn = QPushButton("Browse...")
        self.browse_btn.clicked.connect(self._on_browse)

        self.ext_input = QLineEdit()
        self.ext_input.setMaximumWidth(200)

        self.workers_input = QSpinBox()
        self.workers_input.setMinimum(1)
        self.workers_input.setValue(4)

        self.run_btn = QPushButton("Run")
        self.run_btn.clicked.connect(self._on_run)

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

        # 2. Layout rows
        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Submission folder:"))
        row1.addWidget(self.folder_input)
        row1.addWidget(self.browse_btn)
        row1.addStretch()

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Source extension: "))
        row2.addWidget(self.ext_input)
        row2.addStretch()

        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Threads:"))
        row3.addWidget(self.workers_input)
        row3.addWidget(self.run_btn)
        row3.addWidget(self.open_results_btn)
        row3.addStretch()

        # 3. Main layout
        v = QVBoxLayout(self)
        v.addLayout(row1)
        v.addLayout(row2)
        v.addLayout(row3)
        v.addWidget(self.results_view)
        v.addWidget(self.stats_table)

    def _on_browse(self):
        d = QFileDialog.getExistingDirectory(self, "Select Submissions Folder")
        if d:
            self.submissions_dir = d
            self.folder_input.setText(d)

    def _on_run(self):
        # Clear previous stats immediately when Run is clicked
        self.clear_stats_table()

        d = self.folder_input.text().strip()
        if not d:
            return
        self.submissions_dir = d

        exts = self.ext_input.text().split()
        workers = self.workers_input.value()

        self.run_btn.setEnabled(False)
        self.results_view.clear()
        self.run_requested.emit(d, exts, workers)


    def show_results(self, results):
        import json
        self.results_view.setPlainText(json.dumps(results, indent=2))
        self.run_btn.setEnabled(True)

    def show_stats(self, text):
        self.results_view.append("\n=== Batch Statistics ===\n" + text)

    def show_stats_table(self, stats):
        self.stats_table.clearContents()
        self.stats_table.setRowCount(0)
        self.stats_table.setColumnCount(3)
        self.stats_table.setHorizontalHeaderLabels([
            "User", "Total", "Successful"
        ])
        for row, (user, data) in enumerate(stats.items()):
            self.stats_table.insertRow(row)
            self.stats_table.setItem(row, 0, QTableWidgetItem(user))
            self.stats_table.setItem(row, 1, QTableWidgetItem(str(data['total source files'])))
            self.stats_table.setItem(row, 2, QTableWidgetItem(f"{data['successful']}/{data['total source files']}"))
        self.stats_table.resizeColumnsToContents()

    def clear_stats_table(self):
        self.stats_table.clearContents()
        self.stats_table.setRowCount(0)
        
    def show_wait_dialog(self):
        self.wait_dialog = QProgressDialog(
            "Running all compilers, please wait...", None, 0, 0, self
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
            QMessageBox.warning(self, "Error", "Results folder does not exist in the selected directory.")
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