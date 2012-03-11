#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *

abl1 = Tk()
txt1 = Label(abl1, text = "Első mező :")
txt2 = Label(abl1, text = "Második :")
mezo1 = Entry(abl1)
mezo2 = Entry(abl1)
txt1.grid(row = 0, sticky = E)
txt2.grid(row = 1, sticky = E)
mezo1.grid(row = 0, column = 1)
mezo2.grid(row = 1, column = 1)

abl1.mainloop()
