#!/bin/bash

service ssh start
python3 calcServer.py "192.168.3.6" "9998" &
tail -f /dev/null

