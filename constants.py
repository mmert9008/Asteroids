# This file defines constant values that are used throughout the game.
# Keeping these values in a separate file makes it easy to adjust them
# and keeps the main game logic cleaner.

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Asteroid properties
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3  # Number of different sizes/types of asteroids
ASTEROID_SPAWN_RATE = 0.8  # Rate at which new asteroids spawn (in seconds)
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS # Maximum possible radius of an asteroid

# Player properties
PLAYER_RADIUS = 20

