# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:59:26 2020

@author: MSI
"""


import tkinter as tk
import threading
root = tk.Tk()
root.geometry("700x800+0+0")
word = 'Welcome To My World Of Animation'

def go(counter=0,color_counter=0):
    color_list = ['red','yellow','cyan','red','blue','gray','black']
    if counter == len(word):
        if color_counter == len(color_list)-1: 
            color_counter =0
        l.config(text=word[:counter],fg = color_list[color_counter])
        counter = 0
        root.after(200, lambda: go(counter+1,color_counter+1))
    else:
        if color_counter == len(color_list)-1: 
            color_counter =0
        l.config(text=word[:counter],fg = color_list[color_counter+1])
        root.after(200, lambda: go(counter+1,color_counter+1))

l = tk.Label(root,font=("Comic sans MS",20,'bold','italic'))

l.pack()
threading.Thread(target = go).start()
root.mainloop()