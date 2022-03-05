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
        sh 'sh -c \'python3 /backend/tests/test_prediction.py\''
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}