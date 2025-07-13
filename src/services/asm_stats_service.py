import json

from pathlib import Path

class AsmStatsService:
    """
    Service to process results/assembly_results/runner_output_*.json files
    and provide execution statistics per student.
    """

    def __init__(self, results_folder: Path):
        self.results_folder = Path(results_folder)


    def gather_stats(self):
        print("gather_stats CALLED")
        stats = {}
        for file in self.results_folder.glob("asm_output_*.json"):
            print(f"Processing stats file: {file}")
            try:
                with open(file, encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                print(f"Error reading {file}: {e}")
                continue

            student = file.stem.split("_")[-1]  
            total_files = len(data)

            successful = sum(
                res.get("status") == "OK" and res.get("returncode") == 0
                for res in data
            )
            errors = sum(
                res.get("status") == "SIMULATION ERROR" and res.get("returncode") == 0
                for res in data
            )
            timeouts = sum(
                res.get("status") == "TIMEOUT" and res.get("returncode") == -1
                for res in data
            )

            stats[student] = {
                "total asm files": total_files,
                "successful": successful,
                "error": errors,
                "timeout": timeouts,
            }
        return stats
