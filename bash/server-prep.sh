while true; do
    read -p "Do you wish to install the server software? (y/n) " yn
    case $yn in
        [Yy]* ) sudo apt update -y && sudo apt install -y apache2 mysql-server-8.0 postgresql-server-dev-all gnupg curl && curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor && echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list && sudo apt update && sleep 10 && sudo apt install -y mongodb-org; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done