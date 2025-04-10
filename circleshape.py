import pygame

# Base class for game objects that are treated as circles for collision detection.
# Even if the visual representation is different (like the player's triangle),
# we'll use the 'position' and 'radius' for collision logic.
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Initialize the Sprite class. This is necessary for using sprite groups later.
        # The 'containers' attribute is used by Pygame sprite groups to keep track
        # of which groups this sprite belongs to. We handle its potential absence here.
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Store the position of the circle as a Pygame Vector2.
        # Vector2 is useful for 2D math operations.
        self.position = pygame.Vector2(x, y)
        # Store the velocity of the circle, also as a Pygame Vector2.
        # Initially, the velocity is set to zero (not moving).
        self.velocity = pygame.Vector2(0, 0)
        # Store the radius of the circle. This will be used for collision detection.
        self.radius = radius

    # Method to check if this CircleShape collides with another CircleShape object.
    def collides_with(self, other):
        # Calculate the distance between the centers of the two circles using the distance_to() method.
        distance = self.position.distance_to(other.position)
        # If the distance is less than or equal to the sum of their radii, they are colliding.
        return distance <= self.radius + other.radius

    # This method is intended to be overridden by subclasses to handle
    # the drawing of the specific game object on the screen.
    def draw(self, screen):
        # Sub-classes must provide their own implementation for drawing.
        pass

    # This method is intended to be overridden by subclasses to handle
    # any updates to the game object's state over time, such as movement.
    # The 'dt' (delta time) parameter represents the time passed since the last frame.
    def update(self, dt):
        # Sub-classes must provide their own implementation for updating.
        pass

