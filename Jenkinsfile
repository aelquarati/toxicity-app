pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'docker compose up -d .'
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}