import pygame
import random
from player import Player
from boss import Boss
from Platform import Obstacle
from background import Background
from npc import NPC
from settings import WIDTH, HEIGHT
from settings import generate_speed, generate_FPS, generate_Gs, generate_Ob

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
original_bg_image = pygame.image.load('loading_screen.png').convert()
BACKGROUND_IMG = pygame.transform.scale(original_bg_image, (WIDTH, HEIGHT))
is_bossfight = True

def generate_obstacles(x, shooting_offset=100, gap=1):
    gap_start = random.randint(100, HEIGHT - gap - 100)
    obstacle_top = Obstacle(x, gap_start - HEIGHT, True)
    obstacle_bottom = Obstacle(x, gap_start + gap, False)
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


def main(selected_background, selected_music, selected_player, difficulty):
    FPS = generate_FPS(difficulty)
    GAP_SIZE = generate_Gs(difficulty)
    OBSTACLE_SPACING = generate_Ob(difficulty)
    background1 = Background(selected_background, 4)
    background2 = Background(selected_background, 4)
    background2.rect.x = background1.rect.width
    player = Player(selected_player)
    boss = Boss()
    boss.rect.x = WIDTH // 2 - boss.rect.width // 2
    boss.rect.y = HEIGHT // 2 - boss.rect.height // 2
    all_sprites = pygame.sprite.Group(background1, background2, player)
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
                if event.key == pygame.K_DOWN:
                    player.attack()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.vel_x = 0

        keys_pressed = pygame.key.get_pressed()
        player.update(keys_pressed)
        background1.update()
        background2.update()
        
        if game_started and not is_bossfight:
            if obstacle_timer == 0:
                new_obstacles, gap_start = generate_obstacles(WIDTH, GAP_SIZE)
                obstacles.add(*new_obstacles)
                all_sprites.add(*new_obstacles)
                npc.move_to(gap_start)
                obstacle_timer = OBSTACLE_SPACING
            else:
                obstacle_timer -= 1

            obstacles.update(generate_speed(difficulty))
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
        boss.update(player)
        screen.blit(BACKGROUND_IMG, (0, 0))
        
        all_sprites.draw(screen)
        screen.blit(boss.image, boss.rect)
        draw_text(screen, 'THEBEN QUEST', 100, WIDTH // 2, 20, 'Papyrus.ttf')

        draw_score(screen, f"Score: {score}",
                   WIDTH - 20, 20, 'Papyrus.ttf', size=24)

        pygame.display.flip()

    pygame.quit()


# if __name__ == "__main__":
#    main()
