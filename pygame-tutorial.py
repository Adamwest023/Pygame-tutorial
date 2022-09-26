from operator import truediv
import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 500) - start_time
    score_surf = test_font.render(
        f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)


def intro_screen():
    intro_surf = test_font.render('Pixel Game', False, (111, 196, 169))
    intro_rect = intro_surf.get_rect(center=(400, 50))
    screen.blit(intro_surf, intro_rect)
    instruc_surf = test_font.render('Press SPACE to star', False, (111, 196, 169))
    instruc_rect = instruc_surf.get_rect(center=(400, 350))
    screen.blit(instruc_surf, instruc_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
# clock object for framerate
clock = pygame.time.Clock()
game_active = True
start_time = 0


# create a surface
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# create text and surface for it
# score_surf = test_font.render('My game', False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(400, 50))
# create snail surface and movement
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

snail_rect = snail_surf.get_rect(midbottom=(600, 300))

# player surface and rectangle
player_surf = pygame.image.load(
    'graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

# intro screen
player_stand = pygame.image.load(
    'graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))


while True:
    # event(for) loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/500)

    if game_active:
        # draw all out elements
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 12)
        # screen.blit(score_surf, score_rect)
        # pygame.draw.line(screen, (64, 64, 64), (340, 65), (460, 65), 2)
        display_score()
        snail_rect.x -= 4
        if snail_rect.right <= -30:
            snail_rect.left = 850
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        intro_screen()

    pygame.display.update()
    clock.tick(60)
