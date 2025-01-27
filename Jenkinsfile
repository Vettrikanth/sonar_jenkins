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

node {
  stage('SCM') {
    checkout scm
  }

  stage('Git checkout')
  {
  steps
    {
      git branch: 'main', url: 'https://github.com/Vettrikanth/sonar_jenkins.git'
    }
  }
  

  stage ('Build Docker image')
  {
  steps
    {
      sh 'docker.build("sonarimage"+"$BUILD_NUMBER")'
    }
    }

  
  stage('SonarQube Analysis') {
    def scannerHome = tool 'scanner'; // Ensure 'scanner' matches the configured name in Jenkins
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner -X"
    }
  }
  
  
  
}

