from pathlib import Path
import pytest
from src.services.asm_service import AsmService
from tests.utils import load_json, normalize_stderr

def test_asm_batch_results():
    submissions_dir = Path("tests/turnin_examples")
    expected_dir = Path("tests/expected_results/assembly_results")
    runner_jar = Path("lib/rars_46ab74d.jar").resolve()

    assert runner_jar.exists(), f"RARS jar not found at: {runner_jar}"

    service = AsmService(timeout=30, runner_jar=runner_jar)
    summary = service.run_all(submissions_dir, workers=1)

    for student, result_path in summary.items():
        if result_path.startswith("ERROR"):
            pytest.fail(f"{student} failed with: {result_path}")

        actual_json_path = Path(result_path)
        expected_json_path = expected_dir / f"asm_output_{student}.json"

        assert actual_json_path.exists(), f"Missing output file for {student}"
        assert expected_json_path.exists(), f"Missing expected file for {student}"

        actual = load_json(actual_json_path)
        expected = load_json(expected_json_path)

        assert len(actual) == len(expected), f"Different number of results for {student}"

        for i, (a, e) in enumerate(zip(actual, expected)):
            assert a["asm_file"] == e["asm_file"], f"{student} [#{i}] asm_file mismatch"
            assert a["status"] == e["status"], f"{student} [#{i}] status mismatch"
            assert a["returncode"] == e["returncode"], f"{student} [#{i}] returncode mismatch"

            if "timeout" in a["stderr"].casefold():
                print(f"Skipping stdout check for timeout case: {student} #{i}")
            else:
                assert a["stdout"].strip() == e["stdout"].strip(), f"{student} [#{i}] stdout mismatch"

            a_stderr = normalize_stderr(a["stderr"]).strip()
            e_stderr = normalize_stderr(e["stderr"]).strip()
            assert a_stderr == e_stderr, f"{student} [#{i}] stderr mismatch"
