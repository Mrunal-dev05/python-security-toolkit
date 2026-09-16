"""ARP spoof detection helper using the local ARP table."""

import ipaddress
import re
import subprocess


def run() -> None:
    print("\nARP Spoof Detector")
    print("Enter two observations for the same IP to compare MAC mappings.")
    ip = input("IP address: ").strip()
    mac1 = input("First observed MAC: ").strip().lower()
    mac2 = input("Second observed MAC: ").strip().lower()
    try:
        ipaddress.ip_address(ip)
        mac_re = r"([0-9a-f]{2}:){5}[0-9a-f]{2}"
        if not re.fullmatch(mac_re, mac1) or not re.fullmatch(mac_re, mac2):
            raise ValueError("Invalid MAC address.")
    except ValueError as exc:
        print(f"Invalid input: {exc}")
        return
    if mac1 != mac2:
        print(f"[WARNING] {ip} was observed with different MAC addresses.")
        print("This can be a sign of an ARP mapping change; investigate further in an authorized lab.")
    else:
        print(f"[OK] {ip} has a consistent observed MAC mapping.")


def show_local_arp_table() -> None:
    """Optional helper for viewing the OS ARP table; it does not modify it."""
    try:
        result = subprocess.run(["arp", "-a"], capture_output=True, text=True, check=False)
        print(result.stdout or result.stderr)
    except OSError as exc:
        print(f"Could not read local ARP table: {exc}")
