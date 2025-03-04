import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 500, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBJECT_WIDTH, OBJECT_HEIGHT = 50, 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Falling Objects")

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - PLAYER_HEIGHT - 10
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

class FallingObject:
    def __init__(self):
        self.x = random.randint(0, WIDTH - OBJECT_WIDTH)
        self.y = -OBJECT_HEIGHT
        self.width = OBJECT_WIDTH
        self.height = OBJECT_HEIGHT
        self.speed = random.randint(3, 7)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.y > HEIGHT

# Game loop
player = Player()
falling_objects = []
score = 0
lives = 3
running = True

while running:
    clock.tick(FPS)
    screen.fill(WHITE)  # Clear screen

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw()

    # Add falling objects periodically
    if random.randint(1, 30) == 1:  # Lower the number to increase difficulty
        falling_objects.append(FallingObject())

    # Update falling objects
    for obj in falling_objects[:]:
        obj.move()
        obj.draw()

        # Check for collision
        if (obj.x < player.x + player.width and
            obj.x + obj.width > player.x and
            obj.y < player.y + player.height and
            obj.y + obj.height > player.y):
            lives -= 1
            falling_objects.remove(obj)  # Remove object on collision

        # Remove objects off screen
        elif obj.off_screen():
            falling_objects.remove(obj)
            score += 1  # Increase score for avoiding

    # Display score and lives
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    # Check game over
    if lives <= 0:
        game_over_text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(2000)  # Pause before quitting
        running = False

    pygame.display.update()  # Refresh screen

pygame.quit()
