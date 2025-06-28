import json
from pathlib import Path

class BatchStatsService:
    """
    Service to process result JSON files and provide compile statistics per student.
    """

    def __init__(self, results_folder: Path):
        self.results_folder = Path(results_folder)

    def gather_stats(self):
        print("gather_stats CALLED")
        stats = {}
        for file in self.results_folder.glob("compiler_output_*.json"):
            print(f"Processing stats file: {file}")
            try:
                with open(file, encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                print(f"Error reading {file}: {e}")
                continue
            student = file.stem.replace("compiler_output_", "")
            total_files = len(data)
            successful = sum((res["returncode"] == 0 and not res["stderr"]) for res in data)
            failed = total_files - successful
            stats[student] = {
                "total source files": total_files,
                "successful": successful,
            }
        print("Stats ready:", stats)
        return stats
