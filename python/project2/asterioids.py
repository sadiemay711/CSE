import pygame

from objects import Player 
from objects import player 
from objects import player 
from objects import get_pos 
from objects import screen
from objects import displaysize

def rotateplayer(angle):
    rotate_image = pygame.transform.rotate(player.surf, angle)
    rect = rotate_image.get_rect()
    pos = 100,100
    return(rotate_image,pos)


pygame.init()
pos = get_pos

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
    player.update()
    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

pygame.quit()