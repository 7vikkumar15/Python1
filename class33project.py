import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Add Sprites")

# Sprite positions
x1, y1 = 100, 150
x2, y2 = 300, 150
speed = 5

running = True
while running:
    screen.fill((0, 0, 0))

    # Keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x1 -= speed
    if keys[pygame.K_RIGHT]:
        x1 += speed
    if keys[pygame.K_UP]:
        y1 -= speed
    if keys[pygame.K_DOWN]:
        y1 += speed

    # Draw sprites
    pygame.draw.rect(screen, (255, 0, 0), (x1, y1, 50, 50))
    pygame.draw.rect(screen, (0, 255, 0), (x2, y2, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()