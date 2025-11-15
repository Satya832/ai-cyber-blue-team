#!/usr/bin/env python3
import time
from pathlib import Path
import argparse
import random

LOG_DIR = Path(__file__).resolve().parents[1] / 'data' / 'sample_logs'

def fill_auth(n=50):
    p = LOG_DIR / 'auth.log'
    with p.open('a') as f:
        for i in range(n):
            ip = f"10.0.0.{random.randint(2,250)}"
            f.write(f"Failed password for root from {ip} port 22 ssh2\n")
            time.sleep(0.01)

def sqli_example():
    p = LOG_DIR / 'web_traffic.log'
    with p.open('a') as f:
        f.write("GET /index.php?id=1 OR 1=1 -- HTTP/1.1\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fill', action='store_true')
    parser.add_argument('--sqli', action='store_true')
    args = parser.parse_args()
    if args.fill:
        fill_auth(100)
    if args.sqli:
        sqli_example()
