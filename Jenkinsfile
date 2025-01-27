// node {
//   stage('SCM') {
//     checkout scm
//   }
//   stage('SonarQube Analysis') {
//     def scannerHome = tool 'scanner';
//     withSonarQubeEnv() {
//       sh "${scannerHome}/bin/sonar-scanner"
//     }
//   }
// }


pipeline {
    agent any

    environment {
        SCANNER_HOME = tool name: 'scanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
        DOCKER_HUB_CREDENTIALS_ID = 'dockerhub-jenkins-token'
        DOCKER_HUB_REPO = 'vettrikanth/sonarimage'
    }

    stages {
        stage('SCM') {
            steps {
                checkout scm
            }
        }

        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vettrikanth/sonar_jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def buildNumber = env.BUILD_NUMBER ?: "latest"
                    sh "docker build -t ${DOCKER_HUB_REPO}:${buildNumber} ."
                }
            }
        }

        stage('Do3. Docker-in-Docker (If Jenkins is Running in a Docker Container):cker Login') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIALS_ID, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    def buildNumber = env.BUILD_NUMBER ?: "latest"
                    sh "docker push ${DOCKER_HUB_REPO}:${buildNumber}"
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') { // Replace 'SonarQube' with your actual SonarQube server configuration name
                    sh "${SCANNER_HOME}/bin/sonar-scanner -X"
                }
            }
        }
    }
}





