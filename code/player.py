import pygame 
from pygame.surface import Surface

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)