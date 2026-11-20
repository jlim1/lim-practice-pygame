import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")
finished = False
lead_x = display_width / 2
lead_y = display_height / 2
velocity_x = 0
velocity_y = 0
clock = pygame.time.Clock()
block_size = 10
FPS = 30
while not finished:
    # Draining the event queue keeps keyboard and window-close events responsive.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x = -block_size
                velocity_y = 0
            elif event.key == pygame.K_RIGHT:
                velocity_x = block_size
                velocity_y = 0
            elif event.key == pygame.K_UP:
                velocity_y = -block_size
                velocity_x = 0
            elif event.key == pygame.K_DOWN:
                velocity_y = block_size
                velocity_x = 0
    if (
        lead_x >= display_width
        or lead_x < 0
        or lead_y >= display_height
        or (lead_y < 0)
    ):
        finished = True
    lead_x += velocity_x
    lead_y += velocity_y
    screen.fill(white)
    pygame.draw.rect(screen, black, [lead_x, lead_y, block_size, block_size])
    # Updating the window presents the pixels drawn on the display surface.
    pygame.display.update()
    # The clock limits the number of frames drawn per second.
    clock.tick(FPS)
pygame.quit()
raise SystemExit
