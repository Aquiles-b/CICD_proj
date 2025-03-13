FROM jenkins/jenkins:lts

USER root
RUN apt-get update && apt-get install -y docker.io
USER jenkins
RUN jenkins-plugin-cli --plugins docker-workflow

