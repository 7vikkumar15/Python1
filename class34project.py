import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader - Part 1")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.SysFont("Arial", 36)

# Score
score = 0

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce from walls
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

# Create player
player = Sprite(BLUE, 50, 50)
player.rect.x = WIDTH // 2
player.rect.y = HEIGHT // 2

# Create enemies
enemies = pygame.sprite.Group()

for i in range(7):
    enemy = Sprite(RED, 40, 40)
    enemy.rect.x = random.randint(0, WIDTH - 40)
    enemy.rect.y = random.randint(0, HEIGHT - 40)
    enemies.add(enemy)

# All sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemies)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.rect.x -= 5

    if keys[pygame.K_RIGHT]:
        player.rect.x += 5

    if keys[pygame.K_UP]:
        player.rect.y -= 5

    if keys[pygame.K_DOWN]:
        player.rect.y += 5

    # Update enemies
    enemies.update()

    # Collision detection
    hits = pygame.sprite.spritecollide(player, enemies, False)

    if hits:
        score += 1

    # Draw everything
    screen.fill(BLACK)

    all_sprites.draw(screen)

    # Score text
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()