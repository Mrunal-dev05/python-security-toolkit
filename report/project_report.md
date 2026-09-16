# Python Security Toolkit — Project Report

## 1. Cover Page

**Project Title:** Python Security Toolkit  
**Student Name:** Mrunal Prashant Pimpale  
**Course/Subject:** BE - Computer Engineering  
**Institution:** New Horizon Institute of Technology and Management  
**Academic Year:** Second year  
**Submission Date:** 16-09-2026

## 2. Abstract

The Python Security Toolkit is a modular command-line application developed as an academic cybersecurity project. It brings together seven security concepts: MAC address changing, network scanning, ARP spoofing, packet sniffing, network-jamming concepts, DNS spoofing, and ARP spoof detection. The project demonstrates Python modular programming, network fundamentals, input validation, passive packet inspection, and basic defensive detection. Potentially disruptive concepts are implemented as safe, non-invasive simulations for educational purposes.

## 3. Objectives

1. Build one CLI application that launches multiple security modules.
2. Practice Python functions, modules, validation, and exception handling.
3. Demonstrate authorized TCP network scanning.
4. Demonstrate passive packet inspection using Scapy.
5. Explain ARP and DNS spoofing concepts safely through simulation.
6. Demonstrate basic ARP IP/MAC mapping-change detection.
7. Develop and document a complete modular cybersecurity toolkit independently.

## 4. Tools and Technologies

- Python 3.10+
- Scapy
- TCP sockets and Python standard library
- Git and GitHub
- pytest
- Isolated or authorized lab environment

## 5. System Architecture

```text
                         +----------------+
                         |    main.py     |
                         |   CLI Menu     |
                         +-------+--------+
                                 |
        +------------------------+------------------------+
        |        |        |       |       |       |       |
       MAC     Scan     ARP    Sniffer  Jammer   DNS   Detector
        |        |      Demo      |      Demo    Demo      |
        +--------+------+---------+--------+------+---------+
                                 |
                         Authorized Lab
```

## 6. Module Documentation

### 6.1 MAC Changer

**Purpose:** Validate a requested MAC address and demonstrate the intended change.  
**Implementation:** Accepts an interface name and MAC address, validates the MAC format, and displays an educational preview.  
**Result:** The module provides a safe demonstration without automatically modifying the system network interface.

### 6.2 Network Scanner

**Purpose:** Identify selected TCP ports that accept connections on an authorized subnet.  
**Implementation:** Uses `ipaddress` for CIDR validation and Python TCP sockets with a short timeout.  
**Inputs:** Lab subnet and comma-separated TCP ports.

### 6.3 ARP Spoof Demo

**Purpose:** Demonstrate the concept of ARP cache poisoning.  
**Implementation:** Accepts documentation-only lab router and target values and displays a simulation.  
**Result:** The concept is demonstrated without transmitting forged ARP packets.

### 6.4 Packet Sniffer

**Purpose:** Demonstrate passive packet inspection.  
**Implementation:** Uses Scapy's `sniff` function and displays packet summaries.  
**Result:** The module demonstrates packet capture on an authorized interface.

### 6.5 Network Jammer Demo

**Purpose:** Demonstrate network availability disruption as a cybersecurity concept.  
**Implementation:** Runs a short simulated availability test.  
**Result:** The demonstration completes without generating deauthentication packets, flooding traffic, radio interference, or other disruptive activity.

### 6.6 DNS Spoof Demo

**Purpose:** Demonstrate how a manipulated DNS response could change a hostname-to-IP mapping.  
**Implementation:** Displays a simulated domain-to-IP mapping.  
**Result:** The concept is demonstrated without sending DNS packets or changing resolver settings.

### 6.7 ARP Spoof Detector

**Purpose:** Detect a change in the observed MAC address associated with the same IP address.  
**Implementation:** Validates an IP address and two MAC observations, then reports whether the mapping is consistent or has changed.

## 7. Testing Methodology

Testing was performed module by module using the project CLI and authorized/controlled test conditions.

| Test | Input/Environment | Expected Result | Actual Result |
|---|---|---|---|
| Launcher | `python main.py` | Menu appears | Menu displayed successfully. |
| Invalid menu choice | `9` | Validation message | Invalid choice was handled by the CLI. |
| MAC validation | Valid/invalid MAC | Correct acceptance/rejection | MAC input was validated and the requested change was shown as an educational preview. |
| Scanner | Authorized lab subnet + TCP ports | Open ports displayed | Network scanning module executed and displayed the scan result. |
| ARP demo | Lab documentation IPs | Simulation message | ARP spoofing concept was demonstrated through simulation. |
| Packet sniffer | Authorized interface, 5-10 packets | Packet summaries | Packet summaries were captured and displayed. |
| Jammer demo | Short simulation | Simulation completes | Network jammer concept completed as a safe simulation. |
| DNS demo | Test domain + simulated IP | Mapping displayed | Simulated DNS mapping was displayed successfully. |
| ARP detector | Same/different MAC observations | OK/warning | Detector evaluated the MAC observations and reported the mapping status. |

## 8. Results and Screenshots

The project testing evidence is stored in the `screenshots` directory.

- `screenshots/01-main-menu.png`
- `screenshots/02-mac-changer.png`
- `screenshots/03-network-scanner.png`
- `screenshots/04-arp-demo.png`
- `screenshots/05-packet-sniffer.png`
- `screenshots/06-jammer-demo.png`
- `screenshots/07-dns-demo.png`
- `screenshots/08-arp-detector.png`

The screenshots provide visual evidence of the CLI interface and module execution during project testing.

## 9. Challenges

- Designing a common CLI while keeping each module independent.
- Validating user-provided network addresses, MAC addresses, and ports.
- Handling operating-system differences in packet capture privileges.
- Integrating multiple cybersecurity concepts into one Python project.
- Keeping potentially disruptive security demonstrations safe and non-invasive.

## 10. Limitations

- This is an educational toolkit, not a production security assessment platform.
- Scanner results depend on routing, firewalls, host availability, and selected ports.
- Packet capture requires appropriate permissions and can expose sensitive traffic.
- ARP spoofing, DNS spoofing, and network-jamming components are simulations.
- The MAC changer demonstrates the requested change but does not automatically modify the host interface.

## 11. Future Improvements

- Add structured logging and JSON/CSV result export.
- Add automated unit tests for all input-validation and detection logic.
- Add cross-platform interface discovery.
- Add configuration management for lab settings.
- Add a dashboard for visualizing authorized lab results.

## 12. Conclusion

The Python Security Toolkit is a complete modular Python CLI project that combines multiple cybersecurity concepts in a single application. The project demonstrates programming, networking, validation, passive inspection, simulation, and defensive detection skills. The seven modules are integrated through a common command-line interface, documented clearly, and supported by testing screenshots. Potentially disruptive concepts are intentionally demonstrated in a safe and non-invasive manner.

## 13. References

- Python Documentation
- Scapy Documentation
- GitHub Documentation

## 14. Declaration

I confirm that this project was developed as an academic cybersecurity project and that testing was performed only on systems, interfaces, and networks for which I had appropriate authorization.

**Name:** Mrunal Prashant Pimpale  
**Date:** 16-09-2026
