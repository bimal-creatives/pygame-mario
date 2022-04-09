from tkinter import Toplevel
import pygame

class Tile(pygame.sprite.Sprite):
    def ___init__(self,pos,size):
        super().__init__()
        self.image = pygame.surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(Topleft = pos)