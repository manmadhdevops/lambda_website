stage('Deploy to Existing Lambda') {
    steps {
        withCredentials([[
            $class: 'AmazonWebServicesCredentialsBinding',
            credentialsId: 'aws-jenkins'
        ]]) {
            sh '''
            aws lambda update-function-code \
              --function-name My_WebSite \
              --zip-file fileb://function.zip \
              --region us-east-1
            '''
        }
    }
}
