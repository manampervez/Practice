# import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry('400x300')

header = tk.Frame(root, bg='green', height=30)
content = tk.Frame(root, bg='red')
footer = tk.Frame(root, bg='green', height=30)

header.pack(fill='both')
content.pack(fill='both', expand=True)
footer.pack(fill='both')

root.mainloop()