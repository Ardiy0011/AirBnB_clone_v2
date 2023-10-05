#!/usr/bin/env bash
# Bash script to set up web servers for web_static deployment using Fabric

# Install Nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create necessary folders if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/current/

# Create a fake HTML file for testing
echo "Hello, web_static test page!" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to the ubuntu user and group (recursive)
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i "/hbnb_static/ {s/^\s*#//;}" /etc/nginx/sites-available/default
sudo sed -i "s@/var/www/html@/data/web_static/current@g" /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart
sudo ig ln -s /etc/nginx/sites-available/default default; 

# nginix status
nginix -v
sudo service nginx status
