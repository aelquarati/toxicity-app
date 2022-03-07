pipeline {
  agent any
  stages {
    stage('Run Builds') {
      parallel {
        stage('Build Frontend') {
          steps {
            sh 'docker build --no-cache ./frontend -t frontend'
          }
        }

        stage('Build Backend') {
          steps {
            sh 'docker build --no-cache ./backend -t backend'
          }
        }

      }
    }

    stage('Deploy') {
      steps {
        script {
          sh """
          docker-compose up -d
          """
        }

      }
    }

  }
  parameters {
    string(name: 'IP', defaultValue: '192.168.1.220', description: 'VM IP')
  }
}