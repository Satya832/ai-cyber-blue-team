# 🚀 AI Cybersecurity Blue-Team Simulator
### *Autonomous Multi-Agent System for Real-Time Threat Detection & Response*

This project is a complete **multi-agent cybersecurity defense simulator**, where AI agents work together to detect, analyze, and respond to simulated cyber threats.  
It demonstrates real-world agent engineering concepts including:

- Multi-agent parallel & sequential pipelines  
- Event-driven communication  
- Tool integrations  
- Long-running agents  
- Memory & state management  
- Attack simulation  
- Observability & telemetry  

This is a fully working capstone-level project showcasing AI agent design and cybersecurity automation.

---

# 🧠 Project Overview

The simulator creates a virtual Blue-Team environment with autonomous agents that:

- Monitor logs  
- Detect attacks  
- Analyze threat context  
- Suggest mitigation actions  
- Generate incident reports  

All agents communicate through an **EventBus**, process data in real-time, and track historical memory for smarter decisions.

---

# 🧩 Key Features

### ✔ Multi-Agent System
- Long-running log monitor  
- Event-driven architecture  
- Threat detection agent  
- Incident analyzer agent  
- Mitigation agent  
- Reporter agent  

### ✔ Tools & Simulated Attacks
- Log generator  
- Brute-force attack simulation  
- SQL injection detection  
- Custom log parser  

### ✔ Memory & State
- Session memory  
- Persistent JSON memory store  

### ✔ Observability
- Detailed debug logs  
- Agent-level telemetry  
- Step-by-step processing trace  

### ✔ Reporting System
- Auto-generated incident reports  
- Saved as structured JSON  

---

# 🏛 System Architecture

       ┌──────────────────────────┐
       │     Log Generator        │
       └─────────────┬────────────┘
                     writes
                       ▼
            data/sample_logs/auth.log
                       ▼
            ┌──────────────────────┐
            │   LogMonitor Agent   │
            └──────────┬───────────┘
                 publishes log_event
                       ▼
            ┌──────────────────────┐
            │ ThreatDetector Agent │
            └──────────┬───────────┘
                 publishes incident
                       ▼
            ┌──────────────────────┐
            │ IncidentAnalyzer     │
            └──────────┬───────────┘
          publishes mitigation & report
                 ▼                 ▼
     ┌──────────────────┐   ┌─────────────────┐
     │ Mitigation Agent │   │  Reporter Agent │
     └──────────────────┘   └─────────────────┘


---
## 📁 Directory Structure

```
ai-cyber-blue-team/
├── data/
│   ├── sample_logs/
│   │   └── auth.log
│   └── memory_store.json
│
├── scripts/
│   └── generate_logs.py
│
├── src/
│   ├── agent_framework/
│   │   ├── agent_base.py
│   │   ├── eventbus.py
│   │   └── session_service.py
│   │
│   ├── agents/
│   │   ├── log_monitor.py
│   │   ├── threat_detector.py
│   │   ├── incident_analyzer.py
│   │   ├── mitigation_agent.py
│   │   └── reporter.py
│   │
│   ├── tools/
│   │   ├── log_parser.py
│   │   └── attack_simulator.py
│   │
│   ├── memory/
│   │   └── memory_bank.py
│   │
│   ├── observability/
│   │   └── telemetry.py
│   │
│   ├── web/
│   │   └── dashboard.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_log_parser.py
│   └── test_eventbus.py
│
├── docs/
│   └── submission_notes.md
│
└── README.md
```

---

# ⚙ Installation

### 1. Clone the repository

git clone git@github.com

:Satya832/ai-cyber-blue-team.git
cd ai-cyber-blue-team


### 2. Create virtual environment

python3 -m venv .venv
source .venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Set Python path

export PYTHONPATH="$PWD/src"


---

# ▶ Running the System

### 🟦 Terminal 1 — Start main simulator

source .venv/bin/activate
export PYTHONPATH="$PWD/src"
python -m src.main


### 🟩 Terminal 2 — Simulate attacks

**Brute-force example:**

echo "Failed password for root from 8.8.8.8 port 22 ssh2" >> data/sample_logs/auth.log


**Generate many logs:**

python scripts/generate_logs.py --fill


**SQL injection example:**

python scripts/generate_logs.py --sqli


---

# 📑 Output Examples

### ✔ Incident Report (JSON)

Saved in:

data/report_<timestamp>.json


Example:

{
"alert": {
"alert_type": "bruteforce",
"ip": "8.8.8.8",
"confidence": 0.7
}
}


### ✔ Mitigation Message

Displayed in Terminal 1:

[Mitigation] Suggested action for bruteforce


---

# 📌 Technologies Used

- Python  
- Multi-Agent Architecture  
- EventBus  
- Cybersecurity simulation  
- Log parsing  
- JSON reporting  
- SSH-based GitHub workflow  

---

# 🙌 Author
**Satyabrata Behera**
