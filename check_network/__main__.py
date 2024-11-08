import subprocess

def check_network():
    try:
        # Ping Google to check connectivity
        response = subprocess.run(
            ["ping", "-c", "1", "google.com"],
            stdout=subprocess.DEVNULL,  # Hide output
            stderr=subprocess.DEVNULL
        )
        if response.returncode == 0:
            print("Network is working!")
        else:
            print("Network is down.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_network()
