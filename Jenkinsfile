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
        sh '''sshagent([\'github_jenkins\']) {
        sh """
          git remote set-url origin git@github.com:aelquarati/toxicity-app
          git config user.name marwaneaaziz
          git config user.email marwane.aaziz@efrei.net

          git checkout develop
          git commit --allow-empty -m "test withCredentials"
          git push origin develop
 """
         }'''
        }
      }

    }
    parameters {
      string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
    }
  }