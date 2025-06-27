# src/services/compile_service.py
import subprocess
from pathlib import Path

class CompileService:
    def compile(self, folder: Path, exts: list[str]) -> dict:
        """
        Locate all source files matching exts under `folder`,
        invoke the only .py file on them, and return a dict
        with stdout, stderr, and return code.
        """
        py_files = [f for f in folder.glob("*.py") if f.is_file()]
        if len(py_files) != 1:
            return {
                "error": f"Expected exactly one .py file, found {len(py_files)}: {[f.name for f in py_files]}"
            }
        compiler = py_files[0]

        sources = []
        for ext in exts:
            sources += [f for f in folder.glob(f"*{ext}") if f != compiler]
        if not sources:
            return {"error": "No source files found."}

        args = ["python3", str(compiler)] + [str(s) for s in sources]
        proc = subprocess.run(args, capture_output=True, text=True)
        return {
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "rc": proc.returncode
        }
