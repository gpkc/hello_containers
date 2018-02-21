pipeline {
    agent none

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
            agent {
                docker {
                    image 'docker'
                    args '-u root:root'
                }
            }
            steps {
                sh "docker build -t gpkc/hello_containers ."
            }
        }
    }
}