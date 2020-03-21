pipeline {
    agent any
        stages{
            stage('Development Environment') {
                steps {
                sh 'chmod +x ./script/*'
                    sh './script/before_installation.sh'
                    sh './script/installation.sh'
                    sh './script/make_script.sh'
                    sh 'sleep 10'
                    sh './script/make_service.sh'
                }
            }
            stage('Testing'){
                steps {
                    sh 'python3 -m pytest ./test/testing.py'
                    sh 'pip3 show coverage'
                    sh 'python3 -m coverage run -m pytest ./test/testing.py'
                    sh 'python3 -m coverage report -m'
            }
            }   
    }
}