pipeline {
    agent {
        docker {
            image 'python:3.6.4-slim'
            args '-u root:root'
        }
    }

    stages {
        stage('Requirements and Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'PYTHONPATH=. pytest'
            }
        }
    }
}