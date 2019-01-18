import os
import subprocess
os.system("netsh interface show interface")
# It will enabled Wi-Fi Network
subprocess.call(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'enabled'])

# It will enabled TPALAN Network
# subprocess.call(['netsh', 'interface', 'set', 'interface', 'TPALAN', 'enabled'])

'''
def enable():
    os.system("netsh interface set interface 'Wi-Fi' enabled")
enable()

#def disable():
#   os.system("netsh interface set interface 'TPALAN' disabled")

#disable()

'''

'''
import subprocess

def enable():
    subprocess.call('netsh interface set interface "Wi-Fi" enabled')
enable()

'''