import pygame

class translate:
	def __init__(self, amt):
		self.amt = amt

	def apply(self, pos):
		return self.amt + pos