from tkinter import *

window = Tk()
frame = Frame(window)
frame.pack()

bottomframe = Frame(window)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text = "Red", fg = "red", height = '2', width = '30')
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = "Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text = "Blue", fg = "blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text = "Black", fg = "black", height = '2', width = '100')
blackbutton.pack( side = BOTTOM)
window.
