"""Basic TCP network scanner for authorized lab networks."""

import ipaddress
import socket


def run() -> None:
    network_text = input("Lab subnet (example 192.168.1.0/24): ").strip()
    ports_text = input("Ports (comma-separated, example 22,80,443): ").strip()
    try:
        network = ipaddress.ip_network(network_text, strict=False)
        ports = [int(p.strip()) for p in ports_text.split(",") if p.strip()]
        if not ports or any(not 1 <= p <= 65535 for p in ports):
            raise ValueError("Ports must be between 1 and 65535.")
    except ValueError as exc:
        print(f"Invalid input: {exc}")
        return

    print(f"Scanning {network} on ports {ports} (authorized lab use only)...")
    for host in network.hosts():
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.25)
                if sock.connect_ex((str(host), port)) == 0:
                    print(f"[OPEN] {host}:{port}")
