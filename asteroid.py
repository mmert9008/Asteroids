import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random # Import the random module

# Class representing an asteroid in the game. It inherits from CircleShape
# and has a visual representation as a circle.
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the constructor of the parent class (CircleShape)
        # with the initial x, y coordinates, and the asteroid's radius.
        super().__init__(x, y, radius)

    # Method to handle the splitting of an asteroid into smaller asteroids.
    def split(self):
        # Immediately remove the current asteroid.
        self.kill()

        # If the asteroid is already the smallest size, just return.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random split angle between 20 and 50 degrees.
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity.
        new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        # Calculate the new radius for the smaller asteroids.
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new Asteroid objects at the current position with the new radius and velocities.
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity_1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity_2

    # Override the draw method to draw the asteroid as a circle.
    def draw(self, screen):
        # Use pygame.draw.circle to draw a circle on the screen.
        # - 'screen': The Pygame Surface to draw on.
        # - "grey": The color of the circle (you can change this).
        # - (int(self.position.x), int(self.position.y)): The center of the circle.
        # - self.radius: The radius of the circle.
        # - 2: The width of the outline of the circle.
        pygame.draw.circle(screen, "grey", (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    # Override the update method to make the asteroid move.
    def update(self, dt):
        # Update the position of the asteroid by adding its velocity multiplied by the delta time.
        # This ensures that the movement speed is independent of the frame rate.
        self.position += self.velocity * dt

