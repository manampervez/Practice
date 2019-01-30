'''
import os
import subprocess
from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from tkinter import ttk

window= Tk()

# os.system("netsh interface show interface")
###############################################################################
# Wi-Fi ON & LAN OFF Script
def wifiOnscript():
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'enabled'])
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'TPALAN', 'disabled'])
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'TPALANDOC', 'disabled'])
    subprocess.call(['reg', 'import', 'Disable Proxy.reg'])


# Wi-Fi OFF & LAN ON Script
def wifiOffscript():
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'disabled'])
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'TPALAN', 'disabled'])
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'TPALANDOC', 'enabled'])
    subprocess.call(['reg', 'import', 'Enable Proxy.reg'])


# Wi-Fi Fixing Script
def wifiFixingscript():
    subprocess.call(['reg', 'import', 'Disable Proxy.reg'])

# Lan Connection Fixing Script
def lanFixingscript():
    subprocess.call(['reg', 'import', 'Enable Proxy.reg'])

wifiOnButton=Button(window,text="WiFi-ON",command=wifiOnscript, height=1, width=22)
wifiOnButton.grid(row=2,column=0,padx=40, pady=10)

wifiOffButton=Button(window,text="WiFi-OFF",command=wifiOffscript, height=1, width=22)
wifiOffButton.grid(row=3,column=0,padx=40, pady=10)

window.mainloop()
'''

'''
name = input("What's your name? ")
print("Nice to meet you " + name + "!")
age = input("Your age? ")
print("So, you are already " + str(age) + " years old, " + name + "!")
'''

import subprocess
import os
os.system("netsh interface show interface")
# newName = input("Enter To change Interface Name ")
# print(newName)

subprocess.call(['netsh', 'interface', 'set', 'interface', 'name=newName'])

os.system("netsh interface show interface")

'''
netsh interface set interface name="TPALANDOC" newname="TPALAN"

netsh interface set interface name="TPALAN" newname="TPALANDOC"

netsh interface show interface


Admin State    State          Type             Interface Name
-------------------------------------------------------------------------
Enabled        Connected      Dedicated        TPALANDOC


'''