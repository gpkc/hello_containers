pipeline {
    agent none
    stages {
        stage('Requirements and Test') {
            agent {
                docker {
                    image 'python:3.6.4-slim'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'PYTHONPATH=. pytest'
            }
        }
    }
}