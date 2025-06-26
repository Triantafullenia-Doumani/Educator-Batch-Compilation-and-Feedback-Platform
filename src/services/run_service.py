import subprocess
from pathlib import Path

class RunService:
    def run_executable(self, folder: Path, exe_name: str = "a.out") -> dict:
        exe = folder / exe_name
        if not exe.exists():
            return {"error": f"{exe_name} not found"}
        proc = subprocess.run([str(exe)], capture_output=True, text=True)
        return {
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "rc": proc.returncode
        }
