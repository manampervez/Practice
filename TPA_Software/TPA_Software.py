import os
import subprocess
from tkinter import *
from PIL import Image,ImageTk

window= Tk()

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


window.geometry('250x250+250+250') # Window Size
window.title("TPA Software")
window.configure(bg='Blue')


image=Image.open("logo.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo, height=75,width=200)
label.image = photo  # keep a reference!
label.grid(row=0,column=0,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=15, pady=15)


wifiOnButton=Button(window,text="WiFi-ON",command=wifiOnscript)
wifiOnButton.grid(row=2,column=0)

wifiOffButton=Button(window,text="WiFi-OFF",command=wifiOffscript)
wifiOffButton.grid(row=2,column=1)



window.mainloop()