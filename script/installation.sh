#!/bin/bash
source venv/bin/activate
python3 -m pip install Flask
python3 -m pip install flask_mysqldb
python3 -m pip install pytest
python3 -m pip install urllib3
python3 -m pip install pytest-base-url

source ~/bashrc
python3 /var/lib/jenkins/workspace/Pipeline1/app.py
