from src.services.batch_service import BatchService

class BatchController:
    def __init__(self, submissions_dir: str, exts: list[str], workers: int):
        self.service = BatchService(submissions_dir, exts, workers)

    def run(self):
        return self.service.execute_all()