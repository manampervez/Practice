from tkinter import *

window= Tk()
window.title("TPA Software")

wifiOn=Button(window,text="WiFi-ON")
wifiOn.grid(row=0,column=0)

wifiOff=Button(window,text="WiFi-OFF")
wifiOff.grid(row=1,column=0)

window.mainloop()