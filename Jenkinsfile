pipeline {
  agent {
    docker {
      image 'python:3.7'
    }

  }
  stages {
    stage('Test') {
      steps {
        sh 'sh \'pip3 install detoxify\''
        sh 'sh -c \'python3 backend/tests/test_prediction.py\''
        echo 'Unit test pass'
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}