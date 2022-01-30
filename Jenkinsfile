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
              def logContent = Jenkins.getInstance()
                .getItemByFullName(env.JOB_NAME)
                .getBuildByNumber(
                    Integer.parseInt(env.BUILD_NUMBER))
                .logFile.text
              // copy the log in the job's own workspace
              // writeFile file: "buildlog.txt", text: logContent
              echo $logContent
            }
        }
        
        failure {
            echo "fail"
        }
    }
}
