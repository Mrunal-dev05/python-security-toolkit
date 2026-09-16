"""Network jammer concept demo.

No deauthentication, flooding, interference, or disruption is performed.
"""


def run() -> None:
    print("\nNetwork Jammer Demo")
    print("Jamming/disruption can affect availability of other devices.")
    print("This safe demo models the concept without transmitting disruptive traffic.")
    duration = input("Simulation duration in seconds (1-30): ").strip()
    try:
        seconds = int(duration)
        if not 1 <= seconds <= 30:
            raise ValueError
    except ValueError:
        print("Enter a whole number from 1 to 30.")
        return
    print(f"Simulated network availability test for {seconds} seconds completed.")
