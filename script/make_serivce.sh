#!/bin/bash

sudo cp /var/lib/jenkins/workspace/Pipeline/flask.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable flask.service

sudo systemctl stop flask.service
sudo systemctl start flask.service