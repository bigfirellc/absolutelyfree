pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            dir 'build'
            label 'absolutelyfree'
        }
    }   
    stages {
        stage('Test') {
            environment { 
                SECRET_KEY = '5d+hngv=)(xd@qt3swsota_y!=2r-r%h5c_=t$v%o0d&$_cpig'
                DEBUG = 'TRUE'
                USE_S3 = 'FALSE'
            }            
            steps {
                sh 'python manage.py check'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
                sh 'python manage.py test'
            } 
        }        
    }
}