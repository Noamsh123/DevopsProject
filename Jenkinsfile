pipeline {
    agent any


    stages{
        stage ("checkout") {
            steps{
                deleteDir()
                checkout scm
                // echo ${BUILD_NUMBER}
                sh "echo ${BUILD_NUMBER}"
            }
        }

        stage ('build') {
            steps{
                sh "docker build -t shamir-repo ."
                // app = docker.build("shamir-repo")
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

        stage ("push to ecr"){
            steps {
                script{
                    docker.withRegistry("https://644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo","ecr:eu-west-2:my-aws-access"){
                        // sh "docker tag shamir-repo:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo:latest"
                        sh "docker tag shamir-repo:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo:1.1.${BUILD_NUMBER}"
                        sh "docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo:1.1.${BUILD_NUMBER}"
                    }
                }
            }
        }



    }
}