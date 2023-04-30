import pygame
import random
from player import Player
from Platform import Obstacle
from settings import WIDTH, HEIGHT, FPS, GAP_SIZE, OBSTACLE_SPACING

pygame.init()
pygame.mixer.init()  # Initialize the mixer for background music

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
original_bg_image = pygame.image.load('background.png').convert()
BACKGROUND_IMG = pygame.transform.scale(original_bg_image, (WIDTH, HEIGHT))


def generate_obstacles(x):
    gap_start = random.randint(100, HEIGHT - GAP_SIZE - 100)
    obstacle_top = Obstacle(x, gap_start - HEIGHT, True)
    obstacle_bottom = Obstacle(x, gap_start + GAP_SIZE, False)
    return obstacle_top, obstacle_bottom


def draw_text(surface, text, size, x, y, font_name):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (200, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def main():
    player = Player()
    all_sprites = pygame.sprite.Group(player)
    obstacles = pygame.sprite.Group()

    obstacle_timer = 0
    game_started = False

    # Load and play background music
    pygame.mixer.music.load('background_music.mp3')
    pygame.mixer.music.play(-1)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_started:
                        game_started = True
                    player.jump()

        if game_started:
            if obstacle_timer == 0:
                new_obstacles = generate_obstacles(WIDTH)
                obstacles.add(*new_obstacles)
                all_sprites.add(*new_obstacles)
                obstacle_timer = OBSTACLE_SPACING
            else:
                obstacle_timer -= 1

            obstacles.update()
            player.update()

            if pygame.sprite.spritecollideany(player, obstacles):
                running = False

        screen.blit(BACKGROUND_IMG, (0, 0))
        draw_text(screen, 'THEBEN ESCAPE', 64, WIDTH // 2, 20, 'DOOMFONT.ttf')
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
