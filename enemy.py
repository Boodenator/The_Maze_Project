import pygame
from math import atan2, hypot

class Enemy:
    def __init__(self, x, y, texture_path):
        self.x = x
        self.y = y
        self.alive = True
        self.texture = pygame.image.load(texture_path)

    def distance_to_player(self, player):
        return hypot(self.x - player.x, self.y - player.y)

    def angle_to_player(self, player):
        return atan2(self.y - player.y, self.x - player.x)

    def draw(self, screen, player, screen_width, screen_height, fov):
        if not self.alive:
            return
        
        # Calculate distance and angle relative to the player
        distance = self.distance_to_player(player)
        angle = self.angle_to_player(player) - player.angle

        if -fov / 2 <= angle <= fov / 2:  # Enemy is within the player's field of view
            # Calculate screen position and scale based on distance
            scale = 200 / distance  # Adjust based on how far the enemy is
            enemy_x = screen_width / 2 + (angle / fov) * screen_width  # Screen position of the enemy
            enemy_y = screen_height / 2 - scale // 2  # Center enemy vertically

            # Scale the enemy sprite based on distance
            scaled_texture = pygame.transform.scale(self.texture, (int(scale), int(scale)))
            
            # Draw the enemy
            screen.blit(scaled_texture, (enemy_x - scale // 2, enemy_y))