
import json
from pathlib import Path

LOG_FILE = (
    Path(__file__).resolve().parent
    / "results"
    / "week3_audit.jsonl"
)


def calculate_metrics():
    if not LOG_FILE.exists():
        print("No experiment log found.")
        return

    with open(LOG_FILE, encoding="utf-8") as f:
        records = [
            json.loads(line)
            for line in f
            if line.strip()
        ]

    # Keep the most recent record for each
    # configuration and scenario pair.
    latest = {}

    for record in records:
        key = (
            record["configuration"],
            record["scenario_id"]
        )
        latest[key] = record

    for config in ["C0", "C1"]:
        group = [
            r for r in latest.values()
            if r["configuration"] == config
        ]

        completed = [
            r for r in group
            if r["status"] != "error"
        ]

        successes = sum(
            r["attack_success"]
            for r in completed
        )

        total = len(completed)
        asr = (
            (successes / total) * 100
            if total else 0
        )

        print(f"\nConfiguration: {config}")
        print(f"Recorded scenarios: {len(group)}")
        print(f"Completed scenarios: {total}")
        print(f"Successful attacks: {successes}")
        print(f"Attack Success Rate: {asr:.1f}%")

        if len(completed) != len(group):
            print(
                "Warning: Some scenarios failed. "
                "Results are incomplete."
            )


if __name__ == "__main__":
    calculate_metrics()
