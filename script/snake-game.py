import pygame, sys
pygame.init()

#Screen
size = width, height = 320, 240
screen = pygame.display.set_mode(size)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()