pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
               sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh 'sudo systemct1 enable flask.service'
                sh 'sudo systemct1 start flask.service'
                sh 'sudo systemct1 status flask.service'
                sh 'sleep 13'
            }
        }
        stage('Testing'){
            steps {
                sh 'pytest ./test/testing.py'
                sh 'pip3 show coverage'
                sh 'coverage run -m pytest -m  ./test/testing.py'
                sh 'coverage report -m'
        }
    }
}