import json
import platform
from pathlib import Path
from subprocess import Popen, PIPE, TimeoutExpired
from concurrent.futures import ThreadPoolExecutor, as_completed
from .int_to_c_translator import write_to_c


class IntService:
    service_name = "int"
    result_subdir = "intermediate_results"

    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    def run_all(self, submissions_root: Path, workers: int = 4) -> dict[str, str]:
        submissions_root = Path(submissions_root)
        out_dir = submissions_root / "results" / self.result_subdir
        out_dir.mkdir(parents=True, exist_ok=True)

        summary: dict[str, str] = {}
        students = [
            d for d in submissions_root.iterdir()
            if d.is_dir() and d.name != "results" and not d.name.startswith(".")
        ]

        with ThreadPoolExecutor(max_workers=workers) as exe:
            futures = {exe.submit(self.run_folder, s): s for s in students}
            for fut in as_completed(futures):
                student = futures[fut].name
                try:
                    report = fut.result()  
                    path = self.write_report(futures[fut], report)
                    summary[student] = path
                except Exception as e:
                    summary[student] = f"ERROR: {e}"
        return summary

    def run_folder(self, student_folder: Path) -> list[dict]:
        int_files = list(student_folder.glob("*.int"))
        c_folder = student_folder / "c"
        c_folder.mkdir(exist_ok=True)

        results: list[dict] = []
        for intf in int_files:
            result = self.run_file(student_folder, intf)
            results.append(result)
        return results

    def run_file(self, student_folder: Path, int_file: Path) -> dict:
        stem = int_file.stem
        c_file = student_folder / "c" / f"{stem}.c"
        exe = student_folder / (stem + (".exe" if platform.system() == "Windows" else ""))

        write_to_c(str(int_file), str(c_file))
        if not c_file.exists() or c_file.stat().st_size == 0:
            return {
                "int_file": int_file.name,
                "c_file": c_file.name,
                "status": "TRANSLATION FAILED",
                "compile_returncode": None,
                "compile_stdout": "",
                "compile_stderr": "C file not generated or empty.",
                "exec_returncode": None,
                "exec_stdout": "",
                "exec_stderr": ""
            }

        # compile
        try:
            proc = Popen(["gcc", str(Path("c") / c_file.name), "-o", exe.name],
             cwd=student_folder, stdout=PIPE, stderr=PIPE, text=True)

            comp_out, comp_err = proc.communicate(timeout=self.timeout)
            comp_rc = proc.returncode
        except TimeoutExpired:
            proc.kill()
            comp_out, comp_err = proc.communicate()
            comp_rc = -1
            comp_err += "\nCOMPILATION TIMEOUT"

        if comp_rc != 0 or not exe.exists():
            return {
                "int_file": int_file.name,
                "c_file": c_file.name,
                "status": "COMPILATION FAILED",
                "compile_returncode": comp_rc,
                "compile_stdout": comp_out.strip(),
                "compile_stderr": comp_err.strip(),
                "exec_returncode": None,
                "exec_stdout": "",
                "exec_stderr": ""
            }

        # run executable
        cmd = [str(exe)] if platform.system() == "Windows" else [f"./{exe.name}"]
        try:
            run_proc = Popen(cmd, cwd=student_folder, stdout=PIPE, stderr=PIPE, text=True)
            run_out, run_err = run_proc.communicate(timeout=self.timeout)
            run_rc = run_proc.returncode
            status = "OK" if run_rc == 0 else "RUNTIME ERROR"
        except TimeoutExpired:
            run_proc.kill()
            run_out, run_err = run_proc.communicate()
            run_rc = -1
            run_err += "\nEXECUTION TIMEOUT"
            status = "TIMEOUT"

        return {
            "int_file": int_file.name,
            "c_file": c_file.name,
            "status": status,
            "compile_returncode": comp_rc,
            "compile_stdout": comp_out.strip(),
            "compile_stderr": comp_err.strip(),
            "exec_returncode": run_rc,
            "exec_stdout": run_out.strip(),
            "exec_stderr": run_err.strip(),
        }



    def write_report(self, student_folder: Path, report: list[dict]) -> str:
        out_dir = student_folder.parent / "results" / self.result_subdir
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{self.service_name}_output_{student_folder.name}.json"
        out_file.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")

        print(f"[IntService] Writing full report to {out_file}")  # ✅ DEBUG print
        return str(out_file)
