#! /usr/bin/python3

import json
from napalm import get_network_driver

driver = get_network_driver('ios')

R2 = '172.16.1.147'
R3 = '172.16.1.146'
R4 = '172.16.1.145'
R5 = '172.16.1.144'

username = 'shesh'
password = 'shesh'

for device in (R2,R3,R4,R5):
    R_connect = driver(device,username,password)
    R_connect.open()
    R_output = R_connect.get_facts()

    print ("*"*150)
    print (f"Details about {device}")
    print(json.dumps(R_output,indent = 4))

    R_connect.close()