import pygame
from settings import BOSS_SCALE, WIDTH, HEIGHT


class Boss(pygame.sprite.Sprite):
    def __init__(self, boss='npc.png'):
        super().__init__()
        self.last_attack_time = 0
        self.attack_cooldown = 1000
        original_image = pygame.image.load(boss).convert_alpha()
        width, height = original_image.get_size()
        width, height = int(width * BOSS_SCALE), int(height * BOSS_SCALE)
        self.original_image = pygame.transform.scale(
            original_image, (width, height))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 400, 300
        self.vel_x, self.vel_y = 0, 0
        self.attacking = False
        self.attack_timer = 0
        self.spinning = False
        self.spin_angle = 0
        self.jump_counter = 0

    def jump(self):
        if self.jump_counter < 2:
            self.vel_y = -7.5
            self.jump_counter += 1

    def update(self, player):
        self.vel_y += 0.5
        self.rect.y += self.vel_y
        if self.rect.y == HEIGHT - self.rect.height:
            self.jump_counter = 0
        # follow player
        if self.rect.x < player.rect.x:
            self.vel_x = 4.5
        elif self.rect.x > player.rect.x:
            self.vel_x = -4.5
        else:
            self.vel_x = 0

        if self.rect.y < player.rect.y:
            self.vel_y = 7.5
        if self.rect.y > player.rect.y:
            self.vel_y = -3
            self.jump()
            self.jump()
        else:
            self.vel_y = 0

        # attack
        current_time = pygame.time.get_ticks()

        if current_time - self.last_attack_time >= self.attack_cooldown:
            self.attacking = True
            self.spinning = True
            self.spin_angle = 0
            self.last_attack_time = current_time

        # move
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Clamp the boss's position within the screen width and height
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

        # Spin and attack animation
        if self.spinning:
            self.spin_angle += 15
            if self.spin_angle >= 360:
                self.spin_angle = 0
                self.spinning = False

            self.image = pygame.transform.rotate(
                self.original_image, self.spin_angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        if self.attacking:
            if self.attack_timer < 30:
                self.attack_timer += 1
            else:
                self.attack_timer = 0
                self.attacking = False
