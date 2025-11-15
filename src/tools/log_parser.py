import re

FAILED = re.compile(
    r"Failed password for (?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

SQLI = re.compile(
    r"(OR\s+1=1|--)", re.IGNORECASE
)

def parse_lines(lines):
    events = []
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue

        # Failed login
        m = FAILED.search(ln)
        if m:
            events.append({
                "type": "failed_login",
                "ip": m.group("ip"),
                "user": m.group("user"),
                "raw": ln
            })
            continue

        # SQL injection
        if SQLI.search(ln):
            events.append({"type": "sqli", "raw": ln})

    return events

