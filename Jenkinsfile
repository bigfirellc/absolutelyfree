pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker compose build absolutelyfree'
            }
        }
        stage('Test') {
            steps {
                sh 'docker compose run absolutelyfree python manage.py test'
            } 
        }
        stage('Run') {
            steps {
                sh 'docker compose up -d absolutelyfree'
            } 
        }            
    }
}