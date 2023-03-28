pipeline {
    agent any
    
    stages {
        stage('checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/sravanpeddaboina/jenkinstask.git']])
            }
        }
        
        stage('Build') {
            steps {
                script {
                    sh 'docker build . '
                }
            }
        }
        
        stage('python') {
            steps {
                   sh 'python3 1hashmap.py'
                    }
                }
        }
    }
