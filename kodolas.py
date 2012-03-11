#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

def nyomtat():
	ch1 = e.get()
	ch2 = ch1.encode("Latin-1")
	print ch2
	
f = Tk()
e = Entry(f)
e.pack()
Button(f, text = "kiírni", command = nyomtat).pack()
f.mainloop()
