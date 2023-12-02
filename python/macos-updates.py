import os
import subprocess

def check_for_updates():
    try:
        # Run the softwareupdate command to check for updates
        subprocess.run(['softwareupdate', '--list'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error checking for updates: {e}")

def install_updates():
    try:
        # Run the softwareupdate command to install updates
        subprocess.run(['softwareupdate', '-ia'], check=True)
        print("Updates installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing updates: {e}")

if __name__ == "__main__":
    print("Checking for updates...")
    check_for_updates()

    install_updates()
os.system("shutdown -r now")
