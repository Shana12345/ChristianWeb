pipeline {
    agent any
        stages{
            stage('Development Environment') {
                steps {
                sh 'chmod +x ./script/*'
                    sh './script/before_installation.sh'
                    sh 'sudo systemctl enable flask.service'
                    sh 'sudo systemctl start flask.service'
                    sh 'sudo systemctl status flask.service'
                    sh 'sleep 13'
                }
            }
            stage('Testing'){
                steps {
                    sh 'pytest ./test/testing.py'
                    sh 'pip3 show coverage'
                    sh 'python3 -m coverage run -m pytest ./test/testing.py'
                    sh 'python3 -m coverage report -m'
            }
            }   
    }
}