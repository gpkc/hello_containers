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
                sh "docker build -t gpkc/hello_containers ."
            }
        }

        stage('Push Image') {
            when {
                branch 'master'
            }
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://registry.hub.docker.com']) {
                    sh "docker push gpkc/hello_containers"
                }
            }
        }
    }
}