# src/views/buttons.py
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLineEdit, QLabel,
    QSpinBox, QFileDialog, QTextEdit,
    QVBoxLayout, QHBoxLayout, QTableWidgetItem, QTableWidget, QProgressDialog
)
from PyQt6.QtCore import pyqtSignal, Qt

class ButtonsView(QWidget):
    # emits (submissions_dir: str, exts: list[str], workers: int)
    run_requested = pyqtSignal(str, list, int)

    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Create widgets
        self.folder_input = QLineEdit()
        self.browse_btn = QPushButton("Browse...")
        self.browse_btn.clicked.connect(self._on_browse)

        self.ext_input = QLineEdit()

        self.workers_input = QSpinBox()
        self.workers_input.setMinimum(1)
        self.workers_input.setValue(4)

        self.run_btn = QPushButton("Run Batch")
        self.run_btn.clicked.connect(self._on_run)

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
        row1.addWidget(QLabel("Folder:"))
        row1.addWidget(self.folder_input)
        row1.addWidget(self.browse_btn)

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Exts:"))
        row2.addWidget(self.ext_input)

        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Workers:"))
        row3.addWidget(self.workers_input)

        # 3. Main layout
        v = QVBoxLayout(self)
        v.addLayout(row1)
        v.addLayout(row2)
        v.addLayout(row3)
        v.addWidget(self.run_btn)
        v.addWidget(self.results_view)
        v.addWidget(self.stats_table)

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

    def show_stats(self, text):
        # Option 1: append to results_view
        self.results_view.append("\n=== Batch Statistics ===\n" + text)
        # Option 2: put in a separate QTextEdit if you want, just add a stats_view = QTextEdit() in __init__
        
    def show_stats_table(self, stats):
        self.stats_table.clearContents()
        self.stats_table.setRowCount(0)
        self.stats_table.setColumnCount(3)  # Only 3 columns: User, Total, Successful/Total

        self.stats_table.setHorizontalHeaderLabels([
            "User", "Total", "Successful/Total"
        ])

        for row, (user, data) in enumerate(stats.items()):
            self.stats_table.insertRow(row)
            self.stats_table.setItem(row, 0, QTableWidgetItem(user))
            self.stats_table.setItem(row, 1, QTableWidgetItem(str(data['total source files'])))
            self.stats_table.setItem(row, 2, QTableWidgetItem(f"{data['successful']}/{data['total source files']}"))
        self.stats_table.resizeColumnsToContents()



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
