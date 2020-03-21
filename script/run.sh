#!/bin/bash

source ~/bashrc
sudo cp /var/lib/jenkins/workspace/Pipeline1/flask.service /etc/systemd/system
python3 /var/lib/jenkins/workspace/Pipeline1/app.py

