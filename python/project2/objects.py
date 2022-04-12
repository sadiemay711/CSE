import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()


player = Player()


def rot(self):
        self.surf = pygame.transform.rotate(self.og_surf, self.angle)
        self.angle += self.change_angle
        self.angle = self.angle % 36
        self.rect = self.surf.get_rect(center=self.rect.center)