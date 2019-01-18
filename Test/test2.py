'''

import os
#os.system("netsh interface show interface")

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

import subprocess
subprocess.call(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'disabled'])
#