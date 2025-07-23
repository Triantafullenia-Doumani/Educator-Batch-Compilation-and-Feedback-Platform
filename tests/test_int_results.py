# tests/test_int_results.py
import re
import json
import pytest
from pathlib import Path
from src.services.int_service import IntService
from tests.utils import load_json, normalize_stderr


def test_int_batch_results():
    submissions_dir = Path("tests/turnin_examples")
    expected_dir = Path("tests/expected_results/intermediate_results")

    service = IntService(timeout=30)
    summary = service.run_all(submissions_dir, workers=1)

    for student, result_path in summary.items():
        if result_path.startswith("ERROR"):
            pytest.fail(f"{student} failed with: {result_path}")

        actual_json_path = Path(result_path)
        expected_json_path = expected_dir / f"int_output_{student}.json"

        assert actual_json_path.exists(), f"Missing output file for {student}"
        assert expected_json_path.exists(), f"Missing expected file for {student}"

        actual = load_json(actual_json_path)
        expected = load_json(expected_json_path)

        assert len(actual) == len(expected), f"Different number of results for {student}"

        for i, (a, e) in enumerate(zip(actual, expected)):
            assert a["int_file"] == e["int_file"], f"{student} [#{i}] int_file mismatch"
            assert a["c_file"] == e["c_file"], f"{student} [#{i}] c_file mismatch"
            assert a["status"] == e["status"], f"{student} [#{i}] status mismatch"
            assert a["compile_returncode"] == e["compile_returncode"], f"{student} [#{i}] compile returncode mismatch"
            assert a["compile_stdout"].strip() == e["compile_stdout"].strip(), f"{student} [#{i}] compile stdout mismatch"

            a_stderr = normalize_stderr(a["compile_stderr"]).strip()
            e_stderr = normalize_stderr(e["compile_stderr"]).strip()
            assert a_stderr == e_stderr, f"{student} [#{i}] compile stderr mismatch"

            assert a["exec_returncode"] == e["exec_returncode"], f"{student} [#{i}] exec returncode mismatch"
            assert a["exec_stdout"].strip() == e["exec_stdout"].strip(), f"{student} [#{i}] exec stdout mismatch"

            a_exec_err = normalize_stderr(a["exec_stderr"]).strip()
            e_exec_err = normalize_stderr(e["exec_stderr"]).strip()
            assert a_exec_err == e_exec_err, f"{student} [#{i}] exec stderr mismatch"
