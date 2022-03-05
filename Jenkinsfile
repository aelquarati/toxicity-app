pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'build step succeed'
      }
    }

    stage('Test') {
      steps {
        sh 'pwd'
        sh 'sh -c \'pip install python3 /toxicity-app/backend/requirements.txt\''
        sh 'sh -c \'python3 -m pytest\''
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}