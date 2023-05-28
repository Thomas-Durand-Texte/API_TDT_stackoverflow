#!/bin/bash
sudo cp ./setup_https/API_TDT_stackoverflow.service /etc/systemd/system 
sudo systemctl daemon-reload
sudo systemctl start API_TDT_stackoverflow
sudo systemctl enable API_TDT_stackoverflow

sudo systemctl status API_TDT_stackoverflow
