  
#!/usr/bin/python
import os
import socket
import subprocess
import csv
import sys
 

system_software_overview = subprocess.check_output('system_profiler SPSoftwareDataType | grep -E "Time|Boot|Version|Mode|Name|Secure|Intregrity"', shell=True).decode("utf-8").splitlines()
download_speed = subprocess.check_output('curl -s -S -n https://rallycurl.s3.amazonaws.com/MqdUJZGOWWgI -o /tmp/speedtest -w "time total: %{time_total}\nSpeed of Download: %{speed_download}\n" && rm /tmp/speedtest', shell=True).decode("utf-8")
SSID = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I"], shell=True).decode("utf-8").split()[-5]
OS_Info = f'{os.uname()[0]} ({os.uname()[2]}) - {os.uname()[-1]}'
print(f"Nodename: {os.uname()[1]}\nOS Info: {OS_Info}\nOS Version release path: {os.uname()[-2].split()[-1]}\nDate: {' '.join(os.uname()[3].split()[4:10])}\nip_address: {socket.gethostbyname(socket.gethostname())}\nssid: {SSID}\n")

print(f'\n{download_speed}') 

for sys_info in system_software_overview:
    print(sys_info.strip())

args = sys.argv[1:]
if args[0] == "--csv":
    with open('mac_info.csv', 'w', newline = '') as f:
        fieldnames = ['Nodename', 'OS Info', 'OS Version Release Path','Date','Ip_address','ssid']
        writing = csv.DictWriter(f, fieldnames=fieldnames)
        writing.writeheader()
        writing.writerow({'Nodename':os.uname()[1], 'OS Info':OS_Info, 'OS Version Release Path':os.uname()[-2].split()[-1],'Date':' '.join(os.uname()[3].split()[4:10]),'Ip_address':socket.gethostbyname(socket.gethostname()),'ssid':SSID  })

elif args[0] == "--json":
    pass
