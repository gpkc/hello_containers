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

                    sh "docker login -u ${env.HUBLOGIN} -p ${env.HUBPASS}"
                    sh "docker push gpkc/hello_containers:latest"
                }
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'azure-registry',
                    passwordVariable: 'REGPASS',
                    usernameVariable: 'REGLOGIN']]) {

                    sh "docker login -u ${env.REGLOGIN} -p ${env.REGPASS} hellocontainersregistry.azurecr.io"
                    sh "docker tag gpkc/hello_containers:latest hellocontainersregistry.azurecr.io/${env.REGLOGIN}/hello_containers:latest"
                    sh "docker push hellocontainersregistry.azurecr.io/${env.REGLOGIN}/hello_containers:latest"
                }
            }
        }
    }
}