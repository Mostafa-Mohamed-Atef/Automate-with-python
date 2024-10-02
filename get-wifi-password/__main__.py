import subprocess
import os
import qrcode
from PIL import Image
def get_wifi_password():
    try:
        # Get the active SSID using nmcli command
        ssid = subprocess.check_output(["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"]).decode('utf-8').strip()
        # Extract the SSID from the output
        ssid = [line.split(":")[1] for line in ssid.split("\n") if "yes" in line][0]

        # Set the directory where network connection files are stored
        connection_dir = "/etc/NetworkManager/system-connections/"
        # List all files in the connection directory
        connection_files = os.listdir(connection_dir)
        # Find the file that matches the current SSID
        connection_file = next((f for f in connection_files if ssid in f), None)

        # If no matching file is found, print an error and return
        if not connection_file:
            print(f"Could not find connection file for SSID: {ssid}")
            return

        # Use sudo to read the password from the connection file
        password = subprocess.check_output(["sudo", "grep", "psk=", f"{connection_dir}{connection_file}"]).decode('utf-8').strip()
        # Extract the password from the output
        password = password.split("=")[1]

        # Print the SSID and password
        print(f"SSID: {ssid}")
        print(f"Password: {password}")
        return password
    except subprocess.CalledProcessError as e:
        # Handle errors when executing subprocess commands
        print(f"Error executing command: {e}")
    except IndexError:
        # Handle the case when no active Wi-Fi connection is found
        print("No active Wi-Fi connection found.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

def generate_qrcode(password):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(password)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.show()


if __name__ == "__main__":
    password = get_wifi_password()
    qr = input("Generate qr code?\n").lower()
    if qr == 'y': generate_qrcode(password)
