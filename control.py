#!/usr/bin/python3
# Author: Schylar Utley
# Date: 7/8/24
# Purpose: To provide automation for controlling repeated operations

from napalm import get_network_driver
import sys
import os
junos_driver = get_network_driver("junos")

try:
    opt = sys.argv[1]
except IndexError:
    opt = "help"

if opt == "patch":
    n2 = junos_driver(hostname="clab-tshoot-n-2", username="admin", password="admin@123")
    n2.open()
    n2.load_merge_candidate(filename="patch.conf")
    n2.commit_config()
    print("done")
elif opt == "unpatch":
    n2 = junos_driver(hostname="clab-tshoot-n-2", username="admin", password="admin@123")
    n2.open()
    n2.load_merge_candidate(filename="unpatch.conf")
    n2.commit_config()
    print("done")
elif opt == "show_config":
    print(os.system("sshpass -p admin@123 ssh admin@clab-tshoot-n-2 'show configuration routing-options'"))
elif opt == "show_firewall":
    print(os.system("sshpass -p admin@123 ssh admin@clab-tshoot-r-1 'show firewall'"))
elif opt == "clear_firewall":
    print(os.system("sshpass -p admin@123 ssh admin@clab-tshoot-r-1 'clear firewall all'"))
elif opt == "test":
    print(os.system("jsnapy --snapcheck -f config_check.yml"))
elif opt == "r1":
    os.system("sshpass -p admin@123 ssh admin@clab-tshoot-r-1")
elif opt == "n1":
    os.system("sshpass -p admin@123 ssh admin@clab-tshoot-n-1")
elif opt == "n2":
    os.system("sshpass -p admin@123 ssh admin@clab-tshoot-n-2")
elif opt == "rebuild":
    os.system("clab destroy")
    os.system("clab deploy")
elif opt == "help":
    print("Missing arguments. See available args below")
    print("    patch = implement fix")
    print("    unpatch = remove fix")
    print("    show_config = show interface configuration")
    print("    show_firewall = show firewall counters")
    print("    clear_firewall = clear firewall counters")
    print("    test = run unit tests")
    print("    n1,n2,r1 = ssh into containers")
    print("    rebuild = clab destroy + clab deploy")
    print("Example: python3 ./control.py patch")

