from tkinter import *

window = Tk()
window.title("Multi-widget GUI-Practice")


def convertor():
    grams1=float(e1_value.get()) * 1000
    grams.insert(END, grams1)

    pounds1 = float(e1_value.get()) * 2.20462
    pounds.insert(END, pounds1)

    ounces1 = float(e1_value.get()) * 35.274
    ounces.insert(END, ounces1)


textField1=Label(window,text="KG")
textField1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",command=convertor)
b1.grid(row=0,column=2)

gramsLabel=Label(window,text="GRAMS")
gramsLabel.grid(row=1,column=0)
grams=Text(window,height=1,width=15)
grams.grid(row=2,column=0)

poundsLabel=Label(window,text="POUNDS")
poundsLabel.grid(row=1,column=1)
pounds=Text(window,height=1,width=15)
pounds.grid(row=2,column=1)

ouncesLabel=Label(window,text="OUNCES")
ouncesLabel.grid(row=1,column=2)
ounces=Text(window,height=1,width=15)
ounces.grid(row=2,column=2)

window.mainloop()