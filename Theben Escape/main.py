import pygame
import random
from player import Player
from Platform import Obstacle
from npc import NPC
from settings import WIDTH, HEIGHT, FPS, GAP_SIZE, OBSTACLE_SPACING

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
original_bg_image = pygame.image.load('loading_screen.png').convert()
BACKGROUND_IMG = pygame.transform.scale(original_bg_image, (WIDTH, HEIGHT))


def generate_obstacles(x, shooting_offset=100):
    gap_start = random.randint(100, HEIGHT - GAP_SIZE - 100)
    obstacle_top = Obstacle(x, gap_start - HEIGHT, True)
    obstacle_bottom = Obstacle(x, gap_start + GAP_SIZE, False)
    obstacle_top.rect.x += shooting_offset
    obstacle_bottom.rect.x += shooting_offset
    return (obstacle_top, obstacle_bottom), gap_start


def draw_text(surface, text, size, x, y, font_name):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def draw_score(screen, text, x, y, font_name, size=24, text_color=(255, 0, 0)):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.topright = (x, y)
    screen.blit(text_surface, text_rect)


def game_over_screen(screen, score):
    font = pygame.font.Font('doomfont.ttf', 64)
    text = font.render("GAME OVER", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
    screen.blit(text, text_rect)

    font = pygame.font.Font('doomfont.ttf', 32)
    text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
    screen.blit(text, text_rect)


def end_game(screen, score):
    game_over_screen(screen, score)


def draw_speech_bubble(screen, text, x, y, font_name, size=100, padding=10, bubble_color=(255, 255, 255), text_color=(0, 0, 0)):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x + padding, y + padding)

    bubble_rect = text_surface.get_rect()
    bubble_rect.inflate_ip(padding * 2, padding * 2)
    bubble_rect.topleft = (x, y)

    pygame.draw.rect(screen, bubble_color, bubble_rect)
    pygame.draw.rect(screen, text_color, bubble_rect, 2)
    screen.blit(text_surface, text_rect)


def middle_collision(player, obstacles):
    middle_offset = player.rect.height // 2
    player_middle_rect = player.rect.inflate(0, -middle_offset)
    for obstacle in obstacles:
        if player_middle_rect.colliderect(obstacle.rect):
            if player.attacking:
                obstacle.kill()
                return False, True
            else:
                return True, False
    return False, False


def main(selected_background, selected_music):
    player = Player()
    all_sprites = pygame.sprite.Group(player)
    obstacles = pygame.sprite.Group()

    npc = NPC()
    all_sprites.add(npc)
    speech_bubble_timer = 0
    obstacle_timer = 0
    game_started = False
    original_bg_image = pygame.image.load(selected_background).convert()
    BACKGROUND_IMG = pygame.transform.scale(original_bg_image, (WIDTH, HEIGHT))
    pygame.mixer.music.load(selected_music)
    pygame.mixer.music.play(-1)
    score = 0
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
                if event.key == pygame.K_RETURN:
                    player.attack()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.vel_x = 0

        keys_pressed = pygame.key.get_pressed()
        player.update(keys_pressed)

        if game_started:
            speech_bubble_timer += 1
            if speech_bubble_timer % (5) == 0:
                draw_speech_bubble(
                    screen, "Watch out!", npc.rect.x - 150, npc.rect.y - 50, 'doomfont.ttf', size=200)

        if game_started:
            if obstacle_timer == 0:
                new_obstacles, gap_start = generate_obstacles(WIDTH)
                obstacles.add(*new_obstacles)
                all_sprites.add(*new_obstacles)
                npc.move_to(gap_start)
                obstacle_timer = OBSTACLE_SPACING
            else:
                obstacle_timer -= 1

            obstacles.update()
            for obstacle in obstacles:
                if obstacle.rect.right < player.rect.centerx and not obstacle.scored:
                    score += 1
                    obstacle.scored = True

            player.update(keys_pressed)

            collided, attacking_collision = middle_collision(player, obstacles)
            if collided:
                end_game(screen, score)
                # pygame.time.wait(10000)
                running = False

            elif attacking_collision:
                score += 5

        screen.blit(BACKGROUND_IMG, (0, 0))
        draw_text(screen, 'THEBEN ESCAPE', 100, WIDTH // 2, 20, 'Papyrus.ttf')
        all_sprites.draw(screen)
        draw_score(screen, f"Score: {score}",
                   WIDTH - 20, 20, 'Papyrus.ttf', size=24)

        pygame.display.flip()

    pygame.quit()


# if __name__ == "__main__":
#    main()
