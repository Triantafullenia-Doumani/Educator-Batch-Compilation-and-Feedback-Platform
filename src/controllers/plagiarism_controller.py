from PyQt6.QtCore import QObject, pyqtSignal

class PlagiarismController(QObject):
    plagiarism_checked = pyqtSignal(dict)

    def __init__(self, service):
        super().__init__()
        self.service = service

    def check(self, submissions_dir):
        from threading import Thread
        def run():
            result = self.service.run_moss(submissions_dir)
            self.plagiarism_checked.emit(result)
        Thread(target=run, daemon=True).start()
