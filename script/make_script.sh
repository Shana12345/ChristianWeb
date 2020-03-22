#!/bin/bash

source /var/lib/jenkins/bashrc
source /var/lib/jenkins/workspace/Pipeline1/venv/bin/activate

/var/lib/jenkins/workspace/Pipeline1/coverage.sh run -m pytest /var/lib/jenkins/workspace/Pipeline1/test/testing.py
/var/lib/jenkins/workspace/Pipeline1/coverage.sh