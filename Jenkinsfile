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
        withCredentials(bindings: [usernamePassword(credentialsId: 'gitcreds', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
          sh '''
          git remote set-url origin git@github.com:aelquarati/toxicity-app
          git config user.name marwaneaaziz
          git config user.email marwane.aaziz@efrei.net
          GIT_SSH_COMMAND="ssh -i $SSH_KEY"
          if [ ! `git branch --list develop` ]
          then git branch develop
          fi
          git checkout develop
          git commit --allow-empty -m "test withCredentials"
          git push origin develop
          '''
        }

        echo 'Push compeleted'
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}