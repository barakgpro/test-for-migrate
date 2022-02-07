pipeline {
  agent any
  stages {
    stage('print message') {
      steps {
        
        echo 'step 1'
        echo 'sfr-36e9424f-3664-4e80-bee9-1c227a1d1c31'
        echo 'sfr-36e9424f-3664-4e80-bee9-1c227a1d1c31'
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
          sh ("""
          # Set workspace directory
          set work_area = "/home/barakg/temp/"
          mkdir $work_area
          echo "\\033[32m"-INFO- work area $work_area  "\\033[m"

          setenv PTOOLS_CONFIG "/data/tools_cfgs"
          setenv PTOOLS "/data/tools"
          source /data/tools/proteus_psetup/latest/psetup.csh -work_area $work_area
          setenv WORK $work_area
          setenv PROTEUS_EDA "$WORKSPACE"
          setenv PROTEUS_TOOL "$WORKSPACE/proteus5.0"
          echo "\\033[32m"-INFO- PROTEUS_EDA = $PROTEUS_EDA"\\033[m"
          echo "\\033[32m"-INFO- PROTEUS_TOOL = $PROTEUS_TOOL"\\033[m"
        
          setenv PROTEUS_SFM /data/tools/proteus_sfm/v3.0.0_pre_release_2
          """)
              
          def logContent = Jenkins.getInstance()
          .getItemByFullName(env.JOB_NAME)
          .getBuildByNumber(
            Integer.parseInt(env.BUILD_NUMBER))
            .logFile.text

            def curr_idx = 0
            while (true) {
              try {
                def idx1 = logContent.indexOf('sfr-', curr_idx)   
                def idx2 = logContent.indexOf('\n', idx1)
                def sfr_id = logContent.substring(idx1, idx2)
                echo "removing ${sfr_id}"
                sh 'sfm remove --uid $sfr_id'
                curr_idx = idx2
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
