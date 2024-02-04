#!/usr/bin/env bash
#server deploment of web_static

apt-get -y update

# install nginx if it's not already installed

if ! command -v nginx > /dev/null; then
    apt-get install -y nginx
fi

ufw allow 'Nginx HTTP'

# create the folders
mkdir -p /data/web_static/shared/  /data/web_static/releases/test/

echo " 
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html 

# create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership
chown -R ubuntu /data/
chgrp -R ubuntu /data/


mkdir -p /var/www/html
echo "Hello World!" > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/404.html

printf %s "server{
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$hostname;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.google.com;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-available/default

nginx -t
service nginx restart
