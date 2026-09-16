# Testing Guide

Use an isolated virtual machine/lab network or localhost. Do not test against networks or devices without explicit authorization.

## 1. Launcher smoke test

Run:

```bash
python main.py
```

Expected evidence:
- The menu displays options 1-7 and 0.
- Entering an invalid option prints a validation message.
- Entering `0` exits cleanly.

## 2. MAC Changer

Use a lab interface name and a clearly fictional/test MAC value.

Expected:
- Valid MAC format is accepted.
- The module states that it is an educational preview.
- No host interface is changed automatically.

Screenshot suggestion: terminal showing the module and validation result.

## 3. Network Scanner

Use only a subnet you control. For a simple local test, scan a small range and one or two TCP ports.

Expected:
- Valid CIDR and port input is accepted.
- Open TCP ports are reported as `[OPEN]`.
- Invalid ports or CIDR values are rejected.

Screenshot suggestion: terminal showing the supplied lab subnet and scan result.

## 4. ARP Spoof Demo

Enter documentation-only lab IP addresses.

Expected:
- The module prints the configured values.
- It clearly states that no forged ARP packets are transmitted.

## 5. Packet Sniffer

Capture only an interface and traffic that you are authorized to monitor.

Expected:
- Scapy imports successfully after installing `requirements.txt`.
- Packet summaries are printed until the requested count is reached.
- Invalid packet counts are rejected.

Screenshot suggestion: terminal with a small packet count such as 5-10.

## 6. Network Jammer Demo

Use a short simulation duration between 1 and 30 seconds.

Expected:
- The module reports a simulated availability test.
- No deauthentication, flooding, radio interference, or other disruptive traffic occurs.

## 7. DNS Spoof Demo

Use a test/documentation domain and a simulated IP address.

Expected:
- The module prints the simulated mapping.
- It states that DNS packets and resolver settings were not modified.

## 8. ARP Spoof Detector

Provide one IP address with either matching or different observed MAC addresses.

Expected:
- Matching MAC values produce an `[OK]` result.
- Different MAC values produce a `[WARNING]` result and recommend investigation.

## Evidence checklist

- [ ] Launcher menu screenshot
- [ ] MAC Changer screenshot
- [ ] Network Scanner screenshot
- [ ] ARP Spoof Demo screenshot
- [ ] Packet Sniffer screenshot
- [ ] Network Jammer Demo screenshot
- [ ] DNS Spoof Demo screenshot
- [ ] ARP Spoof Detector screenshot
- [ ] README and repository structure checked
- [ ] Actual test dates/environment recorded in the report
