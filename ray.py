import math
import numpy as np
import pygame
import utils

class Ray:
	def __init__(self, pos, angle):
		self.pos = pos
		self.direction = pygame.Vector2(math.cos(angle), math.sin(angle))
		#self.direction.xy = 1, 0

	def show(self, screen, col):
		# Draw the ray
		translate = utils.translate(self.pos)
		#pygame.draw.line(screen, col, translate.apply((0, 0)), translate.apply(self.direction * 10))
		pygame.draw.line(screen, col, self.pos, self.pos + self.direction*10)

	def lookAt(self, x, y):
		self.direction.x  = x - self.pos.x
		self.direction.y  = y - self.pos.y
		self.direction = self.direction.normalize()


	def cast(self, wall):
		# Source: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
		x1 = wall.a.x
		y1 = wall.a.y
		x2 = wall.b.x
		y2 = wall.b.y

		x3 = self.pos.x
		y3 = self.pos.y
		x4 = self.pos.x + self.direction.x
		y4 = self.pos.y + self.direction.y

		#den = ((x1 - x2)*(y3 - y4)) - ((y1 - y2)*(x3 - x4))
		den = np.linalg.det(np.array([[(x1 - x2), (x3 - x4)], [(y1 - y2), (y3 - y4)]]))
		#print(den)
		if den ==0:
			#print(den)
			return

		#t = (((x1 - x3)*(y3 - y4)) - ((y1 - y3)*(x3 - x4))) / den
		#u = -(((x1 - x2)*(y1 - y3)) - ((y1 - y2)*(x1 - x3))) / den
		t = np.linalg.det(np.array([[(x1 - x3), (x3 - x4)], [(y1 - y3), (y3 - y4)]])) / den
		u = -np.linalg.det(np.array([[(x1 - x2), (x1 - x3)], [(y1 - y2), (y1 - y3)]])) / den

		#print(t, u)
		if (t >= 0) and (t <= 1) and (u >= 0):
			pt = pygame.Vector2(0, 0)
			pt.x = int(x1 + int((t*(x2 - x1))))
			pt.y = int(y1 + int((t*(y2 - y1))))
			return pt
		else:
			#print(t, u)
			#print(x1,y1, x2,y2, x3,y3, x4,y4)
			return