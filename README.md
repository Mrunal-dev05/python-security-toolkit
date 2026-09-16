# Python Security Toolkit

A Python-based cybersecurity toolkit that brings together seven network-security and ethical-hacking concepts in one command-line application for educational and authorized lab environments.

> **Safety:** Use this project only on systems and networks you own or have explicit permission to test. ARP spoofing, DNS spoofing, and network-jamming components are intentionally non-invasive simulations. The MAC changer is an educational preview and does not modify the host automatically.

## Objectives

- Integrate multiple cybersecurity concepts into one Python CLI.
- Practice modular Python project structure and input validation.
- Demonstrate network scanning and passive packet inspection in an authorized lab.
- Explain ARP/DNS spoofing and availability attacks without transmitting disruptive or forged traffic.
- Demonstrate basic ARP mapping-change detection.

## Modules

| # | Module | Purpose | Safety behavior |
|---|---|---|---|
| 1 | MAC Changer | Validate and preview a requested MAC address | No automatic system change |
| 2 | Network Scanner | Check selected TCP ports on a lab subnet | User supplies subnet/ports |
| 3 | ARP Spoof Demo | Explain ARP poisoning concept | Simulation only; no forged packets |
| 4 | Packet Sniffer | Display packet summaries with Scapy | Passive capture only; authorized interface |
| 5 | Network Jammer Demo | Explain availability disruption | Simulation only; no interference/flooding |
| 6 | DNS Spoof Demo | Explain manipulated DNS responses | Simulation only; no DNS traffic modification |
| 7 | ARP Spoof Detector | Compare observed IP/MAC mappings | Detection only; no network changes |

## Architecture

```text
                 +----------------------+
                 |       main.py        |
                 |   CLI menu / errors  |
                 +----------+-----------+
                            |
        +-------------------+-------------------+
        |         |         |        |          |
      MAC       Scan      ARP Demo  Sniffer   Detector
        |         |         |        |          |
        +---------+---------+--------+----------+
                            |
                    Authorized Lab
```

## Project Structure

```text
python-security-toolkit/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── modules/
│   ├── __init__.py
│   ├── mac_changer.py
│   ├── network_scanner.py
│   ├── arp_spoofer.py
│   ├── packet_sniffer.py
│   ├── network_jammer.py
│   ├── dns_spoofer.py
│   └── arp_spoof_detector.py
├── docs/
│   └── TESTING.md
└── report/
    └── project_report.md
```

## Requirements

- Python 3.10+
- Scapy for the packet-sniffer module
- pytest for automated validation tests when tests are added
- Administrator/root privileges may be required for packet capture on some systems

## Installation

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Example Workflow

1. Start `python main.py`.
2. Select a module from the menu.
3. Provide only lab/authorized values.
4. Record terminal output for the project report.
5. For packet capture, stop the module with `Ctrl+C` when the requested packet count is reached or when you want to end the demonstration.

## Testing

See [`docs/TESTING.md`](docs/TESTING.md) for a module-by-module test checklist and expected evidence. Do not scan, capture, spoof, or disrupt networks without authorization.

## Report

A ready-to-complete project report is provided in [`report/project_report.md`](report/project_report.md). Replace the screenshot placeholders with your own authorized lab screenshots and add your name, institution, and actual test results before submission.

## Limitations

- The toolkit is a learning project, not a production security scanner.
- Network results depend on firewall rules, routing, operating system behavior, and the selected lab network.
- The ARP/DNS/jamming modules are simulations rather than offensive implementations.
- Packet summaries can contain sensitive information, so captures should be limited to authorized test traffic.

## Future Improvements

- Add structured logging and exportable JSON results.
- Add a configuration file for lab settings.
- Add unit tests for validation and detection logic.
- Improve cross-platform interface discovery.
- Add a small desktop/web dashboard for visualizing authorized lab results.

## Disclaimer

This repository is intended for cybersecurity education, coursework, and authorized testing only. The user is responsible for complying with applicable laws, policies, and network-owner permissions.
