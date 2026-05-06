import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Add Elements")

font = pygame.font.SysFont("Arial", 30)

running = True
while running:
    screen.fill((255, 255, 255))  # white background

    # Draw rectangle
    pygame.draw.rect(screen, (255, 0, 0), (150, 150, 200, 100))

    # Add text
    text = font.render("Hello Game!", True, (0, 0, 0))
    screen.blit(text, (170, 180))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()