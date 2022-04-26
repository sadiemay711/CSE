
import pygame 
import sys 
from button import Button 
  
# initializing the constructor 
pygame.init() 
clock = pygame.time.Clock()

hoz,vert = (720,720) 
# "I feel like a jellyfish sliding off a car"
# opens up a window 
screen = pygame.display.set_mode(size=(hoz,vert)) 
WHITE = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100) 
width = screen.get_width() 
height = screen.get_height() 

buttonA = Button(100,100, 50,50, WHITE)


smallfont = pygame.font.SysFont(None,35)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(buttonA)
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
    all_sprites_list.draw(screen)
    buttonA.update(event_list)
    pygame.display.update()
    print(buttonA.clicked) 