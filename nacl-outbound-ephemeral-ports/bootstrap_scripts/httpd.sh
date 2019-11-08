#!/bin/bash -xe

# Lets log everything to console for being lazy (not recommended)
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1

#install httpd
yum install httpd ec2-instance-connect -y

#enable and start httpd
systemctl enable httpd
systemctl start httpd
echo "<html><head><title> Mystikal World</title></head>" >  /var/www/html/index.html
echo "<body><br/><br/><br/><br/><br/><hr/>" >>  /var/www/html/index.html
echo "<div><center><h2>Welcome to Valaxy </h2>" >>  /var/www/html/index.html
echo "<hr/>" >>  /var/www/html/index.html
echo "<div><center><h5> $(curl http://169.254.169.254/latest/meta-data/instance-id) - $(hostname -f), $(date)</h5>" >> /var/www/html/index.html
echo "</center></div></body></html>" >>  /var/www/html/index.html
