while true; do
    read -p "Do you wish to install the server software? (y/n) " yn
    case $yn in
        [Yy]* ) sudo apt update -y && sudo apt install -y apache2; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done
