import json
from pathlib import Path

class AsmStatsService:
    """
    Service to process results/assembly_results/asm_output_*.json files
    and provide execution statistics per student.
    """

    def __init__(self, results_folder: Path):
        self.results_folder = Path(results_folder)

    def gather_stats(self):
        stats = {}

        for file in self.results_folder.glob("asm_output_*.json"):
            try:
                with open(file, encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                print(f"Error reading {file}: {e}")
                continue

            student = file.stem.split("_")[-1]
            total_files = len(data)

            counts = {
                "OK": 0,
                "SIMULATION ERROR": 0,
                "TIMEOUT": 0,
                "CRASH": 0,
                "UNKNOWN": 0,
            }

            for res in data:
                status = res.get("status", "UNKNOWN").upper()
                if status in counts:
                    counts[status] += 1
                else:
                    counts["UNKNOWN"] += 1

            stats[student] = {
                "total asm files": total_files,
                "successful": counts["OK"],
                "simulation error": counts["SIMULATION ERROR"],
                "timeout": counts["TIMEOUT"],
            }

        return stats
