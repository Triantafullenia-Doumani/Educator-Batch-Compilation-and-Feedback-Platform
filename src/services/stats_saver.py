# src/services/stats_saver.py

import json
from pathlib import Path

class StatsSaver:
    """
    Utility class to save stats dictionaries to JSON files.
    """

    @staticmethod
    def save(stats: dict, save_path: str | Path):
        """
        Save the given stats dictionary to a JSON file at save_path.
        """
        save_path = Path(save_path)
        save_path.parent.mkdir(exist_ok=True, parents=True)
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        print(f"Stats saved to {save_path}")
