# src/services/batch_service.py
import logging
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
import subprocess

# configure root logger
logging.basicConfig(level=logging.DEBUG, 
                    format="%(asctime)s %(levelname)s %(message)s")

class BatchService:
    def __init__(self, submissions_dir: str, exts: list[str], workers: int = 4):
        self.root = Path(submissions_dir)
        self.exts = exts
        self.workers = workers
        self.results_dir = self.root / "results"
        logging.debug(f"Initializing BatchService: root={self.root}, exts={self.exts}, workers={self.workers}")
        try:
            self.results_dir.mkdir(exist_ok=True, parents=True)
            logging.debug(f"Ensured results dir exists at {self.results_dir}")
        except Exception:
            logging.exception("Failed to create results directory")

    def _run_one(self, folder_path: str) -> dict:
        print(f"_run_one called for folder: {folder_path}")
        folder = Path(folder_path)
        student = folder.name
        logging.debug(f"Processing student folder: {folder}")

        try:
            # find exactly one .py driver
            pys = [p for p in folder.glob("*.py") if p.is_file()]
            if len(pys) != 1:
                msg = f"expected exactly one .py file, found {len(pys)}"
                logging.warning(f"{student}: {msg}")
                return {"student": student, "error": msg}
            compiler = pys[0]
            logging.debug(f"{student}: using compiler {compiler.name}")

            # gather sources (excluding the compiler itself)
            sources = []
            for ext in self.exts:
                for src in folder.glob(f"*{ext}"):
                    if src != compiler:
                        sources.append(src)
            logging.debug(f"{student}: found sources {', '.join(s.name for s in sources)}")
            if not sources:
                msg = "no sources found"
                logging.warning(f"{student}: {msg}")
                return {"student": student, "error": msg}

            # invoke the compiler script on each source
            log = ""
            for src in sources:
                logging.debug(f"{student}: running {compiler.name} on {src.name}")
                proc = subprocess.run(
                    ["python3", str(compiler), str(src)],
                    capture_output=True, text=True
                )
                log += f"--- {src.name} (rc={proc.returncode}) ---\n"
                log += proc.stdout + proc.stderr + "\n"

            # write output file
            out_file = self.results_dir / f"compiler_output_{student}.txt"
            out_file.write_text(log, encoding="utf-8")
            logging.info(f"{student}: wrote results to {out_file}")
            return {"student": student, "output_file": str(out_file)}

        except Exception as e:
            logging.exception(f"{student}: unexpected error")
            return {"student": student, "error": str(e)}

    def execute_all(self) -> dict:
        print("execute_all called")
        logging.debug("Starting execute_all()")
        folders = [p for p in self.root.iterdir() if p.is_dir()]
        logging.debug(f"Student folders: {[p.name for p in folders]}")
        summary: dict[str, str] = {}

        with ProcessPoolExecutor(max_workers=self.workers) as executor:
            future_to_student = {
                executor.submit(self._run_one, str(folder)): folder.name
                for folder in folders
            }
            for fut in as_completed(future_to_student):
                result = fut.result()
                student = result["student"]
                if "output_file" in result:
                    summary[student] = result["output_file"]
                else:
                    summary[student] = f"ERROR: {result.get('error')}"
                logging.debug(f"{student}: summary entry {summary[student]}")

        logging.info("Finished all students")
        return summary
