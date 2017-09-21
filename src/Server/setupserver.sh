sudo apt-get update

sudo apt-get install apache2

sudo apt-get install mysql-server

#Change the bind address in the /etc/mysql/my.cnf file to 0.0.0.0

sudo ufw enable
sudo iptables -A INPUT -p tcp -m state --state NEW,ESTABLISHED -m tcp --dport 3306 -j ACCEPT
sudo ufw reload
sudo ufw disable

sudo apt-get install php5 libapache2-mod-php5 php5-mysql phpmyadmin

sudo mysql_secure_installation


sudo sed -i 's/bind-address.*=.*127.0.0.1/bind-address=::/g' /etc/mysql/my.cnf

sudo cp pin.php /var/www/html
sudo cp plug.php /var/www/html
sudo cp lens.php /var/www/html
sudo cp session.php /var/www/html
sudo cp count.php /var/www/html
sudo cp grand.php /var/www/html
sudo cp mat.php /var/www/html

sudo rm /var/www/html/index.html

sudo a2enmod ssl

sudo service apache2 restart

sudo mkdir /etc/apache2/ssl

sudo apt-get install openssl

sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt


sudo a2ensite default-ssl.conf

sudo service apache2 restart