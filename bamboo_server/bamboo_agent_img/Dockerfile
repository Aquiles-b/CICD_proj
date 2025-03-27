FROM atlassian/bamboo-agent-base

RUN apt-get update && apt-get install -y ansible ssh python3 python3-pip
RUN pip install robotframework pexpect --break-system-packages
