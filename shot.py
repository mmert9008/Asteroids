import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

# Class representing a bullet fired by the player. It inherits from CircleShape.
class Shot(CircleShape):
    def __init__(self, x, y):
        # Call the constructor of the parent class (CircleShape)
        # with the initial x and y coordinates and the shot's radius.
        super().__init__(x, y, SHOT_RADIUS)

    # Override the draw method to draw the shot as a small circle.
    def draw(self, screen):
        # Use pygame.draw.circle to draw a filled circle on the screen.
        # - 'screen': The Pygame Surface to draw on.
        # - "yellow": The color of the shot (you can change this).
        # - (int(self.position.x), int(self.position.y)): The center of the circle.
        # - self.radius: The radius of the circle.
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), int(self.radius))

    # Override the update method to make the shot move.
    def update(self, dt):
        # Update the position of the shot by adding its velocity multiplied by the delta time.
        # This ensures that the movement speed is independent of the frame rate.
        self.position += self.velocity * dt

