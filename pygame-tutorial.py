import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")

# clock object for framerate
clock = pygame.time.Clock()

#create a surface
test_surface = pygame.Surface((100,200))
test_surface.fill('Red')

while True:
    # event(for) loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface, (200,100))
            
    # draw all out elements
    # update everything
    pygame.display.update()
    clock.tick(60)
    