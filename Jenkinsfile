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
        sh 'sh -c \'pip install "/var/jenkins_home/workspace/ty-app_feature_TOX-5-add-backend/toxicity-app/backend/requirements.txt"\''
        sh 'sh -c \'python3 -m pytest\''
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}