import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background color
    screen.fill(BACKGROUND_COLOR)

    # Update the display
    pygame.display.flip()