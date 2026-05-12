import pygame

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Sprite class
class Box(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.image = pygame.Surface((80, 80))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_color(self, color):
        self.image.fill(color)

# Create sprites
sprite1 = Box(RED, 100, 150)
sprite2 = Box(BLUE, 400, 150)

# Group
sprites = pygame.sprite.Group()
sprites.add(sprite1)
sprites.add(sprite2)

# Custom event
CHANGE_COLOR = pygame.USEREVENT + 1

pygame.time.set_timer(CHANGE_COLOR, 2000)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Custom event
        if event.type == CHANGE_COLOR:
            sprite1.change_color((0, 255, 0))
            sprite2.change_color((255, 255, 0))

    # Draw
    screen.fill(WHITE)

    sprites.draw(screen)

    pygame.display.update()

pygame.quit()