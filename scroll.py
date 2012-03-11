#!/usr/bin/env python
#-*- coding:utf-8-*-

from Tkinter import *
import Pmw

def action(event = None):
	"""A szöveg görgetése a <target> tag-ig"""
	index = st.tag_nextrange('target', '0.0', END)
	st.see(index[0])
	
# Egy ScrolledText widgetet tartalmazó ablak létrehozása :
fen = Pmw.initialise()
st = Pmw.ScrolledText(fen, labelpos = N, label_text = "A ScrolledText widget demója",
						label_font = "Times 14 bold italic", label_fg = "navy",
						label_pady = 5, text_font = "Helvetica 11 normal", 
						text_bg = "ivory", text_padx = 10, text_pady = 10,
						text_wrap_ = "none", borderframe = 1, borderframe_borderwidth = 3,
						borderframe_relief = SOLID, usehullsize = 1, 
						hull_width = 370, hull_height = 240)
st.pack(expand = YES, fill = BOTH, padx = 8, pady = 8)

# Tag-ek definíciója, eseménykezelő kapcsolása az egérkattintáshoz :
st.tag_configure("title_", foreground = "brown", font = "Helvetica 11 bold italic")
st.tag_configure("link", foreground = "blue", font = "Helvetica 11 bold")
st.tag_configure("target", foreground = "forest green", font = "Times 11 bold")
st.tag_bind("link", "<Button-1>", action)

title_ = """A róka és a holló
írta Jean de la Fontaine, francia szerző
\n"""
author = """
Jean de la Fontaine
francia író (1621 - 1695)
Verses meséi és mindenek előtt,
1668-tól 1694-ig publikált állattörténetei
tették híressé."""

# A Text widget kitöltése (2 technika) :
st.importfile("CorbRenard.txt")
st.insert("0.0", title_, "title_")
st.insert(END, author, "author")
# Kép beszúrása :
photo = PhotoImage(file = "emma.gif")
st.image_create("6.14", image = photo)
# tag dinamikus létrehozása :
st.tag_add("link", "2.4", "2.23")

fen.mainloop()
