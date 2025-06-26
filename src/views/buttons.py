from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QSpinBox, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import pyqtSignal

class ButtonsView(QWidget):
    # Signal: submissions_dir, exts, workers
    run_requested = pyqtSignal(str, list, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        # Folder selector
        self.folder_label = QLabel("Submissions Folder:")
        self.folder_input = QLineEdit()
        self.browse_btn = QPushButton("Browse...")
        self.browse_btn.clicked.connect(self._on_browse)
        folder_layout = QHBoxLayout()
        folder_layout.addWidget(self.folder_label)
        folder_layout.addWidget(self.folder_input)
        folder_layout.addWidget(self.browse_btn)

        # Extensions input
        self.ext_label = QLabel("Extensions:")
        self.ext_input = QLineEdit()
        ext_layout = QHBoxLayout()
        ext_layout.addWidget(self.ext_label)
        ext_layout.addWidget(self.ext_input)

        # Workers spinner
        self.workers_label = QLabel("Workers:")
        self.workers_input = QSpinBox()
        self.workers_input.setMinimum(1)
        self.workers_input.setValue(4)
        workers_layout = QHBoxLayout()
        workers_layout.addWidget(self.workers_label)
        workers_layout.addWidget(self.workers_input)

        # Run button
        self.run_btn = QPushButton("Run Batch")
        self.run_btn.clicked.connect(self._on_run)

        # Results display
        self.results_view = QTextEdit()
        self.results_view.setReadOnly(True)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(folder_layout)
        main_layout.addLayout(ext_layout)
        main_layout.addLayout(workers_layout)
        main_layout.addWidget(self.run_btn)
        main_layout.addWidget(self.results_view)
        self.setLayout(main_layout)

    def _on_browse(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select Submissions Folder")
        if dir_path:
            self.folder_input.setText(dir_path)

    def _on_run(self):
        dir_path = self.folder_input.text().strip()
        if not dir_path:
            return
        exts = self.ext_input.text().split()
        workers = self.workers_input.value()
        self.run_btn.setEnabled(False)
        self.results_view.clear()
        self.run_requested.emit(dir_path, exts, workers)

    def show_results(self, results: list[dict]):
        import json
        self.results_view.setPlainText(json.dumps(results, indent=2))