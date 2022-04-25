BLACK = (0,0,0)
WHITE = (255,255,255)
hoz,vert = (700,500)

import pygame
from paddle import Paddle
from ball import Ball
from walls import Wall

pygame.init()

scoreA = 0
scoreB = 0

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

wallA = Wall(WHITE, 5, vert)
wallA.rect.x = 0
wallA.rect.y = 0

wallB = Wall(WHITE, 5, vert)
wallB.rect.x = hoz - 5
wallB.rect.y = 0

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(wallA)
all_sprites_list.add(wallB)
all_sprites_list.add(ball)



screen = pygame.display.set_mode(size=(hoz,vert))
pygame.display.set_caption("Pong")

carryOn = True

clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
    all_sprites_list.update()

    if pygame.sprite.collide_mask(ball, wallA):
        ball.bounce()
        ball.respawn()
        scoreB+=1
    if  pygame.sprite.collide_mask(ball, wallB):
        ball.bounce()
        ball.respawn()
        scoreA+=1

    if ball.rect.y>vert-10:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 


    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()


    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5)
    all_sprites_list.draw(screen)
    print(pygame.sprite.collide_rect(ball,wallA)) 

    font = pygame.font.Font(None,74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()