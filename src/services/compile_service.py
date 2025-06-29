import subprocess
from pathlib import Path

class CompileService:
    def compile(self, folder: Path, exts: list[str]) -> list[dict]:
        # 1) Find the student’s compiler script
        py_files = [f for f in folder.glob("*.py") if f.is_file()]
        if len(py_files) != 1:
            return [{"error": f"Expected exactly one .py file, found {len(py_files)}"}]
        compiler = py_files[0].name  # name only, since we'll cwd into folder

        # 2) Gather source files (all extensions except the compiler script)
        sources = [
            f for ext in exts
            for f in folder.glob(f"*{ext}")
            if f.name != compiler
        ]
        if not sources:
            return [{"error": "No source files found."}]

        results = []
        for src in sources:
            # 3) Clean out any old artifacts
            for pat in ("*.asm", "*.int"):
                for old in folder.glob(pat):
                    old.unlink(missing_ok=True)

            # 4) Invoke the compiler in its own folder
            print("HEHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH", folder)        
            proc = subprocess.run(
                ["python3", "compiler.py", src.name],
                cwd=str(folder),              # <-- must be the student’s directory
                capture_output=True,
                text=True
            )


            # 5) Collect the newly minted .asm/.int files
            outputs = [f.name for pat in ("*.asm", "*.int")
                       for f in folder.glob(pat)]

            results.append({
                "source": src.name,
                "returncode": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
                "outputs": outputs,
            })

        return results
