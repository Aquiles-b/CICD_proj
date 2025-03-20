pipeline {
    agent any

    stages {
        stage('Test') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                    dir 'jenkins_server/PyDockerImg'
                    reuseNode true
                }
            }
            steps {
                script {
                    sh '''
                        python3 calcApp/calcServer.py "127.0.0.1" "9998" &
                    '''
                    def result = sh(script: 'robot -L DEBUG -d testCalcApp/output \
                        -v SERVER_IP:127.0.0.1 -v SERVER_PORT:9998 \
                        testCalcApp/tests/calcTest.robot', returnStatus: true)

                    if (result != 0) {
                        error "Test failed!!"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '''
                        ansible-playbook -i '192.168.3.6,' -u root jenkins_server/deploy.yml
                    '''
                }
            }
        }
    }
    
    post {
        always {
            script {
                def author = sh(script: 'git log -1 --pretty=%an', returnStdout: true).trim()
                def email = sh(script: 'git log -1 --pretty=%ae', returnStdout: true).trim()

                def logFiles = "testCalcApp/output/*.html"

                def buildStatus = currentBuild.result ?: 'UNSTABLE'

                def bodyMessage = "Hello,\n\nBuild Status: ${buildStatus}\n\nHere are the test logs for the last commit by ${author}."

                emailext(
                    subject: "Test Logs for Commit by ${author}",
                    body: bodyMessage,
                    to: "${email}",
                    attachmentsPattern: logFiles
                )
            }
        }
    }
}
