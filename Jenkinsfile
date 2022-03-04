pipeline {
  agent {
    docker {
      image 'python 3.7'
    }

  }
  stages {
    stage('Test') {
      steps {
        sh 'sh -c \'python model_api/tests/test_prediction.py\''
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}