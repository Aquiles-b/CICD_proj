FROM jenkins/jenkins:lts

USER root
RUN apt-get update && apt-get install -y docker.io
RUN jenkins-plugin-cli --plugins docker-workflow git github

USER jenkins
