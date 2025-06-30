# src/services/batch_service.py
from pathlib import Path
import subprocess
import json

class BatchService:
    def __init__(self, submissions_dir: str, exts: list[str], timeout: int = 30):
        self.root = Path(submissions_dir)
        self.exts = exts
        self.timeout = timeout
        self.results_dir = self.root / "results"
        self.results_dir.mkdir(parents=True, exist_ok=True)

    def _run_one(self, folder: Path) -> dict:
        # locate compiler script
        py_files = list(folder.glob("*.py"))
        if len(py_files) != 1:
            return {"student": folder.name, "error": f"expected one .py, found {len(py_files)}"}
        compiler = py_files[0].name

        # find source files
        sources = [f for ext in self.exts for f in folder.glob(f"*{ext}") if f.name != compiler]
        if not sources:
            return {"student": folder.name, "error": "no sources"}

        results = []
        # clean old artifacts
        for pat in ("*.asm", "*.int"):
            for old in folder.glob(pat):
                old.unlink(missing_ok=True)

        for src in sources:
            try:
                p = subprocess.run(
                    ["python3", compiler, src.name],
                    cwd=folder,
                    capture_output=True,
                    text=True,
                    timeout=self.timeout
                )
                rc, out, err = p.returncode, p.stdout, p.stderr
            except subprocess.TimeoutExpired as e:
                rc, out, err = -1, e.stdout or "", (e.stderr or "") + "\nTIMEOUT"

            outputs = [f.name for pat in ("*.asm", "*.int") for f in folder.glob(pat)]
            results.append({
                "source": src.name,
                "returncode": rc,
                "stdout": out,
                "stderr": err,
                "outputs": outputs,
            })

        out_file = self.results_dir / f"compiler_output_{folder.name}.json"
        out_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
        return {"student": folder.name, "output_file": str(out_file)}

    def execute_all(self) -> dict[str, str]:
        summary = {}
        for folder in self.root.iterdir():
            if not folder.is_dir() or folder.name == self.results_dir.name:
                continue
            res = self._run_one(folder)
            student = res["student"]
            summary[student] = res.get("output_file", f"ERROR: {res.get('error')}")
        return summary
