import random
import time

AUTH_LOG = "data/sample_logs/auth.log"

def generate_bruteforce_logs(count=200):
    print(f"[+] Generating {count} brute-force logs...")

    with open(AUTH_LOG, "a") as f:
        for _ in range(count):
            ip = f"10.0.0.{random.randint(1, 250)}"
            log = f"Failed password for root from {ip} port 22 ssh2\n"
            f.write(log)

    print(f"[+] Writing logs to {AUTH_LOG}")
    print("[+] Done! Added brute-force logs successfully.\n")


def generate_sqli_logs(count=20):
    print(f"[+] Generating {count} SQL injection logs...")

    with open(AUTH_LOG, "a") as f:
        for _ in range(count):
            ip = f"192.168.1.{random.randint(1, 250)}"
            log = f'GET /login.php?user=" OR 1=1;-- from {ip}\n'
            f.write(log)

    print(f"[+] Writing logs to {AUTH_LOG}")
    print("[+] Done! Added SQLi logs successfully.\n")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("--fill", action="store_true", help="Generate brute-force logs")
    parser.add_argument("--sqli", action="store_true", help="Generate SQLi logs")

    args = parser.parse_args()

    print("\n=== LOG GENERATOR STARTED ===")

    if args.fill:
        generate_bruteforce_logs()

    if args.sqli:
        generate_sqli_logs()

    if not args.fill and not args.sqli:
        print("[-] No option selected. Use --fill or --sqli")

    print("=== LOG GENERATOR FINISHED ===\n")

