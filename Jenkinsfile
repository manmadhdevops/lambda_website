pipeline {
    agent any

    environment {
        FUNCTION_NAME = "My_WebSite"
        REGION = "us-east-1"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Package Lambda Code') {
            steps {
                sh '''
                rm -f function.zip
                zip -r function.zip lambda_function.py
                '''
            }
        }

        stage('Deploy to Existing Lambda') {
            steps {
                sh '''
                aws lambda update-function-code \
                  --function-name $FUNCTION_NAME \
                  --zip-file fileb://function.zip \
                  --region $REGION
                '''
            }
        }
    }
}
