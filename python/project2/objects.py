import pygame

displaysize = 800
screen = pygame.display.set_mode([displaysize,displaysize])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.draw.circle(screen, (255,255,255),(75,25), 10)
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

    def rotateplayer(angle):
        rotate_image = pygame.transform.rotate(player.image, angle)
        rect = rotate_image.get_rect()
        pos = 100,100
        return(rotate_image,pos)


    def update(self):
        for event in pygame.event.get():
             if event.key ==  pygame.K_LEFT:
                self.rect.move_ip(-5,0)
             if event.key ==  pygame.K_RIGHT:
                self.rect.move_ip(5,0)
             if event.key ==  pygame.K_UP:
                self.rect.move_ip(0,-5)
             if event.key ==  pygame.K_DOWN:
                self.rect.move_ip(0,5)



def get_pos():
    pos = pygame.mouse.get_pos()
    return (pos)


player = Player()


