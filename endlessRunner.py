import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(100, HEIGHT - 100, 50, 50)
enemy = pygame.Rect(-30, HEIGHT - 100, 50, 50)

gravity = 0
jumping = False

# Ground
ground_y = HEIGHT - 50

# Obstacles
obstacles = []
spawn_timer = 0

# Score
score = 0
start_ticks = pygame.time.get_ticks()

# Game Loop
running = True
while running:
    screen.fill(WHITE)

    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        gravity = -15
        jumping = True

    # Player physics
    gravity += 1
    player.y += gravity
    if player.bottom >= ground_y:
        player.bottom = ground_y
        gravity = 0
        jumping = False

    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen,(0,0,255), enemy)

    # Obstacles logic
    spawn_timer += 1
    if spawn_timer > 60:
        spawn_timer = 0
        obstacle = pygame.Rect(WIDTH, ground_y - 30, 30, 30)
        obstacles.append(obstacle)

    for obstacle in obstacles[:]:
        obstacle.x -= 6
        pygame.draw.rect(screen, (255, 0, 0), obstacle)
        if obstacle.right < 0:
            obstacles.remove(obstacle)
        if player.colliderect(obstacle):
            running = False  # Game over

    # Ground
    pygame.draw.line(screen, BLACK, (0, ground_y), (WIDTH, ground_y), 4)

    # Score
    score = (pygame.time.get_ticks() - start_ticks) // 100
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    # Refresh
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
