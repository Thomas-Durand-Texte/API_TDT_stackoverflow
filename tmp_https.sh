#!/bin/bash
projectname=API_TDT_stackoverflow
sudo cp ./setup_https/${projectname}.service /etc/systemd/system 
sudo systemctl daemon-reload
sudo systemctl start ${projectname}
sudo systemctl enable ${projectname}

sudo systemctl status ${projectname}

# sudo cp ./setup_https/API_TDT_stackoverflow /etc/nginx/sites-available
# sudo ln -s /etc/nginx/sites-available/API_TDT_stackoverflow /etc/nginx/sites-enabled

