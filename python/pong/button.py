import pygame
from random import randint
BLACK = (0,0,0)


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y,width,height, color):
        super(Button,self).__init__() 
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect(center = (x, y))

        self.clicked = False

    def setimage(self,color,image,screen):
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((color), pygame.RLEACCEL)
        screen.blit(self.surf,self.rect)
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked