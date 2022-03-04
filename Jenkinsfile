pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'bat \'python model_api/tests/test_prediction.py\''
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}