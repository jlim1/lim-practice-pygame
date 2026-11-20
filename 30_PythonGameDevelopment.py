from pathlib import Path
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
img = pygame.image.load(str(Path(__file__).resolve().with_name("snakehead2.png")))
clock = pygame.time.Clock()
block_size = 20
FPS = 15
direction = "right"
font = pygame.font.SysFont(None, 25)


def snake(block_size, snakelist):
    if direction == "right":
        # The rotated sprite faces the direction of travel.
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    screen.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(screen, green, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return (textSurface, textSurface.get_rect())


def message_to_screen(msg, color):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (display_width / 2, display_height / 2)
    screen.blit(textSurf, textRect)


def play():
    global direction
    finished = False
    game_over = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    velocity_x = 10
    velocity_y = 0
    segments = []
    length = 1
    apple_x = round(random.randrange(0, display_width - block_size))
    apple_y = round(random.randrange(0, display_height - block_size))
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
                    game_over = False
                    finished = True
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
                    direction = "left"
                    velocity_x = -block_size
                    velocity_y = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    velocity_x = block_size
                    velocity_y = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    velocity_y = -block_size
                    velocity_x = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
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
        apple_size = 30
        pygame.draw.rect(screen, red, [apple_x, apple_y, apple_size, apple_size])
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        segments.append(snakeHead)
        if len(segments) > length:
            del segments[0]
        for eachSegment in segments[:-1]:
            if eachSegment == snakeHead:
                game_over = True
        snake(block_size, segments)
        pygame.display.update()
        if (
            lead_x > apple_x
            and lead_x < apple_x + apple_size
            or (
                lead_x + block_size > apple_x
                and lead_x + block_size < apple_x + apple_size
            )
        ):
            if lead_y > apple_y and lead_y < apple_y + apple_size:
                apple_x = round(random.randrange(0, display_width - block_size))
                apple_y = round(random.randrange(0, display_height - block_size))
                length += 1
            elif (
                lead_y + block_size > apple_y
                and lead_y + block_size < apple_y + apple_size
            ):
                apple_x = round(random.randrange(0, display_width - block_size))
                apple_y = round(random.randrange(0, display_height - block_size))
                length += 1
        # The clock limits the number of frames drawn per second.
        clock.tick(FPS)
    pygame.quit()
    raise SystemExit


# Returning from a lost round starts a new round with fresh local state.
while True:
    play()
