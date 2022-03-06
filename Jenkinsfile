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
        sh '''withCredentials([sshUserPrivateKey(credentialsId: \'github-pushes\',keyFileVariable: \'SSH_KEY\')]) {
sh \'\'\'
git remote set-url origin git@github.com:yourhttps:https://github.com/aelquarati/toxicity-app
git config user.name aelquarati
git config user.email anas.elquarati@efrei.net
GIT_SSH_COMMAND="ssh -i $SSH_KEY"
if [ ! `git branch --list develop` ]
then git branch develop
fi
git checkout develop
git commit --allow-empty -m "test withCredentials"
git push origin develop'''
        }
      }

    }
    parameters {
      string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
    }
  }