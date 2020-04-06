import numpy as np
import pygame

class Boundary:
	def __init__(self, x1, y1, x2, y2):
		self.a = pygame.Vector2()
		self.a.xy = x1, y1
		self.b = pygame.Vector2()
		self.b.xy = x2, y2

	def show(self, screen, col):
		# Draw the boundary
		pygame.draw.line(screen, col, self.a, self.b)