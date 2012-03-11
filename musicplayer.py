#!/usr/bin/env python
#-*-coding:utf-8-*-

import pygame

class MusicPlayer:
	def __init__(self):
		pygame.init()
		
	def set_song(self, song):
		self.song = song
		pygame.mixer.music.load(self.song)
		
	def play(self):
		pygame.mixer.music.play()
		
	def stop(self):
		pygame.mixer.music.stop()
		
	def set_time(self):
		self.time = mad.MadFile(self.song).total_time() / 1000
		self.sav.configure(to = self.time)
