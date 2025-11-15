import time
from src.tools.log_parser import parse_lines

class LogMonitorAgent:
    def __init__(self, event_bus, session, telemetry, log_path):
        print("[Init] LogMonitorAgent READY")
        self.event_bus = event_bus
        self.session = session
        self.telemetry = telemetry
        self.log_path = log_path
        self._pos = 0
        self._running = False

    def start(self):
        print("[DEBUG] LogMonitor STARTED. Watching:", self.log_path)
        self._running = True
        while self._running:
            print("[DEBUG] Loop iteration. Reading log...")

            try:
                with open(self.log_path, "r") as f:
                    f.seek(self._pos)
                    new_data = f.read()
                    print("[DEBUG] New data length:", len(new_data))
                    self._pos = f.tell()
            except Exception as e:
                print("[DEBUG] Error reading file:", e)
                new_data = ""

            if new_data:
                lines = new_data.splitlines()
                print("[DEBUG] Parsed", len(lines), "lines")
                for line in lines:
                    print("[DEBUG] RAW LINE:", line)
                events = parse_lines(lines)
                print("[DEBUG] EVENTS FOUND:", events)

                for ev in events:
                    self.event_bus.publish("log_event", ev)

            time.sleep(1)

    def stop(self):
        self._running = False

