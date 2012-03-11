#!/usr/bin/python
#-*-coding:utf-8-*-

import pygame, mad, time, threading
from Tkinter import *

class GNUAmp:
	"""A simple musicplayer"""
	def __init__(self):
		pygame.init()
		self.STOPPED = 1
		self.PAUSED = 2
		self.RUNNING = 3
		self.state = self.STOPPED
		pygame.init()
		self.set_song("/home/palesz/Zenék/fangoria - criticar por criticar.mp3")
		
		self.ablak = Tk()
		self.label_current = Label(self.ablak, text = "0:00")
		self.label_current.grid(row = 1, column = 1)
		self.sav = Scale(self.ablak, orient = HORIZONTAL, from_ = 0.0, showvalue = 0, length = 150)
		self.sav.grid(row = 1, column = 2, columnspan = 2)
		self.set_time()
		self.label_max = Label(self.ablak, text = self.initiate_max())
		self.label_max.grid(row = 1, column = 4)
		self.button_play = Button(self.ablak, text = "Play", command = self.start)
		self.button_play.grid(row = 2, column = 1)
		Button(self.ablak, text = "Stop", command = self.stop).grid(row = 2, column = 2)
		Scale(self.ablak, from_ = 0.0, to=1.0, resolution = 0.01, orient = HORIZONTAL, command = self.set_volume, showvalue = 0).grid(
				row=2,column = 3, padx = 10)
		self.label_volume = Label(self.ablak)
		self.label_volume.grid(row = 2, column = 4)
		
		self.ablak.mainloop()
		
	def start(self):
		"control the behavior of the 'Play' button"
		if self.state == self.STOPPED:
			self.play()
		elif self.state == self.RUNNING:
			self.pause()
		elif self.state == self.PAUSED:
			self.resume()
		
	def set_time(self):
		self.time = mad.MadFile(self.song).total_time() / 1000
		self.sav.configure(to = self.time)
	
	def initiate_max(self):
		"initiate the labels"	
		self.perc = self.time / 60
		self.masodperc = self.time - self.perc * 60
		if self.masodperc < 10:
			self.formattime = "%s:0%s" % (self.perc, self.masodperc)
		else:
			self.formattime = "%s:%s" % (self.perc, self.masodperc)
		return self.formattime
		
	def play(self):
		"play the current song, and change the 'Play' button"
		pygame.mixer.music.play()
		self.button_play.configure(text = "Pause")
		self.state = self.RUNNING	
		self.t = ThreadingClass(self.sav, self.label_current, self.label_max)
		self.t.start()
			
	def pause(self):
		"pausing the current song, and change the 'Play' button"
		pygame.mixer.music.pause()
		self.button_play.configure(text = "Play")
		self.state = self.PAUSED
		
	def resume(self):
		"resume the current sont, and change the 'Play' button"
		pygame.mixer.music.unpause()
		self.button_play.configure(text = "Pause")
		self.state = self.RUNNING
			
	def stop(self):
		"stop the playing, and reset a few variable"
		pygame.mixer.music.stop()
		self.button_play.configure(text = "Play")
		self.sav.set(0)
		self.label_current.configure(text = "0:00")
		if self.state != self.STOPPED:
			self.t.stop()
		self.state = self.STOPPED
		
	def set_song(self, song):
		"set and load the song"
		self.song = song
		pygame.mixer.music.load(self.song)	
		
	def set_volume(self, volume):
		"set the volume level"
		pygame.mixer.music.set_volume(float(volume))
		self.label_volume.configure(text = str(volume))
		
class ThreadingClass(threading.Thread):
	def __init__(self, sav, label_current, label_max):
		threading.Thread.__init__(self)
		self.sav = sav
		self.label_current = label_current
		self.label_max = label_max
		self.perc = 0
		self.masodperc = 0
			
	def run(self):
		while pygame.mixer.music.get_busy():
			self.ertek = pygame.mixer.music.get_pos() / 1000
			self.ido = self.ertek
			self.sav.set(self.ertek)
			self.label_current.configure(text = self.update())
			time.sleep(1)
		self.label_current.configure(text = "0:00")
			
	def stop(self):
		self.retry = True
		while self.retry:
			self.join(1)
			self.retry = False
		self.perc = 0
		
	def update(self):
		"update the elapsed time"
		while self.ido > 0:
			if self.ido % 60:
				self.masodperc += 1
			else:
				self.masodperc = 0
				self.perc += 1
		
			if self.masodperc < 10:
				return "%s:0%s" % (self.perc, self.masodperc)
			return "%s:%s" % (self.perc, self.masodperc)
			
if __name__ == "__main__":
	GNUAmp()

	
	
	







