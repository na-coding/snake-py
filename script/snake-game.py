import pygame, sys
import Color
pygame.init()

#Screen
size = width, height = 320, 240
center_x = width//2
center_y = height//2
screen = pygame.display.set_mode(size)

#Game variables
speed = 0.005
move = 0
offset = 10

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()
    
    screen.fill(Color.WHITE)

    pygame.draw.line(screen, Color.BLACK, (center_x,center_y), (center_x ,center_y + 3), 1)
    speed += 0.005


    pygame.display.flip()