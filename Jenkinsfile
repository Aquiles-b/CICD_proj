pipeline {
    agent {
        docker {
            image 'python:latest'
            label 'docker'
        }
    }
    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building inside a Python Docker container'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Running tests inside a Python Docker container'
                }
            }
        }
    }
}

