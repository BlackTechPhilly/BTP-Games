import pygame
import sys

# ============================
# Step 1: Initialize Pygame
# ============================
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Mini Mario Style Game")

# ============================
# Step 2: Define Colors
# ============================
WHITE = (255, 255, 255)
BLUE = (66, 135, 245)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# ============================
# Step 3: Classes
# ============================

class Player:
    def __init__(self, x, y):
        self.width = 100
        self.height = 60
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.vel = [0, 0]
        self.speed = 5
        self.jump_power = -15
        self.gravity = 1
        self.on_ground = False
        self.health = 100

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.vel[0] = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel[0] = self.speed
        else:
            self.vel[0] = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel[1] = self.jump_power
            self.on_ground = False

    def apply_physics(self, platforms):
        self.vel[1] += self.gravity
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

        self.on_ground = False
        for plat in platforms:
            if self.rect.colliderect(plat):
                if self.vel[1] > 0 and self.rect.bottom <= plat.top + self.vel[1]:
                    self.rect.bottom = plat.top
                    self.vel[1] = 0
                    self.on_ground = True

    def draw(self, surface, scroll_x):
        pygame.draw.rect(surface, BLUE, (self.rect.x - scroll_x, self.rect.y, self.width, self.height))


class Enemy:
       
    def __init__(self, x, y, width=40, height=40):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 10
        self.health = 30
        
    def draw(self, surface, scroll_x):
        pygame.draw.rect(surface, RED, (self.rect.x - scroll_x, self.rect.y, self.rect.width, self.rect.height))


# ============================
# Step 4: Platforms
# ============================
platforms = [
    pygame.Rect(0, HEIGHT - 40, 2000, 40),
    pygame.Rect(300, HEIGHT - 150, 100, 20),
    pygame.Rect(500, HEIGHT - 250, 100, 20),
    pygame.Rect(750, HEIGHT - 180, 150, 20),
    pygame.Rect(1000, HEIGHT - 300, 100, 20)
]

# ============================
# Step 5: Create Player and Enemies
# ============================
player = Player(100, HEIGHT - 150)
enemies = [Enemy(600, HEIGHT - 100), Enemy(1100, HEIGHT - 340)]

# ============================
# Step 6: Game Loop
# ============================
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # ============================
    # Step 7: Event Handling
    # ============================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ============================
    # Step 8: Input
    # ============================
    keys = pygame.key.get_pressed()
    player.handle_input(keys)

    # ============================
    # Step 9: Physics
    # ============================
    player.apply_physics(platforms)

    # ============================
    # Step 10: Enemy Collision
    # ============================
    for enemy in enemies[:]:
        if player.rect.colliderect(enemy.rect):
            if player.vel[1] > 0 and player.rect.bottom <= enemy.rect.top + player.vel[1]:
                enemies.remove(enemy)
                player.vel[1] = player.jump_power // 2  # Bounce

    # ============================
    # Step 11: Camera Scroll
    # ============================
    scroll_x = player.rect.x - WIDTH // 2

    # ============================
    # Step 12: Drawing
    # ============================
    for plat in platforms:
        pygame.draw.rect(screen, GREEN, (plat.x - scroll_x, plat.y, plat.width, plat.height))

    for enemy in enemies:
        enemy.draw(screen, scroll_x)

    player.draw(screen, scroll_x)

    pygame.display.flip()
