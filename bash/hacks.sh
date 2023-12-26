while true; do
    read -p "Do you want to run a Samba Exploit (y/n) " yn
    case $yn in
        [Yy]* ) msfconsole && read -p "What is the target IP? " rhost && set rhosts $rhost && exploit ; break;;
    esac
done