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


def torontoOWA():
    webbrowser.open(url,new=new)

def citypassReset():
    webbrowser.open(url2,new=new)

###############################################################################

window.geometry('250x450+250+250') # Window Size
window.resizable(width=False, height=False) # This code will Stop resizing the windows size that you define.
window.title("TPA Software")
window.configure(bg='green')

# ----------- Configuration for cityOWA Button, you can change the website link here -----------
new = 1
url = "https://exchange.toronto.ca/owa"
url2 = "https://sspr.toronto.ca/sspr/private/Login?idle=false&passwordModified=false&publicOnly=false"

# ----------- Configuration for cityOWA Button -----------

# ----------- Configuration for Logo image , You can change logo here -----------
image=Image.open("logo.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo, height=75,width=200)
label.image = photo  # keep a reference!
label.grid(row=0,column=0,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=20, pady=15)

# ----------- End of Logo Configuration  -----------

wifiOnButton=Button(window,text="WiFi-ON",command=wifiOnscript, height=1, width=22)
wifiOnButton.grid(row=2,column=0,padx=40, pady=10)

wifiOffButton=Button(window,text="WiFi-OFF",command=wifiOffscript, height=1, width=22)
wifiOffButton.grid(row=3,column=0,padx=40, pady=10)

cityOWA= Button(window, text = "Toronto Online Email",command=torontoOWA ,height=1, width=22)
cityOWA.grid(row=4,column=0,padx=40, pady=10)

cityPassword=Button(window,text="City Password Reset",command=citypassReset, height=1, width=22)
cityPassword.grid(row=5,column=0,padx=40, pady=10)

wifiFixing=Button(window,text="Wi-Fi Connection Fixing",command=wifiFixingscript, height=1, width=22)
wifiFixing.grid(row=6,column=0,padx=40, pady=10)

lanFixing=Button(window,text="Internet Connection Fixing",command=lanFixingscript, height=1, width=22)
lanFixing.grid(row=7,column=0,padx=40, pady=10)

# ttk.Separator(master,orient=HORIZONTAL).grid(row=2, columnspan=5,sticky="sw")
ttk.Separator(window).place(x=0, y=410, relwidth=1)

footer = Label(window, text="Designed and Developed By \nToronto Parking Authority I.T Department",
               font=("Helvetica", 7),justify=CENTER,relief=RIDGE)
footer.grid(row=8,column=0,padx=40, pady=29)


window.mainloop()