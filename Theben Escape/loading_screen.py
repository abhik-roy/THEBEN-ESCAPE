import os
import pygame
import main
from settings import WIDTH, HEIGHT, FPS, GAP_SIZE, OBSTACLE_SPACING
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Loading Screen")

# Load assets
background_image = pygame.image.load('loading_screen.png')
font = pygame.font.Font('Papyrus.ttf', 30)

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

        text_surface = font.render(self.text, True, (0, 0, 50))
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
    Button(50, 100, 200, 50, "ASPHODEL", (200, 200, 200), (100, 100, 100)),
    Button(50, 200, 200, 50, "HADES", (200, 200, 200), (100, 100, 100)),
    Button(50, 300, 200, 50, "DARKWOOD", (200, 200, 200), (100, 100, 100)),
]

# Music buttons
music_buttons = [
    Button(550, 100, 200, 50, "DOOM", (200, 200, 200), (100, 100, 100)),
    Button(550, 200, 200, 50, "puppetz", (200, 200, 200), (100, 100, 100)),
    Button(550, 300, 200, 50, "voodoo", (200, 200, 200), (100, 100, 100)),
    Button(550, 400, 200, 50, "POT", (200, 200, 200), (100, 100, 100)),
    Button(550, 500, 200, 50, "yeeHAW", (200, 200, 200), (100, 100, 100)),
]

selected_background = None
selected_music = None
title_font = pygame.font.Font('Papyrus.ttf', 60)
sub_font = pygame.font.Font('Papyrus.ttf', 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))
    title_text = title_font.render("THEBEN ESCAPE", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(title_text, title_rect)
    subtitle_text = sub_font.render(
        "Choose a background and a song to start your escape ", True, (0, 0, 0))
    subtitle_rect = subtitle_text.get_rect(x=10, y=HEIGHT - 150)

    screen.blit(subtitle_text, subtitle_rect)

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

    if selected_background is not None and selected_music is not None:
        # This function will be defined in the main.py file
        main.main(selected_background, selected_music)
        break

    pygame.display.update()

pygame.quit()
