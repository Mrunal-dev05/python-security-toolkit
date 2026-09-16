"""MAC address change demonstration.

This module intentionally prints the command rather than changing the host
interface automatically. Apply changes manually only in an authorized lab.
"""

import re


def run() -> None:
    interface = input("Interface name: ").strip()
    mac = input("New MAC address (AA:BB:CC:DD:EE:FF): ").strip()
    if not interface or not re.fullmatch(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", mac):
        print("Invalid interface or MAC address.")
        return
    print("Educational preview only. No system change was made.")
    print(f"Target interface: {interface}")
    print(f"Requested MAC: {mac}")
