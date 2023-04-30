import pygame
from settings import OBSTACLE_WIDTH


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, is_stalactite):
        super().__init__()
        image_file = 'stalactite.png' if is_stalactite else 'stalagmite.png'
        original_image = pygame.image.load(image_file).convert_alpha()
        width, height = original_image.get_size()
        height = int(height * (OBSTACLE_WIDTH / width))
        self.image = pygame.transform.scale(
            original_image, (OBSTACLE_WIDTH, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        self.rect.x -= 5
        if self.rect.x + self.rect.width < 0:
            self.kill()
