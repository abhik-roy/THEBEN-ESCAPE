import os
import pygame
import main
from settings import WIDTH, HEIGHT, FPS, GAP_SIZE, OBSTACLE_SPACING

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Loading Screen")

# Load assets
background_image = pygame.image.load('loading_screen.png')
font = pygame.font.Font('Papyrus.ttf', 30)
green_color = (0, 255, 0)

# Define button class


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(screen, self.hover_color,
                             (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color,
                             (self.x, self.y, self.width, self.height))

        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            if click[0] == 1:
                return True
        return False


# Background buttons
background_buttons = [
    Button(40, 100, 180, 40, "ASPHODEL", (200, 200, 200), (100, 100, 100)),
    Button(40, 150, 180, 40, "HADES", (200, 200, 200), (100, 100, 100)),
    Button(40, 200, 180, 40, "DARKWOOD", (200, 200, 200), (100, 100, 100)),
    Button(40, 250, 180, 40, "LABYRINTH", (200, 200, 200), (100, 100, 100)),
]

music_buttons = [
    Button(300, 100, 180, 40, "Rip n' Tear", (200, 200, 200), (100, 100, 100)),
    Button(300, 160, 180, 40, "puppetz", (200, 200, 200), (100, 100, 100)),
    Button(300, 220, 180, 40, "SRV", (200, 200, 200), (100, 100, 100)),
    Button(300, 280, 180, 40, "TOOL", (200, 200, 200), (100, 100, 100)),
    Button(300, 340, 180, 40, "DINO JR", (200, 200, 200), (100, 100, 100)),
]

# Player character buttons
player_buttons = [
    Button(550, 100, 180, 40, "MINOTAUR",
           (200, 200, 200), (100, 100, 100)),
    Button(550, 160, 180, 40, "GLADIATOR",
           (200, 200, 200), (100, 100, 100)),
    Button(550, 220, 180, 40, "SORCEROR", (200, 200, 200), (100, 100, 100)),
]

# Difficulty buttons
difficulty_buttons = [
    # Button(800, 140, 180, 40, "CHOOSE A DIFFICULTY", (0, 255, 0), (0, 200, 0)),
    Button(800, 200, 180, 40, "GOOBER", (200, 200, 200), (100, 100, 100)),
    Button(800, 260, 180, 40, "GREENIE", (200, 200, 200), (100, 100, 100)),
    Button(800, 320, 180, 40, "GAMER", (200, 200, 200), (100, 100, 100)),
    Button(800, 380, 180, 40, "GOD", (200, 200, 200), (100, 100, 100)),
]

# Load assets
# background_image = pygame.image.load('loading_screen.png')
# font = pygame.font.Font('Papyrus.ttf', 30)
# title_font = pygame.font.Font('Papyrus.ttf', 60)
# sub_font = pygame.font.Font('Papyrus.ttf',


selected_background = None
selected_music = None
selected_player = None
selected_difficulty = None
title_font = pygame.font.Font('Papyrus.ttf', 60)
sub_font = pygame.font.Font('Papyrus.ttf', 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))
    title_text = title_font.render(
        "THEBEN QUEST : an AI game", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(title_text, title_rect)

    subtitle_text = sub_font.render(
        "Choose a background, a song, a difficulty", True, (0, 0, 0))
    subtitle_rect = subtitle_text.get_rect(x=10, y=HEIGHT - 200)
    screen.blit(subtitle_text, subtitle_rect)

    subtitle_text = sub_font.render(
        "and a player character to start your escape", True, (0, 0, 0))
    subtitle_rect = subtitle_text.get_rect(x=10, y=HEIGHT - 150)
    screen.blit(subtitle_text, subtitle_rect)

# Draw choose difficulty text
    d_font = pygame.font.Font('Papyrus.ttf', 34)
    difficulty_text = d_font.render("Choose a difficulty", True, (10, 20, 10))
    difficulty_text_rect = difficulty_text.get_rect(center=(900, 160))
    screen.blit(difficulty_text, difficulty_text_rect)

    # Draw background buttons and check if they are clicked
    for i, button in enumerate(background_buttons):
        button.draw(screen)
        if button.is_clicked():
            selected_background = f"background{i + 1}.png"

    # Draw music buttons and check if they are clicked
    for i, button in enumerate(music_buttons):
        button.draw(screen)
        if button.is_clicked():
            selected_music = f"music{i + 1}.mp3"

    # Draw player buttons and check if they are clicked
    for i, button in enumerate(player_buttons):
        button.draw(screen)
        if button.is_clicked():
            selected_player = f"player{i + 1}.png"

    # Draw difficulty buttons and check if they are clicked
    for i, button in enumerate(difficulty_buttons):
        button.draw(screen)
        if button.is_clicked():
            selected_difficulty = i

    if selected_background is not None and selected_music is not None and selected_player is not None and selected_difficulty is not None:
        # This function will be defined in the main.py file
        main.main(selected_background, selected_music,
                  selected_player, selected_difficulty)
        break

    pygame.display.update()

pygame.quit()
