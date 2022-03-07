pipeline {
  agent any
  stages {
    stage('Run Builds') {
      parallel {
        stage('Build Frontend') {
          steps {
            script {
              dir('frontend'){
                echo "BACKENDHOST=${IP} > .env.local"
                buildImage('frontend','.')
              }
            }

          }
        }

        stage('Build Backend') {
          steps {
            script {
              dir('api'){
                buildImage('backend','.')
              }
            }

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