#!/bin/bash

echo -n "Would you like to install a Web Server or Database Server?... Enter 1 for Apache, 2 for MySQL, 3 for Postgres, or 4 for MongoDB: "
read VAR
	if [[ $VAR = 1 ]]; then
      		sudo apt update && sleep 10 sudo apt install apache2 -y
	fi
	if [[ $VAR = 2 ]]; then
    		sudo apt install mysql-server-8.0 -y
	fi
	if [[ $VAR = 3 ]]; then
    		sudo apt install postgresql-server-dev-all -y
	fi
	if [[ $VAR = 4 ]]; then
                sudo apt install mongodb-org -y
	fi
