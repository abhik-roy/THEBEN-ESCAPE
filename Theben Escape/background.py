import pygame
from settings import WIDTH, HEIGHT


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, speed):
        super().__init__()
        self.image = pygame.image.load(image_file).convert()
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.rect.left = self.rect.width
