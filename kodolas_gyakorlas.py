#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

def nyomtat():
	ch1 = e.get()
	ch2 = ch1.encode("Latin-2")
	print ch2

ablak = Tk()
e = Entry(ablak)
e.pack()
Button(ablak, text = "kiírni", command = nyomtat).pack()

ablak.mainloop()
