import pygame


pygame.init()

displaysize = 800

screen = pygame.display.set_mode([displaysize,displaysize])


x = displaysize/2
y = displaysize/2


running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN: 
            if event.key == K_ESCAPE:
                running = False 
            if event.key ==  K_LEFT:
                y = y -5
            if event.key ==  K_RIGHT:
                y = y +5
            if event.key ==  K_UP:
                x = x +5
            if event.key ==  K_DOWN:
                x = x -5

    screen.fill((245, 245, 245))



    pygame.draw.circle(screen, (0,0,255), (x,y), 75)

    pygame.display.flip()

pygame.quit()