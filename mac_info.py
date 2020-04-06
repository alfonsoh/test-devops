  
#!/usr/bin/python
import os
import socket
import subprocess

# need to find: username, IP address, SSID, computer name, OS version, and uptime of system
def main():
    #(sysname, nodename, release, version, machine)
    uname_info = os.uname()


    print(uname_info)
    print("Nodename: %s" %(uname_info[1]))
    print("OS Info: %s (%s) - %s" % (uname_info[0], uname_info[2], uname_info[-1]))

    release_path = uname_info[-2].split()[-1]
    print("OS Version release path: %s" % (release_path))

    date = ' '.join(uname_info[3].split()[4:10]) 
    print("Date: %s" %(date))

    ip_address = socket.gethostbyname(socket.gethostname())
    print("ip_address: %s" %(ip_address))

    username = os.getlogin()
    print("username: %s" %(username))

    proc = subprocess.Popen(["/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport", "-I"], stdout=subprocess.PIPE)

    ssidOutput = proc.stdout.read().split()[-5]
    print("ssid: %s" %(ssidOutput))

    os.system("/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | awk -F: '/ SSID/{print $2}'")

    # uptime = subprocess.Popen("uptime")
    # print("uptime: %s" %(uptime))

    uptime = subprocess.Popen("uptime", stdout=subprocess.PIPE)
    uptime_output = uptime.stdout.read()
    uptimeDays = str(uptime_output).split(' ')
    uptimeShortArr = uptimeDays[3:5]
    uptimeShortArr.append(uptimeDays[6])

    print(uptimeShortArr)


    uptimeJoined = ' '.join(uptimeShortArr)
    print("uptime: %s hrs:mins" %(uptimeJoined))


if __name__ == '__main__':
    main()
