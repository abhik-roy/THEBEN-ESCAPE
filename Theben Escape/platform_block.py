import pygame
from settings import WIDTH

class PlatformBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load('platform.png').convert_alpha()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass
