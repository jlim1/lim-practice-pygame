import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Slither")
finished = False
while not finished:
    # Draining the event queue keeps keyboard and window-close events responsive.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill(white)
    pygame.draw.rect(screen, black, [400, 300, 10, 10])
    screen.fill(red, rect=[200, 200, 50, 50])
    # Updating the window presents the pixels drawn on the display surface.
    pygame.display.update()
pygame.quit()
raise SystemExit
