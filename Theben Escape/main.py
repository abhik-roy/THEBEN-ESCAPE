import pygame
import random
from player import Player
from Platform import Obstacle
from settings import WIDTH, HEIGHT, FPS, GAP_SIZE, OBSTACLE_SPACING

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Theben Escape")
clock = pygame.time.Clock()
original_bg_image = pygame.image.load('background2.png').convert()

BACKGROUND_IMG = pygame.transform.scale(original_bg_image, (WIDTH, HEIGHT))


def generate_obstacles(x):
    gap_start = random.randint(100, HEIGHT - GAP_SIZE - 100)
    obstacle_top = Obstacle(x, gap_start - HEIGHT, True)
    obstacle_bottom = Obstacle(x, gap_start + GAP_SIZE, False)
    return obstacle_top, obstacle_bottom


def draw_text(surface, text, size, x, y, font_name):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def main():
    player = Player()
    all_sprites = pygame.sprite.Group(player)
    obstacles = pygame.sprite.Group()

    obstacle_timer = 0
    game_started = False

    pygame.mixer.music.load('background_music.mp3')
    pygame.mixer.music.set_volume(0.5)  # Set the volume to 50%

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
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop_movement()

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
        draw_text(screen, 'THEBEN ESCAPE', 64, WIDTH // 2, 20, 'doomfont.ttf')
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
