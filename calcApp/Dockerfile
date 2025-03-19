FROM python:latest

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y openssh-server

RUN echo 'root:root' | chpasswd

RUN sed -i 's/#PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
