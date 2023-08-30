pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                bat 'npm install'
            }
        }
        
        stage('Deploy') {
            steps {
                // Use the 'start' command to run the kubectl apply commands in the background
                bat 'start kubectl apply -f kubernetes/deployment.yaml'
                bat 'start kubectl apply -f kubernetes/service.yaml'
            }
        }
    }
}
