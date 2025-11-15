import threading

class AgentBase(threading.Thread):
    def __init__(self, name, event_bus, session, telemetry):
        super().__init__(daemon=True)
        self.name = name
        self.event_bus = event_bus
        self.session = session
        self.telemetry = telemetry
