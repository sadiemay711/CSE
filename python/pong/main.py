
import pygame
import sys
from button import Button

# initializing the constructor
pygame.init()
clock = pygame.time.Clock()

rez_listA = [320,640,1280,1920]
rez_listB = [240,480,720,1080]


hoz,vert = (720,720) 
margin = 20
# "I feel like a jellyfish sliding off a car"
# opens up a window 
screen = pygame.display.set_mode(size=(hoz,vert)) 
WHITE = (255,255,255) 
BLUE = (25,25,255) 
BLACK = (0,0,0)
color_light = (170,170,170) 
color_dark = (100,100,100) 
width = screen.get_width() 
height = screen.get_height() 

back = Button(0+margin,0+margin, 50,50, WHITE)
buttonB = Button(100,500, 50,50, WHITE)


smallfont = pygame.font.SysFont(None,35)

to_up = pygame.sprite.Group()
to_up.add(back)
to_up.add(buttonB)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(back)
# rendering a text written in
# this font
text = smallfont.render('Quit' , True , WHITE)
run = True
while run:
    mouse = pygame.mouse.get_pos()
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
    to_up.update(event_list)
    if back.clicked == True:
        all_sprites_list.add(buttonB)
    if back.clicked == False:
        all_sprites_list.remove(buttonB)
    screen.fill(BLACK)
    back.setimage(WHITE,"arrow.png",screen)
    all_sprites_list.draw(screen)
    pygame.display.flip()