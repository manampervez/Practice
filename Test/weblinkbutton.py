from tkinter import *
import webbrowser

window= Tk()

new = 1
# url = "https://exchange.toronto.ca/owa"
url = "www.nice-canada.ca"

def torontoOWA():
    webbrowser.open(url,new=new)
# webbrowser.open_new_tab(url)

cityOWA= Button(window, text = "Toronto Email",command=torontoOWA ,height=1, width=22)
cityOWA.pack()

window.mainloop()