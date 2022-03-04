pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'sh \'pip install detoxify\''
        sh 'sh -c \'python3 backend/tests/test_prediction.py\''
        echo 'Unit test pass'
        sh 'docker run my image -d'
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}