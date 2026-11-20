import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Slither")
# Updating the window presents the pixels drawn on the display surface.
pygame.display.update()
finished = False
while not finished:
    # Draining the event queue keeps keyboard and window-close events responsive.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
raise SystemExit
