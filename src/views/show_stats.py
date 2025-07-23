# src/views/show_stats.py

from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem

class StatsTableAdapter:
    """
    Displays per-student stats in a table for:
    - compiler
    - assembly
    - intermediate (now same style as others)
    """

    _TYPES = {
        "compiler": {
            "columns": ["User", "Total source files", "Successful"],
            "keys":    ["total source files", "successful"]
        },
        "assembly": {
        "columns": ["User", "Total asm files", "Successful", "Simulation Error", "Timeout", ],
        "keys":    ["total asm files", "successful", "simulation error", "timeout", ]
        }
,
        "intermediate": {
            "columns": ["User", "Total .int files", "Successful / Total"],
            "keys":    ["total int files", "successful"]
        },
    }

    @classmethod
    def show_stats(cls, stats_table: QTableWidget, stats: dict, result_type: str = "compiler"):
        """
        Fill the table with per-user statistics depending on result_type.
        """

        if result_type not in cls._TYPES:
            raise ValueError(f"Unknown result_type '{result_type}' for stats table")

        config = cls._TYPES[result_type]
        stats_table.clearContents()
        stats_table.setRowCount(0)
        stats_table.setColumnCount(len(config["columns"]))
        stats_table.setHorizontalHeaderLabels(config["columns"])

        for row, (user, data) in enumerate(stats.items()):
            stats_table.insertRow(row)
            stats_table.setItem(row, 0, QTableWidgetItem(user))

            # Standard types
            if result_type in ["compiler", "assembly"]:
                for col_idx, key in enumerate(config["keys"], start=1):
                    value = data.get(key, 0) if isinstance(data, dict) else 0
                    stats_table.setItem(row, col_idx, QTableWidgetItem(str(value)))

            # Special format for intermediate: show success/total in one cell
            elif result_type == "intermediate":
                # Expecting per-user stats like { "cs200001": { "total int files": 3, "successful": 2 } }
                stats_table.setRowCount(len(stats))
                stats_table.setColumnCount(3)
                stats_table.setHorizontalHeaderLabels(["User", "Total .int files", "Successful"])

                for row, (user, data) in enumerate(stats.items()):
                    stats_table.setItem(row, 0, QTableWidgetItem(user))
                    total = data.get("total int files", 0) if isinstance(data, dict) else 0
                    success = data.get("successful", 0) if isinstance(data, dict) else 0
                    stats_table.setItem(row, 1, QTableWidgetItem(str(total)))
                    stats_table.setItem(row, 2, QTableWidgetItem(str(success)))

        stats_table.resizeColumnsToContents()
