pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            dir 'jenkins_server/PyDockerImg'
            args '-u root'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                    python3 calcApp/calcServer.py "0.0.0.0" "9998" &
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    robot -L DEBUG -d testCalcApp/output --variable SERVER_IP=0.0.0.0 --variable SERVER_PORT=9998 \
                    testCalcApp/tests/calcTest.robot 
                '''
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '''
                        ssh root@192.168.3.6
                    '''
                }
            }
        }
    }
}
