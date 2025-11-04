# Task 1
```bash
sudo apt update
sudo apt install apache2 -y
```

Change listen 80 to listen 8008 and change virtual host to 8008
```bash
sudo vim /etc/apache2/ports.conf 
sudo vim /etc/apache2/sites-available/000-default.conf
```

Default web root is /var/www/html - we must change it
```bash
sudo vim var/www/html/comp370_hw3.txt
```

Update the Security Group to allow port 8008
Go to AWS -> instances -> comp 370 -> Security -> security groups -> edit inbound rules 
-> add a custom TCP rule with port range 8008 and source 0.0.0.0/0

Restart apache and test
```bash
sudo systemctl restart apache2
```
Visit http://15.223.85.148:8008/comp370_hw3.txt

After installing DBeaver we connect to our data base yb specifying:
- hostname: public ip
- root user: comp370
- database name: comp370_test
- root user pwd: sunglasses
