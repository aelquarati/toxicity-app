pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'python37 pip3 install pytest Detoxify torch'
        echo 'build step succeed'
      }
    }

    stage('Test') {
      steps {
        sh 'sh -c \'python3 -m pytest\''
        echo 'Test stage completed'
      }
    }

    stage('Push ') {
      agent any
      steps {
        sh '''          git remote set-url origin git@github.com:aelquarati/toxicity-app
          git checkout develop
          git commit --allow-empty -m "test withCredentials"
          git push origin develop
 '''
        echo 'Push to develop '
      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}