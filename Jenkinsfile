pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh 'sudo systemct1 start flask.service'
                sh 'sudo systemct1 status flask.service'
                sh 'sudo systemct1 restart flask.service'
            }
        }
         stage('Testing'){
            steps {
                    sh './coverage/testing.sh'
                    sh 'python -m pytest ./test/testing.py'
            }
        }
    }
}