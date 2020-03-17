pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh './script/installation.sh'
                sh 'sudo systemct1 enable flask.service'
                sh 'sudo systemct1 start flask.service'
                sh 'sudo systemct1 status flask.service'
                sh 'sudo systemct1 restart flask.service'
            }
        }
        stage('Testing'){
            steps {
                sh 'pytest ./test/testing.py'
            }
        }
    }
}