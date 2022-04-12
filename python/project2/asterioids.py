import pygame


from objects import player
from objects import rot  

pygame.init()


displaysize = 800

screen = pygame.display.set_mode([displaysize,displaysize])


player_x = displaysize/2
player_y = displaysize/2


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key ==  pygame.K_LEFT:
                player_x = player_x -5
            if event.key ==  pygame.K_RIGHT:
                player_x = player_x +5
            if event.key ==  pygame.K_UP:
               player_y=player_y-5
            if event.key ==  pygame.K_DOWN:
               player_y=player_y+5

    screen.fill((0, 0, 0))

    player.rot()

    screen.blit(player.surf, (player_x,player_y))

    pygame.display.flip()

pygame.quit()