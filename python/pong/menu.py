
import pygame 
import sys 
from button import Button 
  
# initializing the constructor 
pygame.init() 
clock = pygame.time.Clock()

# screen resolution 
res = (720,720) 
# "I feel like a jellyfish sliding off a car"
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont(None,35)

# rendering a text written in
# this font
text = smallfont.render('Quit' , True , color)
run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 

    # updates the frames of the game 
    pygame.display.update()
    print(pygame.mouse.get_pos()) 