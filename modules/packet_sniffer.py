"""Passive packet inspection demo.

Requires Scapy and elevated privileges on many systems. Capture only on an
interface/network you are authorized to monitor.
"""


def run() -> None:
    try:
        from scapy.all import sniff
    except ImportError:
        print("Scapy is not installed. Run: pip install -r requirements.txt")
        return

    interface = input("Interface to monitor (blank = default): ").strip() or None
    count_text = input("Number of packets (default 10): ").strip()
    count = int(count_text) if count_text else 10
    if count < 1 or count > 1000:
        print("Packet count must be between 1 and 1000.")
        return

    def show(packet):
        print(packet.summary())

    print("Starting passive capture. Press Ctrl+C to stop.")
    sniff(iface=interface, prn=show, count=count, store=False)
