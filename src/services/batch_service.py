# src/services/batch_service.py
import logging
from pathlib import Path
import subprocess
import json

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

    def _run_one(self, folder_path: str):
        try:
            folder = Path(folder_path)
            pys = [p for p in folder.glob("*.py") if p.is_file()]
            if len(pys) != 1:
                return {"student": folder.name, "error": f"expected exactly one .py file, found {len(pys)}"}
            compiler = pys[0]

            sources = []
            for ext in self.exts:
                sources += [s for s in folder.glob(f"*{ext}") if s != compiler]
            if not sources:
                return {"student": folder.name, "error": "no sources"}

            results = []
            for src in sources:
                try:
                    p = subprocess.run(
                        ["python3", str(compiler), str(src)],
                        capture_output=True, text=True, timeout=10  # 10 seconds max
                    )
                    results.append({
                        "source": src.name,
                        "returncode": p.returncode,
                        "stdout": p.stdout,
                        "stderr": p.stderr,
                    })
                except subprocess.TimeoutExpired:
                    results.append({
                        "source": src.name,
                        "returncode": -1,
                        "stdout": "",
                        "stderr": "TIMEOUT"
                    })
                except Exception as e:
                    results.append({
                        "source": src.name,
                        "returncode": -2,
                        "stdout": "",
                        "stderr": f"EXCEPTION: {e}"
                    })


            out_file = self.results_dir / f"compiler_output_{folder.name}.json"
            out_file.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
            return {"student": folder.name, "output_file": str(out_file)}
        except Exception as e:
            print(f"EXCEPTION in _run_one for {folder_path}: {e}")
            return {"student": Path(folder_path).name, "error": f"EXCEPTION: {e}"}

    def execute_all(self) -> dict:
        print("execute_all called")
        logging.debug("Starting execute_all()")
        folders = [
            p for p in self.root.iterdir()
            if p.is_dir() and p.name != "results"
        ]
        logging.debug(f"Student folders: {[p.name for p in folders]}")
        summary: dict[str, str] = {}

        for folder in folders:
            result = self._run_one(str(folder))
            student = result["student"]
            if "output_file" in result:
                summary[student] = result["output_file"]
            else:
                summary[student] = f"ERROR: {result.get('error')}"
            logging.debug(f"{student}: summary entry {summary[student]}")

        logging.info("Finished all students")
        return summary
