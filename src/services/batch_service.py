
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
import subprocess

class BatchService:
    def __init__(self, submissions_dir: str, exts: list[str], workers: int = 4):
        self.root = Path(submissions_dir)
        self.exts = exts
        self.workers = workers

    def _process_one(self, folder_path: str) -> dict:
        folder = Path(folder_path)
        # Find the single Python compiler script
        py_files = list(folder.glob("*.py"))
        if not py_files:
            return {"student": folder.name, "error": "No Python compiler file found"}
        if len(py_files) > 1:
            return {"student": folder.name, "error": "Multiple Python files found"}
        compiler = py_files[0]

        # Prepare results directory
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        output_file = results_dir / f"compiler_output_{folder.name}.txt"

        # Run compiler on each source file and log output
        with output_file.open("w", encoding="utf-8") as out_f:
            for ext in self.exts:
                for source in folder.glob(f"*{ext}"):
                    cmd = ["python3", str(compiler), str(source)]
                    proc = subprocess.run(cmd, capture_output=True, text=True)
                    out_f.write(f"== {source.name} ==\n")
                    out_f.write(f"Return code: {proc.returncode}\n")
                    out_f.write("Stdout:\n")
                    out_f.write(proc.stdout if proc.stdout else "<empty>\n")
                    out_f.write("Stderr:\n")
                    out_f.write(proc.stderr if proc.stderr else "<empty>\n")
                    out_f.write("\n")

        return {"student": folder.name, "output_file": str(output_file)}

    def execute_all(self) -> list[dict]:
        folders = [str(p) for p in self.root.iterdir() if p.is_dir()]
        results = []
        with ProcessPoolExecutor(max_workers=self.workers) as exe:
            futures = {exe.submit(self._process_one, f): f for f in folders}
            for future in as_completed(futures):
                results.append(future.result())
        return results