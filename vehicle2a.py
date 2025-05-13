import pygame
from pygame.locals import *

pygame.init()

resolution = (600, 600)
white = (255, 255, 255)
blue = (0, 0, 128)


window = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    window.fill(white)


    pygame.draw.rect(window, blue, [100, 100, 400, 100], 2)


    pygame.display.update()
    clock.tick(60)


pygame.quit()