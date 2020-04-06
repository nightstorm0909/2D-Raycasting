import os
import random
import pygame
from particle import Particle
import ray as ry
import boundary as bd

# initialize the pygame
pygame.init()

# Create the screen
WIDTH = 800     # x axis
HEIGHT = 600    # y axis
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#wall = bd.Boundary(700,100, 700,500)
# Random walls
walls = []
for _ in range(5):
	x1 = random.randint(0, WIDTH)
	x2 = random.randint(0, WIDTH)
	y1 = random.randint(0, HEIGHT)
	y2 = random.randint(0, HEIGHT)
	walls.append(bd.Boundary(x1,y1, x2,y2))
walls.append(bd.Boundary(0, 0, WIDTH, 0))
walls.append(bd.Boundary(WIDTH, 0, WIDTH, HEIGHT))
walls.append(bd.Boundary(WIDTH, HEIGHT, 0, HEIGHT))
walls.append(bd.Boundary(0, HEIGHT, 0, 0))
particle = Particle()

# Title and icon
pygame.display.set_caption("2D RayCasting")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Display the Walls
    for wall in walls:
    	wall.show(screen, (255, 255, 255))
    particle.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    particle.look(walls, screen, (225, 225, 225))
    particle.show(screen, (255, 255, 255))
   
    pygame.display.update()
    #break