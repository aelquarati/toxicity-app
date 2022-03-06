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
        echo 'test step succed'
      }
    }

    stage('Push ') {
      steps {
        sh '''git config --global user.email "marwane.aaziz@efrei.net"

git config --global user.name marwaneaaziz

if [ ! `git branch --list develop` ]
then git branch develop
fi

git checkout develop
git add *
git commit -m "test commit"
git push origin develop'''
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}