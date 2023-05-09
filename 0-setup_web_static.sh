#!/usr/bin/env bash
# a Bash script that sets up nginx web server for the deployment of web static

sudo apt-get update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo '
<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo chown -hR ubuntu:ubuntu /data/
service nginx restart
