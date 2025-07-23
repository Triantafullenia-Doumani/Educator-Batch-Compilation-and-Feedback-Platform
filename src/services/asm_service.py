import json
from pathlib import Path
from subprocess import Popen, PIPE, TimeoutExpired
from concurrent.futures import ThreadPoolExecutor, as_completed

class AsmService:
    service_name = "asm"
    result_subdir = "assembly_results"

    def __init__(self, runner_jar: str, timeout: int = 10):
        self.runner_jar = runner_jar
        self.timeout = timeout

    def interpret_status(self, rc, out, err):
        out = (out or "").lower()
        err = (err or "").lower()


        if "error in" in out or "error in" in err:
            return "SIMULATION ERROR"
        if "timeout" in err:
            return "TIMEOUT"
        if rc == 0:
            return "OK"
        return "UNKNOWN"



    def run_all(self, submissions_root: Path, workers) -> dict[str, str]:
        submissions_root = Path(submissions_root)
        out_dir = submissions_root / "results" / self.result_subdir
        out_dir.mkdir(parents=True, exist_ok=True)

        summary = {}
        students = [
            d for d in submissions_root.iterdir()
            if d.is_dir() and d.name != "results" and not d.name.startswith(".")
        ]

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(self.run_folder, student): student for student in students}
            for fut in as_completed(futures):
                student_folder = futures[fut]
                try:
                    report = fut.result()
                    path = self.write_report(student_folder, report)
                    summary[student_folder.name] = path
                except Exception as e:
                    summary[student_folder.name] = f"ERROR: {e}"

        return summary

    def run_folder(self, student_folder: Path) -> list[dict]:
        asm_files = list(student_folder.glob("*.asm"))
        results = []

        for asm_file in asm_files:
            results.append(self.run_file(student_folder, asm_file))
        return results

    def run_file(self, folder: Path, asm_file: Path) -> dict:
        cmd = ["java", "-jar", self.runner_jar, "sm", asm_file.name]
        proc = Popen(
            cmd,
            cwd=str(folder),
            stdout=PIPE, stderr=PIPE, text=True
        )

        try:
            out, err = proc.communicate(timeout=self.timeout)
            rc = proc.returncode
        except TimeoutExpired:
            proc.kill()
            out, err = proc.communicate()
            rc = 1
            err = (err or "") + "\nTIMEOUT"

        status = self.interpret_status(rc, out, err)

        return {
            "asm_file": asm_file.name,
            "status": status,
            "returncode": rc,
            "stdout": out or "",
            "stderr": (err or "").strip(),
        }


    def write_report(self, student_folder: Path, report: list[dict]) -> str:
        if not isinstance(report, list):
            report = []
        out_dir = student_folder.parent / "results" / self.result_subdir
        out_file = out_dir / f"{self.service_name}_output_{student_folder.name}.json"
        out_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
        return str(out_file)
