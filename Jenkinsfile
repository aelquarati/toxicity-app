pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build ./backend -t mynewim'
        sh 'docker run mynewim'
        echo 'build step succeed'
      }
    }

    stage('Test') {
      steps {
        sh 'sh \'pip install detoxify\''
        sh 'sh -c \'python3 backend/tests/test_prediction.py\''
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}