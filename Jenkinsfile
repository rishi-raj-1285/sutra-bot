pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Environment') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Validate Application') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t sutra-bot:jenkins .'
            }
        }
    }
}