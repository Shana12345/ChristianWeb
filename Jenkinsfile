pipeline {
    agent any
        stages{
            stage('Development Environment') {
                steps {
                sh 'chmod +x ./script/*'
                    sh './script/before_installation.sh'
                    sh './script/installation.sh'
                    sh 'sudo systemctl enable flask.service'
                    sh 'sudo systemctl start flask.service'
                    sh 'sudo systemctl status flask.service'
                }
            }
            stage('Testing'){
                steps {
                    sh 'python3 -m pytest ./test/testing.py'
                    sh 'pip3 install coverage'
                    sh 'coverage run --source estimator,database -m pytest'
                    sh 'pip3 show coverage'
                    sh 'python3 -m coverage run -m pytest ./test/testing.py'
                    sh 'python3 -m coverage report -m'
            }
            }   
    }
}