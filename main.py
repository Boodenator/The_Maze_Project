import pygame
from math import pi, cos, sin, atan2, hypot
from maze import maze
from player import Player
from enemy import Enemy

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FOV = pi / 3  # 60 degrees field of view
NUM_RAYS = 120  # Number of rays cast
MAX_DEPTH = 800  # Max depth for rendering walls
WALL_HEIGHT = 60  # Wall height for 3D effect

# Load textures
WALL_TEXTURE = pygame.image.load('wall.jpg')
GUN_IMAGE = pygame.image.load('gun.jpg')  # Gun image

# Define colors
SKY_COLOR = (135, 206, 235)  # Baby blue for the sky
GROUND_COLOR = (34, 139, 34)  # Green for the ground

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load shooting sound
SHOOT_SOUND = pygame.mixer.Sound('shoot_sound.wav')  # Optional sound for shooting

# Create a list of enemies
enemies = [
    Enemy(200, 200, 'enemy.png'),  # Add enemy sprites
    Enemy(400, 400, 'enemy.png')
]

def cast_rays(player, maze):
    rays = []
    for ray in range(NUM_RAYS):
        ray_angle = (player.angle - FOV / 2) + (ray / NUM_RAYS) * FOV
        for depth in range(MAX_DEPTH):
            target_x = player.x + cos(ray_angle) * depth
            target_y = player.y + sin(ray_angle) * depth

            # Check for wall hit in the maze
            if maze[int(target_y / WALL_HEIGHT)][int(target_x / WALL_HEIGHT)] == 1:
                rays.append((depth, ray_angle))  # Store both depth and angle
                break
    return rays

def draw_walls(screen, rays):
    wall_width = SCREEN_WIDTH // NUM_RAYS
    for i, (depth, ray_angle) in enumerate(rays):
        wall_height = min(SCREEN_HEIGHT, WALL_HEIGHT * SCREEN_HEIGHT / (depth + 0.0001))
        
        # Calculate texture slice
        texture_x = int((ray_angle % (2 * pi)) / (2 * pi) * WALL_TEXTURE.get_width())
        texture_slice = WALL_TEXTURE.subsurface(texture_x, 0, 1, WALL_TEXTURE.get_height())
        texture_slice = pygame.transform.scale(texture_slice, (wall_width, int(wall_height)))

        # Draw wall slice
        screen.blit(texture_slice, (i * wall_width, (SCREEN_HEIGHT - wall_height) // 2))

def draw_sky_and_ground(screen):
    # Fill the top half with sky color (baby blue)
    screen.fill(SKY_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 2))
    
    # Fill the bottom half with ground color (green)
    screen.fill(GROUND_COLOR, (0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2))

def draw_gun(screen):
    # Scale gun image and position it at the bottom center
    gun_scaled = pygame.transform.scale(GUN_IMAGE, (150, 150))  # Adjust gun size as needed
    screen.blit(gun_scaled, (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 150))  # Adjust positioning

def handle_shooting(player, rays, enemies):
    """Simulate shooting when the spacebar or mouse is clicked."""
    for ray in rays:
        depth, ray_angle = ray
        if depth < MAX_DEPTH:
            print("Hit detected at depth:", depth)
            # Check if any enemy is within shooting range
            for enemy in enemies:
                if enemy.alive:
                    enemy_distance = enemy.distance_to_player(player)
                    enemy_angle = enemy.angle_to_player(player)

                    if abs(enemy_angle - player.angle) < 0.1 and enemy_distance < depth:
                        print(f"Enemy hit at distance {enemy_distance}")
                        enemy.alive = False  # Mark the enemy as killed
                        break

            # Play shooting sound
            SHOOT_SOUND.play()

def main():
    running = True
    player = Player()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys, maze)

        screen.fill((0, 0, 0))  # Clear the screen with black

        # 1. Draw the sky and ground (it needs to be rendered first)
        draw_sky_and_ground(screen)

        # 2. Cast rays and draw the walls
        rays = cast_rays(player, maze)
        draw_walls(screen, rays)

        # 3. Draw enemies
        for enemy in enemies:
            enemy.draw(screen, player, SCREEN_WIDTH, SCREEN_HEIGHT, FOV)

        # 4. Draw the gun after the walls
        draw_gun(screen)

        # Handle shooting mechanics
        if keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:  # Spacebar or mouse click
            handle_shooting(player, rays, enemies)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()