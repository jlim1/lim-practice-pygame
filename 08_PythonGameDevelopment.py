import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Slither")
finished = False
lead_x = 300
lead_y = 300
velocity_x = 0
while not finished:
    # Draining the event queue keeps keyboard and window-close events responsive.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x = -10
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
    lead_x += velocity_x
    screen.fill(white)
    pygame.draw.rect(screen, black, [lead_x, lead_y, 10, 10])
    # Updating the window presents the pixels drawn on the display surface.
    pygame.display.update()
pygame.quit()
raise SystemExit
