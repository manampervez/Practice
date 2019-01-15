from tkinter import *
import subprocess

#result = subprocess.run(["runas", "/noprofile", "/user:Administrator", "netsh", "interface", "set", "interface", "Ethernet0", "DISABLED"])

window= Tk()
window.title("TPA Software")

wifiOn=Button(window,text="WiFi-ON")
wifiOn.grid(row=0,column=0)

wifiOff=Button(window,text="WiFi-OFF")
wifiOff.grid(row=1,column=0)

#udemy Tutorial:
def km_to_miles():
    print("Hello World")

b1=Button(window,text="Quit",command=window.quit)
b1.grid(row=0,column=1)
#print("FAILED..." if result.returncode else "SUCCESS!")

e1=Entry(window)
e1.grid(row=1,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=2,column=1)


window.mainloop()