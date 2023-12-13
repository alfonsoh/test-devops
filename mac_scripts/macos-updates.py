import os
import subprocess
import platform
import time

SECONDS_TO_DAYS = 1 / 86400

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
    reboot = False;
    
    # Check system uptime
    uptime_days = time.monotonic() * SECONDS_TO_DAYS
    print(f'uptime: {uptime_days} days')
    if (uptime_days > 10):
        reboot = True
    
    version, _, architecture = platform.mac_ver()
    print(f'version: {version}')
    print(f'architecture: {architecture}')
    
    if int(version.split('.')[0]) < 14:
        check_for_updates()
        install_updates()
        reboot = True
    
    # Install homebrew
    
    os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
    
    # Configure system to run brew install commands
    
    os.system("(echo; echo 'eval \"$(/usr/local/bin/brew shellenv)\"') >> /Users/admin/.zprofile\"")
    
    os.system("eval \"$(/usr/local/bin/brew shellenv)\"")

    # Install or upgrade required packages
    
    os.system("brew install --cask firefox")
    os.system("brew install --cask zoom")
    os.system("brew install --cask slack")
    os.system("brew install --cask google-chrome")
    os.system("brew install --cask appcleaner")
    os.system("brew install --cask the-unarchiver")
    os.system("brew install --cask gimp")

    if reboot:
        # Reboot system after updates and packages
        os.system("shutdown -r now")
