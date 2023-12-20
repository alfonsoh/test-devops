  
#!/usr/bin/python
import os
import socket
import subprocess

# need to find: username, IP address, SSID, computer name, OS version, and uptime of system
def main():
    #(sysname, nodename, release, version, machine)
    uname_info = os.uname()


    print(uname_info)
    print(f"Nodename: {uname_info[1]}")

    print(f"OS Info: {uname_info[0]} ({uname_info[2]}) - {uname_info[-1]}")

    release_path = uname_info[-2].split()[-1]
    print(f"OS Version release path: {release_path}")

    date = ' '.join(uname_info[3].split()[4:10]) 
    print(f"Date: {date}")

 #   ip_address = socket.gethostbyname(socket.gethostname())
 #   print(f"ip_address: {ip_address}")

    proc = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I"], shell=True).decode("utf-8")

    ssidOutput = proc.split()[-5]
    print(f"ssid: {ssidOutput}")


    system_software_overview = subprocess.check_output('system_profiler SPSoftwareDataType | grep -E "Time|Boot|Version|Mode|Name|Secure|Intregrity"', shell=True).decode("utf-8")
    print()
    for sys_info in system_software_overview.splitlines():
        print(sys_info.strip())

# Verify that speed test is accurate
#    print()
#    download_speed = subprocess.check_output('curl -s -S -n https://rallycurl.s3.amazonaws.com/MqdUJZGOWWgI -o /tmp/speedtest -w "time total: %{time_total}\nSpeed of Download: %{speed_download}\n" && rm /tmp/speedtest', shell=True).decode("utf-8")
#    print(download_speed)

if __name__ == '__main__':
    main()
