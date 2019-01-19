import os
import subprocess
from tkinter import *
from PIL import Image,ImageTk

# os.system("netsh interface show interface")

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



window= Tk()

window.geometry('250x250+250+250') # Window Size
window.configure(background='white')

image=Image.open("logo.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo, height=60,width=150)
label.image = photo  # keep a reference!
label.grid(row=0,column=1)


window.title("TPA Software")


wifiOnButton=Button(window,text="WiFi-ON",command=wifiOnscript)
wifiOnButton.grid(row=1,column=1)

wifiOffButton=Button(window,text="WiFi-OFF",command=wifiOffscript)
wifiOffButton.grid(row=2,column=1)


'''
#udemy Tutorial:
def km_to_miles():
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)

b1=Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=1)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=1,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=2,column=1)
'''
window.mainloop()