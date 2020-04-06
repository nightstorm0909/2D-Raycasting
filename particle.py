import math
import pygame
import ray as r

class Particle:
	def __init__(self):
		self.pos = pygame.Vector2(100, 200)
		self.rays = []
		for i in range(0, 360, 1):
			self.rays.append(r.Ray(self.pos, math.radians(i)))

	def update(self, x, y):
		self.pos.x, self.pos.y = x, y

	def look(self, walls, screen, col):
		for ray in self.rays:
			record = float('inf')
			closest = None
			for wall in walls:
				pt = ray.cast(wall)
					
				if (pt):										
					d = self.pos.distance_to(pt)
					if (d < record):
						record = d
						closest = pt
					#pygame.draw.line(screen, col, (int(self.pos.x), int(self.pos.y)), (int(pt.x), int(pt.y)))
			if closest:
				pygame.draw.line(screen, col, (int(self.pos.x), int(self.pos.y)), (int(closest.x), int(closest.y)))

	def show(self, screen, col):
		pygame.draw.circle(screen, col, (int(self.pos.x), int(self.pos.y)), 10)
		for ray in self.rays:
			ray.show(screen, col)