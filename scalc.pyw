#-------------------------------------------------------------------------------
# Name:        scalc
# Purpose:     to demonstrate a scientific calculator in python
#
# Author:      CA1K
#
# Created:     09/02/2019
#-------------------------------------------------------------------------------

#feel free to tinker with the variables bw, bp, l1, and l2

from tkinter import *
import tkinter as tk
from math import *
import os

#pre-defined variables
l1 = "Calculator by CA1K.XKOTTO.COM" #top label in the window
l2 = "Scientific Calculator" #title
v = 0 #output value
bw = 6 #button width
bp = 3 #button padding
que = [] #number que the calculator will reference
finished = 0 #signals that the operations are done
span = 7 #span of the non-buttons

#pre-defined classes/functions
class window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.que = que
        self.finished = finished
        self.v = v
        self.pi = pi
        self.e = e
        self.init_window()
    def init_window(self):
        self.master.title(l2)
        self.pack(fill=BOTH, expand=1)
        l = Label(self, text=l1, bg="black", fg="white")
        l.grid(row=0, column=0, columnspan=span, sticky=W+E)
        entry = Label(self, text=str(v), bg="gray")
        entry.grid(row=1, columnspan=span, sticky=W+E)
        cls = Button(self, text="Clear", width=bw, command=lambda:clr(entry,que))
        cls.grid(row=2, column=0, columnspan=span, sticky=W+E)
        sev = Button(self, text="7", width=bw, command=lambda:chb(7,entry))
        sev.grid(row=3, column=0)
        xlx = Button(self, text="log x2, x", width=bw, command=lambda:op(entry,7,que))
        xlx.grid(row=3, column=6)
        xl2 = Button(self, text="log 2, x", width=bw, command=lambda:lb2(entry))
        xl2.grid(row=4, column=6)
        xl10 = Button(self, text="log 10, x", width=bw, command=lambda:l10(entry))
        xl10.grid(row=5, column=6)
        mod = Button(self, text="%", width=bw, command=lambda:op(entry,6,que))
        mod.grid(row=6, column=6)
        powr = Button(self, text="^", width=bw, command=lambda:op(entry,4,que))
        powr.grid(row=3, column=4)
        sq = Button(self, text="x^2", width=bw, command=lambda:sqr(entry))
        sq.grid(row=4, column=4)
        cu = Button(self, text="x^3", width=bw, command=lambda:cub(entry))
        cu.grid(row=5, column=4)
        npow = Button(self, text="x^x", width=bw, command=lambda:npown(entry))
        npow.grid(row=6, column=4)
        ee = Button(self, text="e", width=bw, command=lambda:chb(e,entry))
        ee.grid(row=3, column=5)
        pie = Button(self, text="π", width=bw, command=lambda:chb(pi,entry))
        pie.grid(row=4, column=5)
        ssq = Button(self, text="√", width=bw, command=lambda:ssqf(entry))
        ssq.grid(row=5, column=5)
        s3q = Button(self, text="3√", width=bw, command=lambda:s3qf(entry))
        s3q.grid(row=6, column=5)
        xrx = Button(self, text="x2√x", width=bw, command=lambda:op(entry,5,que))
        xrx.grid(row=7, column=5)
        eig = Button(self, text="8", width=bw, command=lambda:chb(8,entry))
        eig.grid(row=3, column=1)
        nin = Button(self, text="9", width=bw, command=lambda:chb(9,entry))
        nin.grid(row=3, column=2)
        div = Button(self, text="/", width=bw, command=lambda:op(entry,3,que))
        div.grid(row=3, column=3)
        fou = Button(self, text="4", width=bw, command=lambda:chb(4,entry))
        fou.grid(row=4, column=0)
        fiv = Button(self, text="5", width=bw, command=lambda:chb(5,entry))
        fiv.grid(row=4, column=1)
        six = Button(self, text="6", width=bw, command=lambda:chb(6,entry))
        six.grid(row=4, column=2)
        mul = Button(self, text="*", width=bw, command=lambda:op(entry,2,que))
        mul.grid(row=4, column=3)
        one = Button(self, text="1", width=bw, command=lambda:chb(1,entry))
        one.grid(row=5, column=0)
        two = Button(self, text="2", width=bw, command=lambda:chb(2,entry))
        two.grid(row=5, column=1)
        thr = Button(self, text="3", width=bw, command=lambda:chb(3,entry))
        thr.grid(row=5, column=2)
        mns = Button(self, text="-", width=bw, command=lambda:op(entry,1,que))
        mns.grid(row=5, column=3)
        zer = Button(self, text="0", width=bw, command=lambda:chb(0,entry))
        zer.grid(row=6, column=0)
        equ = Button(self, text="=", width=bw, command=lambda:fin(entry,que))
        equ.grid(row=6, column=1)
        pls = Button(self, text="+", width=bw, command=lambda:op(entry,0,que))
        pls.grid(row=6, column=2)
        dot = Button(self, text=".", width=bw, command=lambda:dec(entry))
        dot.grid(row=6, column=3)
        si = Button(self, text="sin(x)", width=bw, command=lambda:sct(0,entry))
        si.grid(row=7, column=0)
        co = Button(self, text="cos(x)", width=bw, command=lambda:sct(1,entry))
        co.grid(row=7, column=1)
        tang = Button(self, text="tan(x)", width=bw, command=lambda:sct(2,entry))
        tang.grid(row=7, column=2)
        dtr = Button(self, text="° -> π", width=bw, command=lambda:conv(0,entry))
        dtr.grid(row=7, column=3)
        rtd = Button(self, text="π -> °", width=bw, command=lambda:conv(1,entry))
        rtd.grid(row=7, column=4)
        rp = Button(self, text="1 / x", width=bw, command=lambda:recp(entry))
        rp.grid(row=7, column=6)
        asi = Button(self, text="asin(x)", width=bw, command=lambda:sct(3,entry))
        asi.grid(row=8, column=0)
        aco = Button(self, text="acos(x)", width=bw, command=lambda:sct(4,entry))
        aco.grid(row=8, column=1)
        atang = Button(self, text="atan(x)", width=bw, command=lambda:sct(5,entry))
        atang.grid(row=8, column=2)
        delt = Button(self, text="del", width=bw, command=lambda:de(entry))
        delt.grid(row=8, column=3)
        ttg = Button(self, text="Graphing Calculator", width=int(bw*3.5), command=lambda:tg(self))
        ttg.grid(row=8, column=4, columnspan=3, sticky=E)
        self.pack()
        def reg(a,b,c): #uses a to determine the type of calculation of b and c
            if(a==0):
                print(str(b) + " + " + str(c))
                return b + c
            if(a==1):
                print(str(b) + " - " + str(c))
                return b - c
            if(a==2):
                print(str(b) + " x " + str(c))
                return b * c
            if(a==3):
                print(str(b) + " / " + str(c))
                return b / c
            if(a==4):
                print(str(b) + " to the power of " + str(c))
                return b ** c
            if(a==5):
                print(str(c) + " root " + str(b))
                return b ** (1 / c)
            if(a==6):
                print(str(b) + " % " + str(c))
                return b % c
            if(a==7):
                print(str(b) + " log " + str(c))
                return log(b,c)
        def chb(n,z): #change the output box number
            r = z.cget("text")
            if(self.finished == 0): #if the number in the box isn't the answer...
                if(r == "0" or n == pi or n == e):
                    z.config(text=str(n))
                else:
                    z.config(text=r+str(n))
            else:
                z.config(text=str(n))
                self.finished = 0
        def clr(z,z2): #erase the value in the output and array values
            z.config(text="0")
            z2.clear() #supposed to be an array
            v = 0 #resetting the answer variable
        def op(z,n,q): #puts the operation and first number in que
            if(len(q)==0):
                try:
                    q.append(int(z.cget("text")))
                except ValueError: #if the number is a float...
                    q.append(float(z.cget("text")))
                q.append(n)
                z.config(text="0")
            else:
                q.clear()
                try:
                    q.append(int(z.cget("text")))
                except ValueError:
                    q.append(float(z.cget("text")))
                q.append(n)
                z.config(text="0")
        def ret(zz): #convenient function to retrieve the number
            try:
                return int(zz.cget("text"))
            except ValueError: #if the number in the output is a float...
                return float(zz.cget("text"))
        def fin(z,q):
            z2 = ret(z)
            q.append(z2)
            v = reg(q[1],q[0],q[2]) #send the array to the reg method
            z.config(text=str(v))
            q.clear()
            finished = 1
            v = 0
        def dec(z): #adds a decimal to the number in the output window
            z2 = z.cget("text")
            if "." in z2:
                print("error: 2 decimals")
            else:
                z.config(text=z2+".") #add a decimal to the end
        def npown(z): #bring the number to the power of itself
            z2 = ret(z)
            z.config(text=str(z2 ** z2))
            print(str(z2) + " to the power of " + str(z2))
            v = 0
            finished = 1
        def sqr(z): #square the number
            z2 = ret(z)
            z.config(text=str(z2 ** 2))
            print(str(z2) + " squared")
            v = 0
            finished = 1
        def cub(z): #cube the number
            z2 = ret(z)
            z.config(text=str(z2 ** 3))
            print(str(z2) + " cubed")
            v = 0
            finished = 1
        def ssqf(z): #square root the number in the box
            z2 = ret(z)
            z.config(text=str(sqrt(z2)))
            print("square root of " + str(z2))
            v = 0
            finished = 1
        def s3qf(z):
            z2 = ret(z)
            z3 = z2 ** (1 / 3) #z2 to the power of 0.3, which is a cube root
            z.config(text=str(z3))
            print("cube root of " + str(z2))
            v = 0
            finished = 1
        def sct(m,z): #sine, cosine, tangent...
            z2 = ret(z)
            if(z2 % pi == 0 or z2 / pi == 0.5 or z2 / pi == 1.5):
                print("[deg -> rad] conversion not needed")
            else:
                print("converting " + str(z2) + " degrees to " + str(radians(z2)) + " radians")
                z2 = radians(z2)
            if(m == 0):
                z.config(text=str(sin(z2)))
                print("sine of " + str(z2))
            if(m == 1):
                z.config(text=str(cos(z2)))
                print("cosine of " + str(z2))
            if(m == 2):
                z.config(text=str(tan(z2)))
                print("tangent of " + str(z2))
            if(m == 3):
                z.config(text=str(asin(z2)))
                print("arc sine of " + str(z2))
            if(m == 4):
                z.config(text=str(acos(z2)))
                print("arc cosine of " + str(z2))
            if(m == 5):
                z.config(text=str(atan(z2)))
                print("arc tangent of " + str(z2))
            v = 0
            finished = 1
        def conv(m,z): #convert between degrees and radians
            z2 = ret(z)
            if(m == 0): #degrees to radians
                print("converting " + str(z2) + " degrees to " + str(radians(z2)) + " radians")
                z.config(text=str(radians(z2)))
            if(m == 1): #radians to degrees
                print("converting " + str(z2) + " radians to " + str(degrees(z2)) + " degrees")
                z.config(text=str(degrees(z2)))
            v = 0
            finished = 1
        def lb2(z): #log base 2
            z2 = ret(z)
            z3 = log(z2,2)
            z.config(text=str(z3))
            print(str(z2) + " log 2")
            v = 0
            finished = 1
        def l10(z): #log base 10
            z2 = ret(z)
            z3 = log10(z2)
            z.config(text=str(z3))
            print(str(z2) + " log 10")
            v = 0
            finished = 1
        def recp(z): #return the reciprocal (opposite) of the value
            z2 = ret(z)
            z3 = 1 / z2
            z.config(text=str(z3))
            print("reciprocal of " + str(z2))
            v = 0
            finished = 1
        def de(z): #deletes a digit from the number in the box
            z2 = z.cget("text")
            z2 = z2[:-1]
            if(z2 == ""):
                z2 = "0"
            z.config(text=z2)
        def tg(m): #toggles calculator to graphing calculator
            m.master.destroy()
            os.popen("gcalc.pyw")

#procedures
root = tk.Tk()
root.resizable(0,0)
win = window(root)
root.mainloop()

#if __name__ == '__main__':
#    main()

