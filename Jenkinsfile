pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'docker build -t mynewim'
        sh 'docker run mynewimage '
        sh 'sh \'pip install detoxify\''
        sh 'sh -c \'python3 backend/tests/test_prediction.py\''
        echo 'Unit test pass'
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}