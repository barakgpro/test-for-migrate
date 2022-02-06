pipeline {
  agent any
  stages {
    stage('print message') {
      steps {
        echo 'step 1'
        echo 'sfr-12345-12345-12345-12345-12345'
        echo 'sfr-12345-12345-12345-12345-12346'
        echo 'sfr-12345-12345-12345-12345-12347'
      }
    }

    stage('print finish') {
      steps {
        echo 'step 2'
        echo 'sfr-12345-12345-12345-12345-12345'
        echo 'steps finish'
      }
    }
    }

post{
    always {
        script {
          def logContent = Jenkins.getInstance()
          .getItemByFullName(env.JOB_NAME)
          .getBuildByNumber(
            Integer.parseInt(env.BUILD_NUMBER))
            .logFile.text
            // copy the log in the job's own workspace
            // writeFile file: "buildlog.txt", text: logContent
            // def idx1 = logContent.indexOf("Fii")
            // def idx2 = logContent.indexOf("to", idx1)

            while (true) {
              try {
                // test
                curr_idx = 0
                def idx1 = logContent.indexOf("sfr-", curr_idx)   
                def idx2 = logContent.indexOf("\n", idx1)
                def sfr_id = logContent.substring(idx1, idx2)
                echo 'removing ${sfr_id}' 
                curr_idx = idx2

                // actual code
                // def idx1 = logContent.indexOf("sfr-")   
                // def idx2 = logContent.indexOf("\n", idx1)
                // def sfr_id = logContent.substring(idx1, idx2)
                // sfm remove --$sfr_id
                
              }
              catch(Exception ex) {
                echo "all spots closed" 
                break
              }

              
            }
            

          }
    }
}
}
