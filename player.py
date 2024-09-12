import pygame
from math import pi, cos, sin

# Constants
MOVE_SPEED = 5
ROTATE_SPEED = pi / 90  # Rotate speed (in radians)
WALL_HEIGHT = 60  # The height of each cell in the maze

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.angle = pi / 2  # Start facing upwards

    def move(self, keys, maze):
        new_x = self.x
        new_y = self.y

        if keys[pygame.K_UP]:
            new_x += MOVE_SPEED * cos(self.angle)
            new_y += MOVE_SPEED * sin(self.angle)
        if keys[pygame.K_DOWN]:
            new_x -= MOVE_SPEED * cos(self.angle)
            new_y -= MOVE_SPEED * sin(self.angle)
        if keys[pygame.K_LEFT]:
            self.angle -= ROTATE_SPEED
        if keys[pygame.K_RIGHT]:
            self.angle += ROTATE_SPEED

        # Check for wall collision before updating position
        if maze[int(new_y / WALL_HEIGHT)][int(new_x / WALL_HEIGHT)] == 0:  # Only move if no wall
            self.x = new_x
            self.y = new_y