import subprocess
from pathlib import Path

class CompileService:
    def compile(self, folder: Path, exts: list[str]) -> dict:
        """
        Locate all source files matching exts under `folder`,
        invoke folder/compiler.py on them, and return a dict
        with stdout, stderr, and return code.
        """
        compiler = folder / "compiler.py"
        sources = []
        for ext in exts:
            sources += list(folder.glob(f"*{ext}"))
        args = ["python3", str(compiler)] + [str(s) for s in sources]
        proc = subprocess.run(args, capture_output=True, text=True)
        return {
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "rc": proc.returncode
        }
