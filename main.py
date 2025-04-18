# This file contains the main game loop and initializes Pygame.
import pygame
from constants import * # Import all constants from the constants.py file
from player import Player    # Import the Player class from the player.py file
from asteroidfield import AsteroidField # Import the AsteroidField class
from asteroid import Asteroid # Import the Asteroid class
from shot import Shot         # Import the Shot class
import sys # Import the sys module for exiting the program

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame. This is a necessary step before using any Pygame modules.
    pygame.init()

    # Create the game window (Surface) with the dimensions defined in constants.py.
    # The 'screen' variable will be used to draw all game elements.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create Pygame Group objects to manage updatable and drawable game objects.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() # Create a group to hold all asteroids
    shots = pygame.sprite.Group()     # Create a group to hold all shots

    # Set the 'containers' class variable for the Player class to include our new groups.
    # Any instances of Player created after this will automatically be added to these groups.
    Player.containers = (updatable, drawable)

    # Set the 'containers' class variable for the Asteroid class to include the asteroid group
    # as well as the updatable and drawable groups.
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set the 'containers' class variable for the Shot class to include the shots group
    # as well as the updatable and drawable groups.
    Shot.containers = (shots, updatable, drawable)

    # Set the 'containers' class variable for the AsteroidField class to only the updatable group.
    # The AsteroidField itself is not something we draw directly, but it does update.
    AsteroidField.containers = (updatable,)

    # Calculate the initial position of the player in the center of the screen.
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    # Instantiate the Player object. It will now automatically be added to the 'updatable' and 'drawable' groups.
    player = Player(player_x, player_y)

    # Instantiate the AsteroidField object. It will start spawning asteroids.
    asteroid_field = AsteroidField()

    # Create a Pygame Clock object. This will be used to control the frame rate of the game.
    clock = pygame.time.Clock()
    # Initialize a variable to store the delta time (time since the last frame).
    # This will be used for frame-rate independent movement and updates.
    dt = 0

    # The main game loop. This loop will continue running until the user quits the game.
    running = True
    while running:
        # Event handling loop. This checks for events such as key presses, mouse movement,
        # and window closing.
        for event in pygame.event.get():
            # If the user clicks the close button (QUIT event), set 'running' to False
            # to exit the game loop.
            if event.type == pygame.QUIT:
                running = False

        # Update game objects. Call the 'update' method for all sprites in the 'updatable' group.
        updatable.update(dt)

        # Collision detection:
        # Check for collisions between the player and each asteroid.
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return # Exit the main function, which will end the game loop

            # Check for collisions between each asteroid and each shot.
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split() # Call the split method instead of kill
                    shot.kill()     # Remove the shot from all groups

        # Drawing section. Everything drawn here will be displayed on the screen.
        # First, fill the screen with black in each frame. This clears the previous frame.
        screen.fill("black")
        # Iterate through all sprites in the 'drawable' group and call their 'draw' method.
        for entity in drawable:
            entity.draw(screen)

        # Update the full display Surface to the screen. This makes the changes visible to the user.
        pygame.display.flip()

        # Control the frame rate of the game. clock.tick(60) will pause the loop
        # to ensure the game runs at a maximum of 60 frames per second.
        # It also returns the time elapsed since the last call to tick() in milliseconds.
        # We divide this by 1000.0 to convert it to seconds and store it in 'dt' (delta time).
        dt = clock.tick(60) / 1000.0

    # Quit Pygame. This should be called after the game loop ends to uninitialize Pygame modules.
    pygame.quit()

# This condition checks if the script is being run directly (not imported as a module).
if __name__ == "__main__":
    main()

