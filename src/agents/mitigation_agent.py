class MitigationAgent:
    def __init__(self, event_bus, session, telemetry):
        print("[Init] MitigationAgent READY")
        event_bus.subscribe("incident", self.handle)

    def handle(self, inc):
        print(f"[Mitigation] Suggested action for {inc['alert']['alert_type']}")
