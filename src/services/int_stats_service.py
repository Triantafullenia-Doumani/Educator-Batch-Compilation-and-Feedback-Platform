import json
from pathlib import Path

class IntStatsService:
    def __init__(self, results_folder: Path):
        self.results_folder = Path(results_folder)

    def gather_stats(self) -> dict[str, dict[str, int]]:
        """
        Return per-user stats with:
        {
            "cs200001": { "total int files": 3, "successful": 2 },
            ...
        }
        """
        stats = {}

        for json_file in self.results_folder.glob("int_output_*.json"):
            student = json_file.stem.removeprefix("int_output_")

            try:
                content = json_file.read_text(encoding="utf-8")
                results = json.loads(content)
                if not isinstance(results, list):
                    continue
            except Exception:
                continue

            total = 0
            successful = 0

            for res in results:
                if not isinstance(res, dict):
                    continue
                total += 1
                if res.get("status") == "OK":
                    successful += 1

            stats[student] = {
                "total int files": total,
                "successful": successful
            }

        return stats
