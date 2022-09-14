import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))

while True:
    # event(for) loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all out elements
    # update everything
    pygame.display.update()
    