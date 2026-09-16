"""DNS spoofing concept demo without modifying DNS traffic."""


def run() -> None:
    print("\nDNS Spoof Demo")
    domain = input("Lab domain to simulate: ").strip()
    fake_ip = input("Simulated response IP: ").strip()
    if not domain or not fake_ip:
        print("Domain and IP are required.")
        return
    print("Simulation only: no DNS packets or resolver settings were changed.")
    print(f"{domain} -> {fake_ip}")
