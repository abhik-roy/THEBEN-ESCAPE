import pygame
from settings import BIRD_SCALE, HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load('player.png').convert_alpha()
        width, height = original_image.get_size()
        width, height = int(width * BIRD_SCALE), int(height * BIRD_SCALE)
        self.original_image = pygame.transform.scale(
            original_image, (width, height))
        self.image = self.original_image.copy()
        self.jump_counter = 0
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 100, 300
        self.vel_y = 0
        self.attacking = False
        self.attack_timer = 0

        self.spinning = False
        self.spin_angle = 0

    def update(self, keys_pressed):
        # gravity
        self.vel_y += 0.5
        self.rect.y += self.vel_y

        # Clamp the player's vertical position within the screen height
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))
        if self.rect.y == HEIGHT - self.rect.height:
            self.jump_counter = 0
        if self.spinning:
            self.spin_angle -= 15
            if self.spin_angle <= -360:
                self.spin_angle = 0
                self.spinning = False

            self.image = pygame.transform.rotate(
                self.original_image, self.spin_angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        if keys_pressed[pygame.K_LEFT]:
            self.vel_x = -10
        elif keys_pressed[pygame.K_RIGHT]:
            self.vel_x = 10
        else:
            self.vel_x = 0

        self.rect.x += self.vel_x

        if self.attacking:
            if self.attack_timer < 30:
                self.attack_timer += 1
            else:
                self.attack_timer = 0
                self.attacking = False

    def jump(self):
        if self.jump_counter < 3:
            self.vel_y = -15
            self.jump_counter += 1

    def attack(self):
        self.attacking = True
        self.spinning = True
        self.spin_angle = 0

    def move_left(self):
        self.vel_x = -10

    def move_right(self):
        self.vel_x = 10

    def stop_movement(self):
        self.vel_x = 0
