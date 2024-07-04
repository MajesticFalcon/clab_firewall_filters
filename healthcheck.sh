#!/usr/bin/bash

flow1=$(sshpass -p 'admin@123' ssh admin@clab-tshoot-n-1 "ping 100.64.1.2 count 4 rapid | grep !")
flow2=$(sshpass -p 'admin@123' ssh admin@clab-tshoot-n-2 "ping 100.64.1.1 count 4 rapid | grep !")

if [[ $flow1 == *"!!!!"* ]]; then
    echo "[0] Flow 1: Success"
else
    echo "[X] Flow 1: Failed"
fi

if [[ $flow2 == *"!!!!"* ]]; then
    echo "[0] Flow 2: Success"
else
    echo "[X] Flow 2: Failed"
fi
