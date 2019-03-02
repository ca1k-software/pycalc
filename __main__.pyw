#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     switches between calculator windows
#
# Author:      CA1K
#
# Created:     17/02/2019
#-------------------------------------------------------------------------------

#import(s)
import os
import tkinter as tk
from tkinter import *

#variables
ti = "Message"
tl = "Choose a type of calculator."
tb1 = "Scientific"
tb2 = "Graphing"
bw = 15 #button width
mode = 2 #boolean that determines the switching between the calculator apps

def cm(v,w): #changes the mode and closes the window
    global mode
    mode = v
    w.destroy()

def wc(): #the window that changes the mode
    t = tk.Tk()
    t.resizable(0,0)
    t.title(ti)
    l = Label(t,text=tl)
    l.grid(row=0, column=0, columnspan=2)
    b1 = Button(t,text=tb1,width=bw,command=lambda:cm(0,t))
    b1.grid(row=1, column=0)
    b2 = Button(t,text=tb2,width=bw,command=lambda:cm(1,t))
    b2.grid(row=1, column=1)
    t.mainloop()

def main():
    wc()
    if(mode == 0):
        os.popen("scalc.pyw")
    elif(mode == 1):
        os.popen("gcalc.pyw")
    pass

if __name__ == '__main__':
    main()
