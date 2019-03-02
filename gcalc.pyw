#-------------------------------------------------------------------------------
# Name:        gcalc
# Purpose:     to demonstrate a graphing calculator in python
#
# Author:      CA1K
#
# Created:     16/02/2019
#-------------------------------------------------------------------------------

import tkinter
from tkinter import *
import tkinter.ttk as ttk
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np
import os

size = 1 #figure size
xsize = 10 #range of the x-axis
l1 = "Graphing Calculator" #title text
l2 = "Graph" #text for the graph button
l3 = "Scientific Calculator" #text for the button that switches calculators
l4 = "Calculator by CA1K.XKOTTO.COM" #label at the top
l5 = "Load a previous function"
l6 = "Previous functions..."
px = [] #x-axis array
fc = [] #function cache; previous functions the user entered in
sp = 111 #sub-plot
acc = 1000 #accuracy variable
mp = 10 #message padding

def err(msg): #error message window script
    t = tkinter.Tk()
    t.resizable(0,0)
    t.title("Error")
    l = Label(t,text=msg,padx=mp,pady=mp)
    l.grid(row=0, column=0, sticky=W+E)
    b1 = Button(t,text="OK",command=lambda:t.destroy())
    b1.grid(row=1, column=0, sticky=W+E)
    t.mainloop()

def sel(ar): #selection window for previous functions the user entered
    if len(ar) < 1:
        trw(4)
        pass
    t = tkinter.Tk()
    t.resizable(0,0)
    t.title("Select")
    l = Label(t,text=l5,padx=mp*6,pady=mp)
    l.grid(row=0, column=0, sticky=W+E)
    cb = ttk.Combobox(t,values=ar)
    cb.set("Select a previous function.")
    cb.grid(row=1, column=0, sticky=W+E)
    b = Button(t,text="OK",command=lambda:ptg(t,cb))
    b.grid(row=2, column=0, sticky=W+E)
    t.mainloop()

def ptg(tk,com): #pass to graph function. designed for the selection window
    upd(graph,ax,px,ply(com.get()))
    mden(com.get())
    tk.destroy()

def trw(en): #throws error with error message
    if(en == 0): #you have characters that are not recognized by the program
        err("Invalid letter(s). Plotting failed.")
    if(en == 1): #you have characters that are not recognized by the program
        err("Invalid syntax. Plotting failed.")
    if(en == 2): #you put in the wrong signs for the interpreter
        err("Invalid operator(s). Plotting failed. See README.")
    if(en == 3): #you divided by zero
        err("Division by zero. Plotting failed.")
    if(en == 4): #you just opened the application or haven't given an input yet
        err("No previous functions entered within the current session.")

def ts(m): #switches to the scientific calculator
    m.destroy()
    os.popen("scalc.pyw")

def plx(a): #fills the x-axis up to the xsize limit
    i = -xsize
    while(i<xsize):
        a.append(i)
        i += 1/acc #manages the amount of points plotted onto the graph
    return a

def ply(en): #calculates the function regarding the x-axis
    a2 = []
    if (en in fc) != True:
        fc.append(en) #add function to cache
    for i in range(0,len(px)):
    #variable and function input into the python evaluation method
        globals = {'x':px[i],'sin':np.sin,'cos':np.cos,'tan':np.tan,
        'arcsin':np.arcsin,'arccos':np.arccos,'arctan':np.arctan,
        'sinh':np.sinh,'cosh':np.cosh,'tanh':np.tanh,'floor':np.floor,
        'ceil':np.ceil,'log':np.log,'log2':np.log2,'log10':np.log10,
        'sqrt':np.sqrt,'fix':np.fix,'e':np.e,'PI':np.pi}
        try:
            a2.append(eval(en,globals))
        except NameError:
            trw(0)
            break
        except SyntaxError:
            trw(1)
            break
        except AttributeError:
            trw(2)
            break
        except ZeroDivisionError:
            trw(3)
            break
        except ValueError: #just a bug fix for the console, don't mind it
            break
    return a2

def upd(g,axis,x,y): #updates the graph in the window
    axis.cla()
    axis.grid()
    axis.plot(x,y)
    g.draw()

def mden(t): #modifies the entry text
    e.delete(0,END)
    e.insert(0,t)

#window and title
root = tkinter.Tk()
root.resizable(0,0)
root.wm_title(l1)

#graphing code
fig = Figure()
ax = fig.add_subplot(sp)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.grid()
graph = FigureCanvasTkAgg(fig, master=root)
graph.get_tk_widget().pack(side="top",fill='both',expand=True)
toolbar = NavigationToolbar2Tk(graph,root)
toolbar.update()
px = plx(px)
ax.plot(px,px) #basically the y=x slope is the default function on startup

e = Entry(root)
e.pack(fill=tkinter.BOTH,expand=1)
b1 = Button(root,text=l2,bg="gray",fg="white",command=lambda:upd(graph,ax,px,ply(e.get())))
b1.pack(fill=tkinter.BOTH,expand=1)
b1 = Button(root,text=l6,bg="#111",fg="white",command=lambda:sel(fc))
b1.pack(fill=tkinter.BOTH,expand=1)
b2 = Button(root,text=l3,bg="black",fg="white",command=lambda:ts(root))
b2.pack(fill=tkinter.BOTH,expand=1)

#main loop
root.mainloop()

#def main():
#    pass

#if __name__ == '__main__':
#    main()

