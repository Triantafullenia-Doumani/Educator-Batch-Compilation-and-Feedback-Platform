# src/controllers/batch_controller.py
from src.services.batch_service import BatchService

class BatchController:
    def __init__(self, submissions_dir: str, exts: list[str], workers):
        self.service = BatchService(submissions_dir, exts, workers)

    def run(self):
        return self.service.run_all()


