import requests


def get_public_ip():
    """Fetch the current public IP address."""
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        return response.json()["ip"]
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None


def main():
    print("Checking VPN status...")

    # Get public IP address before enabling VPN
    ip_before = get_public_ip()
    if ip_before is None:
        print("Failed to retrieve the initial IP address. Exiting.")
        return

    print(f"Public IP before enabling VPN: {ip_before}")
    input("Connect to your VPN and press Enter to continue...")

    # Get public IP address after enabling VPN
    ip_after = get_public_ip()
    if ip_after is None:
        print("Failed to retrieve the IP address after enabling VPN. Exiting.")
        return

    print(f"Public IP after enabling VPN: {ip_after}")

    # Compare IPs
    if ip_before == ip_after:
        print("VPN is NOT working. The IP address has not changed.")
    else:
        print("VPN is working. The IP address has changed.")


if __name__ == "__main__":
    main()
