import os
os.system("netsh interface show interface")

def enable():
    os.system("netsh interface set interface 'Wi-Fi' enabled")

def disable():
    os.system("netsh interface set interface 'Wi-Fi' disabled")