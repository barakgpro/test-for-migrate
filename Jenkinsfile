pipeline {
  agent any
  stages {
    stage('print message') {
      steps {
        echo 'test123'
      }
    }

    stage('print finish') {
      steps {
        echo 'Fiinito'
      }
    }
  }
  
  post {
        always {
            script {
              sh """
              val=${BUILD_URL}/consoleText
              echo $val
              """
            }
        }
        
        failure {
            echo "fail"
        }
    }
}
