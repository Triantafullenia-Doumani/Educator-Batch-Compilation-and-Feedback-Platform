from pathlib import Path
from src.services.asm_service import AsmService

class AsmController:
    """
    Handles the execution and reporting of .asm files for each student.
    This is logic-only and used by AsmWorker.
    """

    def __init__(self, submissions_dir: str, jar_path: str, timeout, workers):
        self.submissions_dir = Path(submissions_dir)
        self.jar_path = jar_path
        self.timeout = timeout
        self.workers = workers

    def run(self) -> dict:
        print("[AsmController] run() called")
        svc = AsmService(runner_jar=self.jar_path, timeout=self.timeout)
        summary = svc.run_all(self.submissions_dir, workers=self.workers)
        print("[AsmController] summary returned:", summary)
        return summary
