#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *

def mozgat():
	"mozgatja a korongot"
	global x1, y1, dx, dy, color, oval
	x1, y1 = x1 + dx, y1 + dy
	if y1 > 360:
		y1, dx, dy, = 360, 10, 0
		can.delete(ALL)
		oval = can.create_oval(x1, y1, x1 + 30, y1 + 30, width = 2, fill = "blue")
	if x1 > 360:
		x1, dx, dy = 360, 0, -10
		can.delete(ALL)
		oval = can.create_oval(x1, y1, x1 + 30, y1 + 30, width = 2, fill = "green")
	if y1 < 10:
		y1, dx, dy = 10, -10, 0
		can.delete(ALL)
		oval = can.create_oval(x1, y1, x1 + 30, y1 + 30, width = 2, fill = "yellow")
	if x1 < 10:
		x1, dx, dy = 10, 0, 10
		can.delete(ALL)
		oval = can.create_oval(x1, y1, x1 + 30, y1 + 30, width = 2, fill = "red")
	can.coords(oval, x1, y1, x1 + 30, y1 + 30)
	if flag > 0:
		ablak.after(50, mozgat) 
		
def start_it():
	global flag
	flag = flag + 1
	if flag == 1:
		mozgat()
	
def stop_it():
	global flag
	flag = 0

########## Főablak ##########
ablak = Tk()

x1, y1 = 10, 10
dx, dy = 0, 10
flag = 0
color = "red"
can = Canvas(ablak, width = 400, height = 400, bg ="white")
can.pack(side = LEFT)
oval = can.create_oval(x1, y1, x1 + 30, y1 + 30, width = 2, fill = color)
Button(ablak, text = "Elindít", command = start_it).pack()
Button(ablak, text = "Leállít", command = stop_it).pack()
Button(ablak, text = "Kilépés", command = ablak.quit).pack(side = BOTTOM)

ablak.mainloop()
