# Python Security Toolkit — Project Report

> **Submission note:** Replace every bracketed placeholder with your real information and actual lab results. Do not claim a test was completed unless you performed it.

## 1. Cover Page

**Project Title:** Python Security Toolkit  
**Student Name:** [Your Name]  
**Roll Number:** [Roll Number]  
**Course/Subject:** [Course Name]  
**Institution:** [Institution Name]  
**Academic Year:** [Year]  
**Submission Date:** [Date]

## 2. Abstract

The Python Security Toolkit is a modular command-line application that brings together seven cybersecurity concepts: MAC address changing, network scanning, ARP spoofing, packet sniffing, network-jamming concepts, DNS spoofing, and ARP spoof detection. The project focuses on learning Python modular design, network fundamentals, input validation, passive inspection, and basic defensive detection. Potentially disruptive concepts are represented with non-invasive simulations rather than forged packets, interference, or traffic manipulation.

## 3. Objectives

1. Build one CLI application that launches multiple security modules.
2. Practice Python functions, modules, validation, and exception handling.
3. Demonstrate authorized TCP network scanning.
4. Demonstrate passive packet inspection using Scapy.
5. Explain ARP and DNS spoofing concepts safely through simulation.
6. Demonstrate basic ARP IP/MAC mapping-change detection.
7. Document testing methodology, results, limitations, and future improvements.

## 4. Tools and Technologies

- Python 3.10+
- Scapy
- TCP sockets and Python standard library
- Git and GitHub
- pytest (for automated tests where applicable)
- An isolated/authorized lab or virtual machine environment

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

**Purpose:** Validate a requested MAC address and show what would be changed.  
**Implementation:** Accepts an interface name and MAC address, validates the MAC format, and prints an educational preview.  
**Safety:** The module does not modify the host interface automatically.

### 6.2 Network Scanner

**Purpose:** Identify selected TCP ports that accept connections on an authorized subnet.  
**Implementation:** Uses `ipaddress` for CIDR validation and Python TCP sockets with a short timeout.  
**Inputs:** Lab subnet and comma-separated TCP ports.

### 6.3 ARP Spoof Demo

**Purpose:** Explain the concept of ARP cache poisoning.  
**Implementation:** Collects documentation-only lab router/target values and prints a simulation.  
**Safety:** No forged ARP packets are transmitted.

### 6.4 Packet Sniffer

**Purpose:** Demonstrate passive packet inspection.  
**Implementation:** Uses Scapy's `sniff` function and prints packet summaries.  
**Safety:** Capture only traffic from an interface/network that the tester is authorized to monitor.

### 6.5 Network Jammer Demo

**Purpose:** Explain availability disruption as a security concept.  
**Implementation:** Simulates a short availability test.  
**Safety:** No deauthentication, flooding, radio interference, or other disruptive traffic is generated.

### 6.6 DNS Spoof Demo

**Purpose:** Explain how a manipulated DNS response could change a hostname-to-IP mapping.  
**Implementation:** Prints a simulated domain-to-IP mapping.  
**Safety:** No DNS packets or resolver settings are changed.

### 6.7 ARP Spoof Detector

**Purpose:** Identify a change in the observed MAC address associated with the same IP address.  
**Implementation:** Validates an IP and two MAC observations, then reports either consistency or a warning for a mapping change.

## 7. Testing Methodology

Testing should be performed module by module in an isolated or explicitly authorized environment.

| Test | Input/Environment | Expected Result | Actual Result |
|---|---|---|---|
| Launcher | `python main.py` | Menu appears | [Fill in] |
| Invalid menu choice | `9` | Validation message | [Fill in] |
| MAC validation | Valid/invalid MAC | Correct acceptance/rejection | [Fill in] |
| Scanner | Authorized lab subnet + TCP ports | Open ports displayed | [Fill in] |
| ARP demo | Lab documentation IPs | Simulation message | [Fill in] |
| Packet sniffer | Authorized interface, 5-10 packets | Packet summaries | [Fill in] |
| Jammer demo | 1-30 second simulation | Simulation completes | [Fill in] |
| DNS demo | Test domain + simulated IP | Mapping displayed | [Fill in] |
| ARP detector | Same/different MAC observations | OK/warning | [Fill in] |

## 8. Results and Screenshots

Add your own screenshots below. Recommended filenames:

- `screenshots/01-main-menu.png`
- `screenshots/02-mac-changer.png`
- `screenshots/03-network-scanner.png`
- `screenshots/04-arp-demo.png`
- `screenshots/05-packet-sniffer.png`
- `screenshots/06-jammer-demo.png`
- `screenshots/07-dns-demo.png`
- `screenshots/08-arp-detector.png`

For each screenshot, write one or two sentences describing the test environment and observed result.

## 9. Challenges

- Designing a common CLI while keeping each module independent.
- Validating user-provided network addresses and ports.
- Handling operating-system differences in packet capture privileges.
- Presenting offensive-security concepts without creating an unsafe or disruptive implementation.

## 10. Limitations

- This is an educational toolkit, not a production security assessment platform.
- Scanner results depend on routing, firewalls, host availability, and selected ports.
- Packet capture requires appropriate permissions and can expose sensitive traffic.
- ARP spoofing, DNS spoofing, and network-jamming components are simulations.
- The MAC changer is a preview rather than an automatic interface-modification utility.

## 11. Future Improvements

- Add structured logging and JSON/CSV result export.
- Add automated unit tests for input validation and detection logic.
- Add cross-platform interface discovery.
- Add configuration management for lab settings.
- Add a dashboard for visualizing authorized lab results.

## 12. Conclusion

The Python Security Toolkit demonstrates how multiple network-security concepts can be organized into a maintainable Python CLI. The project combines practical programming skills with cybersecurity fundamentals while keeping potentially disruptive demonstrations non-invasive. Testing evidence and final observations should be updated from the student's actual authorized lab work.

## 13. References

- Python documentation: https://docs.python.org/3/
- Scapy documentation: https://scapy.readthedocs.io/
- GitHub documentation: https://docs.github.com/

## 14. Declaration

I confirm that the testing described in this report was performed only on systems, interfaces, and networks for which I had appropriate authorization.

**Name:** [Your Name]  
**Signature:** [Signature if required]  
**Date:** [Date]
