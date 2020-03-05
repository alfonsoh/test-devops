import os
import socket
import subprocess
import platform
import sys

user_info = os.uname()
computer_name = user_info[1]
ip_address = socket.gethostbyname(socket.gethostname())
uptime = subprocess.Popen("uptime")

username = os.getlogin()

ssid = subprocess.run(["/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport", "-I"], capture_output=True)

os_version = subprocess.run(["sw_vers", "-productVersion"], capture_output=True)

print(user_info)
print(computer_name)
print(ip_address)
print(uptime)
print(username)
print(ssid)
print(os_version)
