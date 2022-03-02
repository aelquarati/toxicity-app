def buildImage(name,path){
    return docker.build("${name}:latest", "${path}")
}

pipeline {
    agent any
    parameters {
        string (
                name : 'IP',
                defaultValue: '192.168.1.220',
                description: 'VM IP')
    }

    stages {
        stage('Run Builds'){
            parallel {
                stage('Build Frontend') {
                    steps {
                        script{
                              /**build Frontend image**/
                              dir('frontend'){
                                echo "BACKENDHOST=${IP} > .env.local" 
                                buildImage('frontend','.')
                              }
                        }
        
                    }
                }

                stage('Build Backend') {
                    steps {
                        script{
                              /**build Python image**/
                              dir('api'){
                                buildImage('api','.')
                              }
                        }
        
                    }
                }
            }
        }

        stage('Deploy'){
            
            steps{
                script{

                    sh """
                    docker-compose up -d
                    """
                }
            }
        }
    }
}

