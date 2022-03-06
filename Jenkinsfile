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
        sh 'sh -c \'python3 -m pytest /backend\''
      }
    }

    stage('Push ') {
      steps {
        sh '''git config --global user.email "marwane.aaziz@efrei.net"

git config --global user.name marwaneaaziz

if [ ! `git branch --list develop` ]
then git branch develop
fi
git checkout feature/TOX-5-add-backend
git merge develop'''
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}