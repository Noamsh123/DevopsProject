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
        stage ("publish release"){
            when{
                expression{
                    return GIT_BRANCH.contains('main')
                }
            }
            steps{
                script{
                    // sh '''
                    //     echo ${BUILD_NUMBER} | cut -d '/' -f 2
                    // '''
                    // version=sh (script: "echo $(echo ${GIT_BRANCH} | cut -d '/' -f 2)",
                    // returnStdout: true).trim()
                    def version=sh "echo $(echo ${GIT_BRANCH} | cut -d '/' -f 2)"

                    docker.withRegistry("https://644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo","ecr:eu-west-2:my-aws-access"){
                        // sh "docker tag shamir-repo:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo:latest"
                        sh "docker tag shamir-repo:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo:${version}.${BUILD_NUMBER}"
                        sh "docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/shamir-repo:${version}.${BUILD_NUMBER}"
                    }
                }
            }
            
        }


        stage ("publish"){
            when{
                expression{
                    return GIT_BRANCH.contains('main')
                }
            }
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
        stage("deploy"){
            when{
                expression{
                    return GIT_BRANCH.contains('main')
                }
            }
            steps {
                sleep 10
                sh "./deploy.sh ${BUILD_NUMBER}"
            }
        }
    }
}