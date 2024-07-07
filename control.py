#!/usr/bin/python3
from napalm import get_network_driver
import sys
import os
junos_driver = get_network_driver("junos")

patch = """
interfaces {
    ge-0/0/0 {
        unit 0 {
            vlan-tags outer 5 inner 3;
        }
    }
}
"""

unpatch = """
interfaces {
    ge-0/0/0 {
        unit 0 {
            vlan-tags outer 5 inner 2;
        }
    }
}
"""

opt = sys.argv[1]

if opt == "patch":
    n2 = junos_driver(hostname="clab-tshoot-n-2", username="admin", password="admin@123")
    n2.open()
    n2.load_merge_candidate(config=patch)
    n2.commit_config()
    print("done")
elif opt == "unpatch":
    n2 = junos_driver(hostname="clab-tshoot-n-2", username="admin", password="admin@123")
    n2.open()
    n2.load_merge_candidate(config=unpatch)
    n2.commit_config()
    print("done")
elif opt == "show_config":
    print(os.system("sshpass -p admin@123 ssh admin@clab-tshoot-n-2 'show configuration interfaces ge-0/0/0.0 vlan-tags'"))
elif opt == "show_firewall":
    print(os.system("sshpass -p admin@123 ssh admin@clab-tshoot-r-1 'show firewall'"))
elif opt == "clear_firewall":
    print(os.system("sshpass -p admin@123 ssh admin@clab-tshoot-r-1 'clear firewall all'"))
elif opt == "test":
    print(os.system("jsnapy --snapcheck -f config_check.yml"))

