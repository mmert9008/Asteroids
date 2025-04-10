import pygame
from circleshape import CircleShape

# Class representing an asteroid in the game. It inherits from CircleShape
# and has a visual representation as a circle.
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the constructor of the parent class (CircleShape)
        # with the initial x, y coordinates, and the asteroid's radius.
        super().__init__(x, y, radius)

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

