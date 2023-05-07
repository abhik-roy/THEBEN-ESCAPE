import pygame
from boss import Boss
from player import Player
pygame.init()

# Set up the display
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Boss Test")

# Create the boss
boss = Boss()
player = Player('player1.png')
boss.rect.x = width // 2 - boss.rect.width // 2
boss.rect.y = height // 2 - boss.rect.height // 2

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))
    boss.update(player)
    # Draw the boss
    screen.blit(boss.image, boss.rect)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
