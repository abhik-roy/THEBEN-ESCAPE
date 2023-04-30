import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = WINDOW_HEIGHT - PLAYER_HEIGHT - 50
        self.velocity_y = 0

    def update(self):
        self.rect.y += self.velocity_y
        self.velocity_y += GRAVITY

        # Keep player on screen
        if self.rect.bottom > WINDOW_HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT - GROUND_HEIGHT
            self.velocity_y = 0

    def jump(self):
        self.velocity_y = -20
