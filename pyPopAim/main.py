# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


# Setting up the circle
def circleCreation(x_pos, y_pos):
    dot = pygame.draw.circle(screen, (255, 0, 0), (x_pos * 10, y_pos), 5)
    return dot


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    screenDot = []
    if len(screenDot) < 5:
        x_pos = random.randint(int(WIDTH / 100), 100)
        y_pos = random.randint(int(WIDTH / 100), 100)
        circleCreation(x_pos, y_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()
