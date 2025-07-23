# tests/utils.py
import json
import re
from pathlib import Path

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def normalize_stderr(stderr: str) -> str:
    """
    Normalize stderr to ensure consistent output comparison between platforms.
    Combines:
    - Path simplification (e.g. converting full paths to just 'c/<file>.c')
    - Replacing Windows backslashes with POSIX slashes
    - Optionally strips traceback noise
    """
    stderr = stderr.replace("\\", "/")

    # Normalize compiler paths: '.../c/foo.c' => 'c/foo.c'
    stderr = re.sub(r".*?/c/([^/]+\.c)", r"c/\1", stderr)

    # Optional: mask file paths in Python tracebacks
    stderr = re.sub(r'File ".*?", line \d+,', 'File "<file>", line <line>,', stderr)
    stderr = re.sub(r'C:/[^:\n]+', '<path>', stderr)

    return stderr.strip()
