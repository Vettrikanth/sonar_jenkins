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
        stages {
        stage('Test Docker') {
            steps {
                sh 'docker --version'
            }
        }
    }
        stage('Build Docker Image') {
            steps {
                script {
                    def buildNumber = env.BUILD_NUMBER ?: "latest"
                    sh "docker build -t sonarimage:${buildNumber} ."
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
