#! /usr/bin/python3


from datetime import datetime
from netmiko import ConnectHandler

#Get current date and time. COnvert it to string
TNOW = datetime.now().strftime('%Y%m%d_%H%M%S')

#Folder path to save backup files
backup_folder ='/home/sauron/scripts/backup/'

#List of exceptions, should be updated as new exceptions are encountered
netmiko_exceptions = {'NetmikoTimeoutException':'Device not reachable',
                      'SSHException':'Make sure SSH is enabled in device',
                      'NetmikoAuthenticationException':'Authentication Failure.'}

with open('devices_list') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'cisco',
        'password': 'cisco'
    }
    #net_connect = ConnectHandler(**ios_device)
    try:
        net_connect = ConnectHandler(**ios_device)
    except Exception as e :
        print('Failed to ', devices,netmiko_exceptions[type(e).__name__])
        continue
    
    output = net_connect.send_command("show run")
    hostname= net_connect.base_prompt
    with open(backup_folder+hostname+'_'+TNOW,'w') as f:
         f.write(output)
    net_connect.disconnect()
