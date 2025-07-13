import os
import glob
import subprocess
from src.utils.cygwin_path import win_to_cygwin_path
from src.utils.perl_path import find_perl

class PlagiarismService:
    def __init__(self, moss_path):
        self.moss_path = moss_path  # Windows path to scripts/moss

    def run_moss(self, submissions_dir):
        try:
            perl_path = find_perl()  # Find Perl interpreter (cross-platform)
        except RuntimeError as e:
            return {"error": str(e)}

        submissions_dir = os.path.abspath(submissions_dir)
        files = glob.glob(os.path.join(submissions_dir, "*", "*.py"))
        if not files:
            return {"error": "No Python files found for plagiarism check."}

        # Convert Moss script and file paths to Cygwin format for Cygwin Perl
        moss_cyg_path = win_to_cygwin_path(self.moss_path)
        file_cyg_paths = [win_to_cygwin_path(f) for f in files]

        cmd = [perl_path, moss_cyg_path, "-l", "python"] + file_cyg_paths
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            stdout, stderr = proc.communicate()
            if proc.returncode != 0:
                return {"error": stderr or stdout}
            url = None
            for line in stdout.splitlines():
                if "http" in line:
                    url = line.strip()
                    break
            if url:
                return {"url": url, "stdout": stdout}
            else:
                return {"error": "No Moss report URL found.", "stdout": stdout}
        except Exception as e:
            return {"error": str(e)}
