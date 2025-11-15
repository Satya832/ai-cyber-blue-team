class ThreatDetectorAgent:
    def __init__(self, event_bus, session, telemetry):
        print("[Init] ThreatDetectorAgent READY")
        self.event_bus = event_bus
        event_bus.subscribe("log_event", self.handle)

    def handle(self, ev):
        if ev.get("type") == "failed_login":
            alert = {"alert_type": "bruteforce", "ip": ev["ip"], "confidence": 0.7}
            self.event_bus.publish("alert", alert)
        elif ev.get("type") == "sqli":
            alert = {"alert_type": "sqli", "confidence": 0.9}
            self.event_bus.publish("alert", alert)
