from pathlib import Path
from src.services.int_service import IntService

class IntController:
    """
    Handles the execution and reporting of .int files for each student.
    This class contains only logic and is used by IntWorker.
    """

    def __init__(self, submissions_dir: str, timeout, workers):
        self.submissions_dir = Path(submissions_dir)
        self.timeout = timeout
        self.workers = workers

    def run(self) -> dict:
        svc = IntService(timeout=self.timeout)
        summary = svc.run_all(self.submissions_dir, workers=self.workers)
        return summary
