import pygame
from settings import WIDTH, HEIGHT, BIRD_SCALE


class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load('npc.png').convert_alpha()
        width, height = original_image.get_size()
        width, height = int(width * BIRD_SCALE), int(height * BIRD_SCALE)
        self.image = pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH - \
            self.rect.width, HEIGHT // 2 - self.rect.height // 2

    def move_to(self, target_y):
        speed = 10
        if self.rect.y < target_y:
            self.rect.y += speed
        elif self.rect.y > target_y:
            self.rect.y -= speed
