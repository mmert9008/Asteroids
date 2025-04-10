import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED  # Import PLAYER_TURN_SPEED

# Class representing the player's spaceship. It inherits from CircleShape
# so that we can use its position and radius for collision detection,
# even though the player is visually represented as a triangle.
class Player(CircleShape):
    def __init__(self, x, y):
        # Call the constructor of the parent class (CircleShape)
        # with the initial x and y coordinates and the player's radius.
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize the rotation angle of the player. This will affect
        # the orientation of the triangle. It starts at 0 degrees.
        self.rotation = 0

    # Method to rotate the player by a certain amount based on the time passed (dt).
    def rotate(self, dt):
        # Increase the rotation angle by the turn speed multiplied by the delta time.
        # Multiplying by dt makes the rotation speed independent of the frame rate.
        self.rotation += PLAYER_TURN_SPEED * dt

    # Method to calculate the vertices of the triangle representing the player.
    # It uses the player's current position, rotation, and radius to determine
    # the three points of the triangle.
    def triangle(self):
        # 'forward' vector points in the direction the player is currently facing.
        # We start with a vector pointing upwards (0, 1) and rotate it by the player's rotation angle.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # 'right' vector is perpendicular to the 'forward' vector and is used to
        # define the base of the triangle. Its length is related to the player's radius.
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        # Calculate the coordinates of the three vertices of the triangle:
        # 'a' is the tip of the triangle (in the 'forward' direction from the center).
        a = self.position + forward * self.radius
        # 'b' is one of the base points, behind the center and to the left.
        b = self.position - forward * self.radius - right
        # 'c' is the other base point, behind the center and to the right.
        c = self.position - forward * self.radius + right
        # Return the list of the three vertex points.
        return [a, b, c]

    # Override the draw method from the parent class to draw the player's triangle.
    def draw(self, screen):
        # Use pygame.draw.polygon to draw a filled polygon on the screen.
        # - 'screen': The Pygame Surface to draw on.
        # - "white": The color of the polygon.
        # - self.triangle(): The list of vertex points calculated by the triangle() method.
        # - 2: The width of the outline of the polygon (0 for filled).
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # Override the update method from the parent class. This is called in each frame
    # to update the player's state based on user input and the time passed (dt).
    def update(self, dt):
        # Get the state of all keyboard keys. This returns a sequence of boolean values.
        keys = pygame.key.get_pressed()

        # Check if the 'a' key is pressed (pygame.K_a).
        if keys[pygame.K_a]:
            # To rotate left, we need to decrease the rotation angle.
            # We can achieve this by passing a negative 'dt' value to the rotate method.
            self.rotate(-dt)

        # Check if the 'd' key is pressed (pygame.K_d).
        if keys[pygame.K_d]:
            # To rotate right, we increase the rotation angle, so we pass the regular 'dt'.
            self.rotate(dt)

