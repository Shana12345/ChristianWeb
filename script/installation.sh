#!/bin/bash
source venv/bin/activate
pip3 install Flask
pip3 install flask_mysqldb
source ~/bashrc
python3 app.py
python3 /var/lib/jenkins/workspace/Pipeline1/app.py
python -m pip install pytest
pip3 install urllib3
