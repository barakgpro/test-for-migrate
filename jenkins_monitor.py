import re
import time
from datetime import datetime
import jenkins


class JenkinsJob:

    def __init__(self, name, build_num):
        self.name = name
        self.build_num = build_num


def connect_to_server(address='http://localhost:9080', user_='admin', password_='admin'):
    server_instance = jenkins.Jenkins(address, username=user_, password=password_)
    user = server_instance.get_whoami()
    version = server_instance.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
    return server_instance


def jenkins_wait(job_name):
    while True:
        temp_time = datetime.now()
        job_time = temp_time.strftime("%H:%M:%S")
        print('Jenkins build ID :', (server.get_job_info(job_name)['lastBuild']['number']), " Time:", job_time)
        time.sleep(5)
        last_completed_build_num = server.get_job_info(job_name)['lastCompletedBuild']['number']
        last_build_num = server.get_job_info(job_name)['lastBuild']['number']
        if last_completed_build_num == last_build_num:
            print(f"Last ID {last_completed_build_num}, Current ID {last_build_num}")
            break

    time.sleep(25)
    print('Job execution has been completed.')
    console_output = server.get_build_console_output(job_name, last_build_num)
    console_output = re.split('\r\n', console_output)
    return console_output


server = connect_to_server()
running_jobs = server.get_jobs()
log = jenkins_wait(running_jobs[0]['name'])
x = 0
