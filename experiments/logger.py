
import json
from datetime import datetime, timezone
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parent / "results"


def log_event(event):
    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    record = {
        "timestamp": datetime.now(
            timezone.utc
        ).isoformat(),
        **event
    }

    path = RESULTS_DIR / "week3_audit.jsonl"

    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

    return record
