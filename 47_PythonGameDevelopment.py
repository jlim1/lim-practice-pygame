import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Menu Practice")
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (200, 200, 0)
green = (34, 177, 76)
clock = pygame.time.Clock()
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    screen.blit(text, [0, 0])


def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return (textSurface, textSurface.get_rect())


def text_to_button(
    msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"
):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (buttonx + buttonwidth / 2, buttony + buttonheight / 2)
    screen.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    screen.blit(textSurf, textRect)


def pause():
    paused = True
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue playing or Q to quit", black, 25)
    # Updating the window presents the pixels drawn on the display surface.
    pygame.display.update()
    while paused:
        # Draining the event queue keeps keyboard and window-close events responsive.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    raise SystemExit
        # The clock limits the number of frames drawn per second.
        clock.tick(5)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    raise SystemExit
        screen.fill(white)
        message_to_screen("Welcome to Menu Practice!", green, -100, size="large")
        message_to_screen("Explore the game menu", black, -30)
        message_to_screen("and try its controls.", black, 10)
        message_to_screen(
            "Close the window to exit.", black, 50
        )
        pygame.draw.rect(screen, green, (150, 500, 100, 50))
        pygame.draw.rect(screen, yellow, (350, 500, 100, 50))
        pygame.draw.rect(screen, red, (550, 500, 100, 50))
        text_to_button("play", black, 150, 500, 100, 50)
        text_to_button("controls", black, 350, 500, 100, 50)
        text_to_button("quit", black, 550, 500, 100, 50)
        pygame.display.update()
        clock.tick(15)


game_intro()


def play():
    finished = False
    game_over = False
    FPS = 15
    while not finished:
        if game_over == True:
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            # The loss screen waits for the player to restart or exit.
            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            play()
                        elif event.key == pygame.K_q:
                            finished = True
                            game_over = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()
        screen.fill(white)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    raise SystemExit


play()
