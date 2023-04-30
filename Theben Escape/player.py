import pygame
from settings import BIRD_SCALE, HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load('player.png').convert_alpha()
        width, height = original_image.get_size()
        width, height = int(width * BIRD_SCALE), int(height * BIRD_SCALE)
        self.image = pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 100, 300
        self.vel_y = 0

    def update(self):
        self.vel_y += 1
        self.rect.y += self.vel_y

        # Clamp the player's vertical position within the screen height
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

    def jump(self):
        self.vel_y = -12
