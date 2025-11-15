import threading
import time
from src.agent_framework.eventbus import EventBus
from src.agent_framework.session_service import SessionService
from src.observability.telemetry import Telemetry
from src.agents.log_monitor import LogMonitorAgent
from src.agents.threat_detector import ThreatDetectorAgent
from src.agents.incident_analyzer import IncidentAnalyzerAgent
from src.agents.mitigation_agent import MitigationAgent
from src.agents.reporter import ReporterAgent

def main():
    bus = EventBus()
    session = SessionService()
    telemetry = Telemetry()

    log_mon = LogMonitorAgent(bus, session, telemetry, "data/sample_logs/auth.log")
    detector = ThreatDetectorAgent(bus, session, telemetry)
    analyzer = IncidentAnalyzerAgent(bus, session, telemetry)
    mitig = MitigationAgent(bus, session, telemetry)
    reporter = ReporterAgent(bus, session, telemetry)

    t = threading.Thread(target=log_mon.start, daemon=True)
    t.start()

    print("[System] Started. Use generate_logs or attack_simulator.")

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
