import os
import subprocess
from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from tkinter import messagebox
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
    messagebox.showinfo("Information!!", "This process may take up to 2 minute.\nPlease Check your Internet Connection after 2 minute.")


# Wi-Fi OFF & LAN ON Script
def wifiOffscript():
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'disabled'])
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'TPALAN', 'disabled'])
    subprocess.call(['netsh', 'interface', 'set', 'interface', 'TPALANDOC', 'enabled'])
    subprocess.call(['reg', 'import', 'Enable Proxy.reg'])
    messagebox.showinfo("Information!!", "This process may take up to 2 minute.\nPlease Check your Internet Connection after 2 minute.")

# Wi-Fi Fixing Script
def wifiFixingscript():
    subprocess.call(['reg', 'import', 'Disable Proxy.reg'])
    messagebox.showinfo("Information!!", "This process may take up to 2 minute.\nPlease Check your Internet Connection after 2 minute.")

# Lan Connection Fixing Script
def lanFixingscript():
    subprocess.call(['reg', 'import', 'Enable Proxy.reg'])
    messagebox.showinfo("Information!!", "This process may take up to 2 minute.\nPlease Check your Internet Connection after 2 minute.")


def torontoOWA():
    webbrowser.open(url,new=new)

def citypassReset():
    webbrowser.open(url2,new=new)



###############################################################################

# ---------Menu functions Starts------------
'''
def donothing():
    filewin = Toplevel(window)
    button = Button(filewin, text="Do nothing button")
    button.pack()

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Admin", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

window.config(menu=menubar)
'''
# ---------Menu functions END---------------

window.geometry('250x435+250+250') # Window Size
window.resizable(width=False, height=False) # This code will Stop resizing the windows size that you define.
window.title("TPA Software")
window.configure(bg='white')

# ----------- Configuration for cityOWA Button, you can change the website link here -----------
new = 1
url = "https://exchange.toronto.ca/owa"
url2 = "https://sspr.toronto.ca/sspr/private/Login?idle=false&passwordModified=false&publicOnly=false"

# ----------- Configuration for cityOWA Button -----------

# ----------- Configuration for Logo image , You can change logo here -----------
image=Image.open("logo2.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo, height=100,width=100, bg='white')
label.image = photo  # keep a reference!
label.grid(row=0,column=0,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=30, pady=10)

# ----------- End of Logo Configuration  -----------

wifiOnButton=Button(window,text="WiFi-ON",command=wifiOnscript, height=1, width=22, fg='white', bg='green')
wifiOnButton.grid(row=2,column=0,padx=40, pady=5)
wifiOnButton.config(font=('Raleway', 9, 'bold'))


wifiOffButton=Button(window,text="WiFi-OFF",command=wifiOffscript, height=1, width=22, fg='white', bg='green')
wifiOffButton.grid(row=3,column=0,padx=40, pady=10)
wifiOffButton.config(font=('Raleway', 9, 'bold'))

cityOWA= Button(window, text = "Toronto Online Email",command=torontoOWA ,height=1, width=22, fg='white', bg='green')
cityOWA.grid(row=4,column=0,padx=40, pady=10)
cityOWA.config(font=('Raleway', 9, 'bold'))

cityPassword=Button(window,text="City Password Reset",command=citypassReset, height=1, width=22, fg='white', bg='green')
cityPassword.grid(row=5,column=0,padx=40, pady=10)
cityPassword.config(font=('Raleway', 9, 'bold'))

wifiFixing=Button(window,text="Wi-Fi Connection Fixing",command=wifiFixingscript, height=1, width=22, fg='white', bg='green')
wifiFixing.grid(row=6,column=0,padx=40, pady=10)
wifiFixing.config(font=('Raleway', 9, 'bold'))


lanFixing=Button(window,text="LAN Connection Fixing",command=lanFixingscript, height=1, width=22, fg='white', bg='green')
lanFixing.grid(row=7,column=0,padx=40, pady=10)
lanFixing.config(font=('Raleway', 9, 'bold'))

# ttk.Separator(master,orient=HORIZONTAL).grid(row=2, columnspan=5,sticky="sw")
# ttk.Separator(window).place(x=0, y=410, relwidth=1)

footer = Label(window, text="Designed and Developed By \nToronto Parking Authority I.T Department",
               font=("Helvetica", 7),justify=CENTER, bg='white')
footer.grid(row=8,column=0,padx=0, pady=12)



window.mainloop()