#! /usb/bin/puthon3

import os

PATH_UTM = 'opt/utm/transport/conf'

with open(f'/{PATH_UTM}/transport.properties', 'r') as file:
    lines = file.readlines()

attempt_ip = lines[-2]
access_ip = lines[-1]
data_attempt_ip = attempt_ip.split('=')[1].split(',')
data_access_ip = access_ip.split('=')[1].split(',')
text = attempt_ip.split('=')[1].strip()

if data_attempt_ip == data_access_ip:
    print('correct')
else:
    print('string not correct')
    os.system(f"sed -i '$d' /{PATH_UTM}/transport.properties")
    os.system(f'echo "web.server.access.ip = {text}" >> /{PATH_UTM}/transport.properties')
    print('update succesful')
    os.system('supervisorctl restart utm')
