# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:34:54 2020

@author: MSI
"""

import threading
from tkinter import * 
import random 
def change_color():
    color_list = ['red','yellow','cyan','red','blue','gray','black']
    label.config(fg = random.choice(color_list))
    root.after(1000, change_color) 
root = Tk()
label = Label(root,text="Hello Wordl Color Change",font=('Comic sans MS',20,'bold'))
label.pack()
threading.Thread(target = root.after,args=[1000,change_color]).start() # function name without ()


root.mainloop()
