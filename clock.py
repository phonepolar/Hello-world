import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((435, 435))

# Здесь мы будем рисовать
ClockImage = pygame.image.load("watch_12.png").convert()

x = 0; # x coordnate of image
y = 0; # y coordinate of image
screen.blit(ClockImage, ( x,y)) # paint to screen

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
