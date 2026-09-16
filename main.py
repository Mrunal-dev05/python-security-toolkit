"""Python Security Toolkit - educational network security launcher.

Use only on systems and networks you own or have explicit permission to test.
"""

from modules.arp_spoof_detector import run as arp_spoof_detector
from modules.arp_spoofer import run as arp_spoofer
from modules.dns_spoofer import run as dns_spoofer
from modules.mac_changer import run as mac_changer
from modules.network_jammer import run as network_jammer
from modules.network_scanner import run as network_scanner
from modules.packet_sniffer import run as packet_sniffer


def show_menu() -> None:
    print("\n=== Python Security Toolkit ===")
    print("1. MAC Changer")
    print("2. Network Scanner")
    print("3. ARP Spoof Demo")
    print("4. Packet Sniffer")
    print("5. Network Jammer Demo")
    print("6. DNS Spoof Demo")
    print("7. ARP Spoof Detector")
    print("0. Exit")


def main() -> None:
    actions = {
        "1": mac_changer,
        "2": network_scanner,
        "3": arp_spoofer,
        "4": packet_sniffer,
        "5": network_jammer,
        "6": dns_spoofer,
        "7": arp_spoof_detector,
    }

    while True:
        show_menu()
        choice = input("Select an option: ").strip()
        if choice == "0":
            print("Exiting toolkit.")
            return
        action = actions.get(choice)
        if action is None:
            print("Invalid option. Please choose a number from 0 to 7.")
            continue
        try:
            action()
        except KeyboardInterrupt:
            print("\nModule stopped by user.")
        except PermissionError:
            print("Permission denied. Some network operations require elevated privileges.")
        except Exception as exc:
            print(f"Module error: {exc}")


if __name__ == "__main__":
    main()
