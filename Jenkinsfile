pipeline {
    agent any


    stages{
        stage ("checkout") {
            steps{
                deleteDir()
                checkout scm
            }
        }

        stage ('build') {
            steps{
                sh "docker build -t shamir-repo ."
            }
        }

        stage ('run and test'){
            steps{
                sh "docker-compose up -d"
                sleep 16
                sh "bash tests/e2e.sh"
            }
            post{
                always{
                    sh "docker-compose down"
                }
            }
        }



    }
}