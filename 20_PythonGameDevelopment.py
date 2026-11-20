import pygame
import time
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")
clock = pygame.time.Clock()
block_size = 10
FPS = 30
font = pygame.font.SysFont(None, 25)


def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(screen, green, [XnY[0], XnY[1], block_size, block_size])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [display_width / 2, display_height / 2])


def play():
    finished = False
    game_over = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    velocity_x = 0
    velocity_y = 0
    segments = []
    length = 10
    apple_x = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    apple_y = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
    while not finished:
        # The loss screen waits for the player to restart or exit.
        while game_over:
            screen.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            # Updating the window presents the pixels drawn on the display surface.
            pygame.display.update()
            # Draining the event queue keeps keyboard and window-close events responsive.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        finished = True
                        game_over = False
                    if event.key == pygame.K_c:
                        return
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
            game_over = True
        lead_x += velocity_x
        lead_y += velocity_y
        screen.fill(white)
        pygame.draw.rect(screen, red, [apple_x, apple_y, block_size, block_size])
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        segments.append(snakeHead)
        if len(segments) > length:
            del segments[0]
        snake(block_size, segments)
        pygame.display.update()
        if lead_x == apple_x and lead_y == apple_y:
            apple_x = (
                round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            )
            apple_y = (
                round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            )
        # The clock limits the number of frames drawn per second.
        clock.tick(FPS)
    pygame.quit()
    raise SystemExit


# Returning from a lost round starts a new round with fresh local state.
while True:
    play()
