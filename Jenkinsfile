pipeline {

    agent any



    stages {

        stage('Development Testing') {

            steps {

                    sh 'chmod +x ./script/*' 

                    sh './script/before_installation.sh' 

                    sh './script/make_script.sh'

                    sh 'sleep 10'

                    sh './script/make_service.sh'

                }

            }



        }

    }