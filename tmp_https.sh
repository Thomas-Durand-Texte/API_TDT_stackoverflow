#!/bin/bash
projectname=API_TDT_stackoverflow

sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools nginx


sudo cp ./setup_https/${projectname}.service /etc/systemd/system 
sudo systemctl daemon-reload
sudo systemctl start ${projectname}
sudo systemctl enable ${projectname}

sudo systemctl status ${projectname}

# sudo cp ./setup_https/${projectname} /etc/nginx/sites-available
# sudo ln -sf /etc/nginx/sites-available/${projectname} /etc/nginx/sites-enabled

# sudo nginx -t
# sudo systemctl restart nginx
# sudo ufw allow 'Nginx HTTP'



