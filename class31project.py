import pygame

pygame.init()

# Create window
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("My First Game Screen")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()