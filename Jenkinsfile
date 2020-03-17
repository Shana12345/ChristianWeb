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
             
            }
        }
         stage('Testing'){
            steps {
                    sh 'chmod +x ./coverage/*'
                    sh './coverage/testing.sh'
             
            }
        }
    }
}