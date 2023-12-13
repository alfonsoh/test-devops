import os
import subprocess

# Check system uptime

system_uptime = os.popen ('uptime') .read()[:-1]
print (system_uptime)

# Install homebrew

os.system("/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"")

# Configure system to run brew install commands

os.system("(echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> /Users/admin/.zprofile"")

os.system("eval "$(/usr/local/bin/brew shellenv)"")

# Insert sleep or wait command

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

# Install or upgrade required packages

os.system("brew install --cask firefox")
os.system("brew install --cask zoom")
os.system("brew install --cask slack")
os.system("brew install --cask google-chrome")
os.system("brew install --cask appcleaner")
os.system("brew install --cask the-unarchiver")
os.system("brew install --cask gimp")

# Reboot system after updates and packages
os.system("shutdown -r now")
