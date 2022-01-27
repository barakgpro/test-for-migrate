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
    post {
       script {
          sh '''#!/bin/tcsh -f
          val=${BUILD_URL}/consoleText
          echo $val
        }
    }
  }
}
