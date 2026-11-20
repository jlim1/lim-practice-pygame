import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
screen = pygame.display.set_mode((800, 600))
screen.fill(blue)
Pix = pygame.PixelArray(screen)
Pix[10][10] = green
while True:
    # Draining the event queue keeps keyboard and window-close events responsive.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    # Updating the window presents the pixels drawn on the display surface.
    pygame.display.update()
