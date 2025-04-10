# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a Pygame clock object
    clock = pygame.time.Clock()
    # Initialize delta time
    dt = 0

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drawing
        screen.fill("black")  # Fill the screen with black

        # Update the display
        pygame.display.flip()

        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000.0

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()

