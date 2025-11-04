# task 2
```bash
sudo apt install mariadb-server -y
sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf
```
add port = 6002 to 
```conf
# this is only for the mysqld standalone daemon
[mysqld]
port = 6002
```
Restart mariaDB
```bash
sudo systemctl restart mariadb
sudo mysql
```
```SQL
CREATE DATABASE comp370_test;
CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s'; 
GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%';
FLUSH PRIVILEGES;
EXIT;
```
@'%' allows all ips to access, not just local

Now change bind-address = 0.0.0.0 to indicate all ips can access
```bash
sudo vim etc/mysql/mariadb.conf.d/50-server.cnf
sudo systemctl restart mariadb
```
