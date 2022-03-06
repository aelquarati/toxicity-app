pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'pip install pytest'
        echo 'build step succeed'
      }
    }

    stage('Test') {
      steps {
        echo 'Test stage completed'
      }
    }

    stage('Push ') {
      agent any
      steps {
        echo 'Push compeleted'
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}