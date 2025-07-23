# tests/test_compiler_results.py
import re
import json
import pytest
from tests.utils import load_json, normalize_stderr
from pathlib import Path
from src.services.batch_service import BatchService

def test_compiler_batch_results():
    submissions_dir = Path("tests/turnin_examples")
    expected_dir = Path("tests/expected_results/compiler_results")

    service = BatchService(
        submissions_dir=str(submissions_dir),
        exts=[".cpy"],
        timeout=30,
        workers=1
    )

    summary = service.run_all()

    for student, result_path in summary.items():
        if result_path.startswith("ERROR"):
            pytest.fail(f"{student} failed with: {result_path}")

        actual_json_path = Path(result_path)
        expected_json_path = expected_dir / f"compiler_output_{student}.json"

        assert actual_json_path.exists(), f"Missing output file for {student}"
        assert expected_json_path.exists(), f"Missing expected file for {student}"

        actual = load_json(actual_json_path)
        expected = load_json(expected_json_path)

        assert len(actual) == len(expected), f"Different number of entries for {student}"

        for i, (a, e) in enumerate(zip(actual, expected)):
            assert a["file"] == e["file"], f"{student} [#{i}] file mismatch"
            assert a["returncode"] == e["returncode"], f"{student} [#{i}] returncode mismatch"
            assert a["stdout"].strip() == e["stdout"].strip(), f"{student} [#{i}] stdout mismatch"
            assert a["outputs"] == e["outputs"], f"{student} [#{i}] outputs mismatch"

            # Normalize stderr before comparing
            a_stderr = normalize_stderr(a["stderr"]).strip()
            e_stderr = normalize_stderr(e["stderr"]).strip()

            if a_stderr != e_stderr:
                if (
                    e_stderr in ["TIMEOUT", ""] and "EOFError" in a_stderr
                ) or (
                    "EOFError" in e_stderr and a_stderr == ""
                ):
                    pass 
                else:
                    assert False, f"{student} [#{i}] stderr mismatch:\n\nACTUAL:\n{a_stderr}\n\nEXPECTED:\n{e_stderr}"
