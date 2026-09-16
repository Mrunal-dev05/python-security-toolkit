# Python Security Toolkit

A Python-based cybersecurity toolkit that brings together network security and ethical-hacking concepts in one command-line application.

> **Safety:** Use this project only on systems and networks you own or have explicit permission to test. The ARP spoofing, DNS spoofing, and network-jamming components are intentionally non-invasive simulations.

## Modules

1. MAC Changer — validates and previews a requested MAC change without modifying the host.
2. Network Scanner — checks selected TCP ports on an authorized lab subnet.
3. ARP Spoof Demo — explains and simulates ARP poisoning without sending forged packets.
4. Packet Sniffer — passively displays packet summaries using Scapy.
5. Network Jammer Demo — simulates an availability test without disrupting traffic.
6. DNS Spoof Demo — simulates a DNS response without changing resolver traffic.
7. ARP Spoof Detector — compares observed IP/MAC mappings and flags changes.

## Project Structure

```text
python-security-toolkit/
├── main.py
├── requirements.txt
├── README.md
└── modules/
    ├── __init__.py
    ├── mac_changer.py
    ├── network_scanner.py
    ├── arp_spoofer.py
    ├── packet_sniffer.py
    ├── network_jammer.py
    ├── dns_spoofer.py
    └── arp_spoof_detector.py
```

## Setup

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Packet capture may require administrator/root privileges depending on the operating system and capture interface.

## Testing

Test the toolkit in an isolated lab or virtual network. For the scanner, use a subnet and ports belonging to your lab. For the packet sniffer, capture only traffic you are authorized to monitor.

## Learning Goals

- Python modules and CLI application design
- Network addressing and TCP connectivity
- Packet inspection concepts
- ARP and DNS security concepts
- Basic detection and input validation
- Safe cybersecurity experimentation
