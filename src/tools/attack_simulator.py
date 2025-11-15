from pathlib import Path
import time

LOG = Path("data/sample_logs/auth.log")

def simulate_bruteforce(n=50):
    with LOG.open("a") as f:
        for i in range(n):
            f.write("Failed password for root from 10.0.0.8 port 22 ssh2\n")
            time.sleep(0.01)
