pipeline {
    agent any

    stages {
        stage('Requirements and Test') {
            agent {
                docker {
                    image 'python:3.6.4-slim'
                    args '-u root:root'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'PYTHONPATH=. pytest'
            }
        }

        stage('Building Docker Image') {
            steps {
                sh "docker build -t gpkc/hello_containers:latest ."
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'docker-hub-credentials',
                    passwordVariable: 'HUBPASS',
                    usernameVariable: 'HUBLOGIN']]) {
                    
                    docker login -u ${env.HUBLOGIN} -p ${env.HUBPASS}
                    sh "docker push gpkc/hello_containers:latest"
                }
            }
        }
    }
}