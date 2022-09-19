import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
# clock object for framerate
clock = pygame.time.Clock()

# create a surface
sky_surf = pygame.image.load('graphics/Sky.png').convert()  
ground_surf = pygame.image.load('graphics/ground.png').convert()

# create text and surface for it
score_surf = test_font.render('My game', False, 'Black')
score_rect = score_surf.get_rect(center= (400,50))
# create snail surface and movement
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

snail_rect = snail_surf.get_rect(midbottom = (600,300))

# player surface and rectangle
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    # event(for) loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')
             
    # draw all out elements       
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    screen.blit(score_surf, score_rect)
    snail_rect.x -= 4
    if snail_rect.right <= -30:
        snail_rect.left = 850
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)
    
    # collision detection
    # if player_rect.colliderect(snail_rect):
    #    print("collision detected")   
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())
    # update everything
    
    pygame.display.update()
    clock.tick(60)
