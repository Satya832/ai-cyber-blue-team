import time

class IncidentAnalyzerAgent:
    def __init__(self, event_bus, session, telemetry):
        self.event_bus = event_bus
        self.session = session
        event_bus.subscribe("alert", self.handle)

    def handle(self, alert):
        incident = {
            "id": int(time.time() * 1000),
            "alert": alert,
            "analysis": f"Detected {alert['alert_type']}",
            "timestamp": time.time()
        }
        self.session.add_incident(incident)
        self.event_bus.publish("incident", incident)
