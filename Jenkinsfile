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

    stage('parse log') {
      steps {
        script {
          echo "in post###"
          def logContent = Jenkins.getInstance()
          .getItemByFullName(env.JOB_NAME)
          .getBuildByNumber(
            Integer.parseInt(env.BUILD_NUMBER))
            .logFile.text
            // copy the log in the job's own workspace
            // writeFile file: "buildlog.txt", text: logContent
            echo logContent.contains("Fii")
          }

        }
      }

    }
  }
