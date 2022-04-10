<<<<<<< HEAD
import pygame
from pygame.surface import Surface
=======
import pygame 
>>>>>>> parent of 3322ca1 (module problem solved)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
<<<<<<< HEAD
        self.image = Surface((32, 64))
=======
        self.image = pygame.surface((32,64))
>>>>>>> parent of 3322ca1 (module problem solved)
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
