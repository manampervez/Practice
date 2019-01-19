import os
import subprocess
os.system("netsh interface show interface")
#subprocess.call(['Disable Proxy.reg'])
subprocess.call(['reg', 'import', 'Enable Proxy.reg'])

'''
# It will enabled Wi-Fi Network
#subprocess.call(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'enabled'])

# It will enabled TPALAN Network
subprocess.call(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'disabled'])
subprocess.call(['netsh', 'interface', 'set', 'interface', 'TPALANDOC', 'enabled'])


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