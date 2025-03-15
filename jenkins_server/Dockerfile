FROM jenkins/jenkins:lts

USER root
RUN jenkins-plugin-cli --plugins docker-workflow git github

USER jenkins

