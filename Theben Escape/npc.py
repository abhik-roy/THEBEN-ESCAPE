import pygame
from settings import WIDTH, HEIGHT


class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('npc.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH - \
            self.rect.width, HEIGHT // 2 - self.rect.height // 2

    def move_to(self, target_y):
        speed = 5
        if self.rect.y < target_y:
            self.rect.y += speed
        elif self.rect.y > target_y:
            self.rect.y -= speed
