import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paceman Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Game variables
pacman_pos = [250, 250]
pacman_speed = 5

ghost_pos = [random.randint(50, 450), random.randint(50, 450)]
ghost_speed = 3

dots = [[random.randint(10, 490), random.randint(10, 490)] for _ in range(10)]

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Pacman movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_pos[0] -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_pos[0] += pacman_speed
    if keys[pygame.K_UP]:
        pacman_pos[1] -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_pos[1] += pacman_speed
    
    # Ghost movement (simple AI)
    if ghost_pos[0] < pacman_pos[0]:
        ghost_pos[0] += ghost_speed
    if ghost_pos[0] > pacman_pos[0]:
        ghost_pos[0] -= ghost_speed
    if ghost_pos[1] < pacman_pos[1]:
        ghost_pos[1] += ghost_speed
    if ghost_pos[1] > pacman_pos[1]:
        ghost_pos[1] -= ghost_speed
    
    # Draw Pacman
    pygame.draw.circle(screen, YELLOW, pacman_pos, 15)
    
    # Draw Ghost
    pygame.draw.circle(screen, RED, ghost_pos, 15)
    
    # Draw Dots
    for dot in dots:
        pygame.draw.circle(screen, WHITE, dot, 5)
    
    # Collision detection for dots
    dots = [dot for dot in dots if (abs(pacman_pos[0] - dot[0]) > 10 or abs(pacman_pos[1] - dot[1]) > 10)]
    
    # Check for game over (ghost collision)
    if abs(pacman_pos[0] - ghost_pos[0]) < 15 and abs(pacman_pos[1] - ghost_pos[1]) < 15:
        print("Game Over!")
        running = False
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
