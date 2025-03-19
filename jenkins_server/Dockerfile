FROM jenkins/jenkins:lts

USER root
COPY deploy.yml .
RUN apt-get update && apt-get install -y docker.io ansible ssh
RUN jenkins-plugin-cli --plugins docker-workflow git github email-ext

USER jenkins
