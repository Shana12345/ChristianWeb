#!/bin/bash
sudo apt update -y
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python3-venv -y
sudo apt-get install libmysqlclient-dev -y
python3 -m venv venv
sudo systemctl daemon-reload
sudo cp /var/lib/jenkins/workspace/Pipeline1/script/flask.service/run.sh /etc/systemd/system
