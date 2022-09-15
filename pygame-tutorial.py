import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
# clock object for framerate
clock = pygame.time.Clock()

# create a surface
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
# create text and surface for it
text_surface = test_font.render('My game', False, 'Black')

# create snail surface and movement
snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600

while True:
    # event(for) loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 4
    if(snail_x_pos <= -70):
        snail_x_pos = 850
    screen.blit(snail_surface, (snail_x_pos, 270))
    # draw all out elements
    # update everything
    pygame.display.update()
    clock.tick(60)
