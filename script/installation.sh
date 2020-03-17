#!/bin/bash
source venv/bin/activate
pip3 install Flask
pip3 install flask_mysqldb
python3 app.py
python3 -m pip install pytest
python3 -m pip install urllib3
python3 -m pip install pytest-base-url

source ~/.bashrc
python3 /var/lib/jenkins/workspace/Pipeline1/app.py
