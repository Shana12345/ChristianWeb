#!/bin/bash
sudo cp /var/lib/jenkins/workspace/Pipeline1/script/run.sh /etc/systemd/system
sudo apt update -y
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python3-venv -y
sudo apt-get install libmysqlclient-dev -y
python3 -m venv venv
sudo systemctl daemon-reload

