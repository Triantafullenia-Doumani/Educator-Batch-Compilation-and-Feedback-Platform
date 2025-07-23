from pathlib import Path
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

class BatchService:
    service_name = "compiler"
    result_subdir = "compiler_results"

    def __init__(
        self,
        submissions_dir: str,
        exts: list[str],
        timeout: int = 30,
        workers: int = 1
    ):
        self.root = Path(submissions_dir)
        self.exts = exts
        self.timeout = timeout
        self.workers = workers

        # prepare results folder
        self.results_dir = self.root / "results" / self.result_subdir
        self.results_dir.mkdir(parents=True, exist_ok=True)

    def run_all(self) -> dict[str, str]:
        """
        Parallel over each student folder (skipping 'results'),
        writes one report per student, and returns student -> report_path.
        """
        summary: dict[str, str] = {}
        students = [
            d for d in self.root.iterdir()
            if d.is_dir() and d.name != "results" and not d.name.startswith(".")
        ]

        with ThreadPoolExecutor(max_workers=self.workers) as exe:
            futures = {exe.submit(self.run_folder, stu): stu for stu in students}
            for fut in as_completed(futures):
                stu = futures[fut]
                name = stu.name
                try:
                    report = fut.result()
                    path = self.write_report(stu, report)
                    summary[name] = path
                except Exception as e:
                    summary[name] = f"ERROR: {e}"
        return summary

    def run_folder(self, student_folder: Path) -> list[dict]:
        """
        Process a single student's folder:
          - find exactly one .py compiler script
          - gather all other source files matching self.exts
          - clean out old .asm/.int artifacts
          - run each source through run_file()
        """
        py_files = list(student_folder.glob("*.py"))
        if len(py_files) != 1:
            return [{"error": f"expected one .py, found {len(py_files)}"}]
        compiler = py_files[0].name

        sources = [
            f for ext in self.exts
            for f in student_folder.glob(f"*{ext}")
            if f.name != compiler
        ]
        if not sources:
            return [{"error": "no source files"}]

        # clean old artifacts
        for pat in ("*.asm", "*.int"):
            for old in student_folder.glob(pat):
                old.unlink(missing_ok=True)

        results: list[dict] = []
        for src in sources:
            results.append(self.run_file(student_folder, src, compiler))
        return results
    
    def run_file(self, student_folder: Path, src: Path, compiler: str) -> dict:
        try:
            p = subprocess.run(
                ["python3", compiler, src.name],
                cwd=student_folder,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            rc, out, err = p.returncode, p.stdout, p.stderr
        except subprocess.TimeoutExpired as e:
            rc = 1
            out = e.stdout or ""
            err = e.stderr or ""

        expected_outputs = [
            f"assembly-for-({src.name}).asm",
            f"intermediate-for-({src.name}).int"
        ]

        outputs = [
            f.name for f in student_folder.iterdir()
            if f.name in expected_outputs
        ]

        return {
            "file": src.name,
            "returncode": rc,
            "stdout": out.strip(),
            "stderr": err.strip(),
            "outputs": outputs
        }



    def write_report(self, student_folder: Path, report: list[dict]) -> str:
        """
        Dump one JSON per student under results/compiler_results/
        """
        out_dir = student_folder.parent / "results" / self.result_subdir
        out_file = out_dir / f"{self.service_name}_output_{student_folder.name}.json"
        out_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
        return str(out_file)