import jenkins

server = jenkins.Jenkins('http://localhost:9080', username='admin', password='admin')
server.create_job('test_from_python', jenkins.EMPTY_CONFIG_XML)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
x=0