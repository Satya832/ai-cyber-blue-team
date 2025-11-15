import json
from pathlib import Path

DATA_STORE = Path(__file__).resolve().parents[2] / 'data' / 'memory_store.json'

class SessionService:
    def __init__(self):
        try:
            with open(DATA_STORE) as f:
                self.store = json.load(f)
        except:
            self.store = {"incidents": [], "ips": []}

    def add_incident(self, incident):
        self.store["incidents"].append(incident)
        if "ip" in incident.get("alert", {}):
            self.store["ips"].append(incident["alert"]["ip"])
        with open(DATA_STORE, "w") as f:
            json.dump(self.store, f, indent=2)

    def get_incidents(self):
        return self.store["incidents"]
