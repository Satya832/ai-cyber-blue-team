import json
from pathlib import Path

REPORT_DIR = Path("data")

class ReporterAgent:
    def __init__(self, event_bus, session, telemetry):
        print("[Init] Reporter READY")
        event_bus.subscribe("incident", self.report)

    def report(self, inc):
        path = REPORT_DIR / f"report_{inc['id']}.json"
        path.write_text(json.dumps(inc, indent=2))
        print(f"[Reporter] Saved report {path}")
