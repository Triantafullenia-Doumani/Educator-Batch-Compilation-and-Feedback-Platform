# src/views/buttons.py
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLineEdit, QLabel,
    QSpinBox, QFileDialog, QTextEdit,
    QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import pyqtSignal

class ButtonsView(QWidget):
    # emits (submissions_dir: str, exts: list[str], workers: int)
    run_requested = pyqtSignal(str, list, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        # Folder
        self.folder_input = QLineEdit()
        self.browse_btn = QPushButton("Browse...")
        self.browse_btn.clicked.connect(self._on_browse)
        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Folder:")); row1.addWidget(self.folder_input); row1.addWidget(self.browse_btn)

        # Extensions
        self.ext_input = QLineEdit()
        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Exts:")); row2.addWidget(self.ext_input)

        # Workers
        self.workers_input = QSpinBox()
        self.workers_input.setMinimum(1)
        self.workers_input.setValue(4)
        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Workers:")); row3.addWidget(self.workers_input)

        # Run + Results
        self.run_btn = QPushButton("Run Batch")
        self.run_btn.clicked.connect(self._on_run)
        self.results_view = QTextEdit()
        self.results_view.setReadOnly(True)

        # assemble
        v = QVBoxLayout(self)
        v.addLayout(row1)
        v.addLayout(row2)
        v.addLayout(row3)
        v.addWidget(self.run_btn)
        v.addWidget(self.results_view)

    def _on_browse(self):
        d = QFileDialog.getExistingDirectory(self, "Select Submissions Folder")
        if d:
            self.folder_input.setText(d)

    def _on_run(self):
        d = self.folder_input.text().strip()
        if not d:
            return
        exts = self.ext_input.text().split()
        workers = self.workers_input.value()
        self.run_btn.setEnabled(False)
        self.results_view.clear()
        self.run_requested.emit(d, exts, workers)

    def show_results(self, results):
        import json
        self.results_view.setPlainText(json.dumps(results, indent=2))
        self.run_btn.setEnabled(True)
