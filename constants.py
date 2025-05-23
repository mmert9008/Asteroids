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
PLAYER_TURN_SPEED = 300  # Degrees per second the player can rotate
PLAYER_SPEED = 200      # Pixels per second the player can move forward/backward
PLAYER_SHOOT_SPEED = 500 # Pixels per second the player's shots travel
PLAYER_SHOOT_COOLDOWN = 0.3 # Time in seconds between shots

# Shot properties
SHOT_RADIUS = 5

