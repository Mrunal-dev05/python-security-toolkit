"""ARP spoofing concept demo without sending forged packets."""


def run() -> None:
    print("\nARP Spoof Demo")
    print("ARP spoofing can redirect traffic by poisoning a local ARP cache.")
    print("This project uses a non-invasive simulation and does not transmit forged ARP packets.")
    router = input("Lab router IP (for documentation): ").strip()
    target = input("Lab target IP (for documentation): ").strip()
    if not router or not target:
        print("Both lab IPs are required.")
        return
    print(f"Simulation configured: router={router}, target={target}")
