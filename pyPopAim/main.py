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
gamerounds = 0
size = 5


def randomCords():
    timesRandom = random.randint(0, 100)
    x_pos = 250  # random.randint(int(WIDTH / 100)) * timesRandom
    y_pos = 255  # random.randint(int(HEIGHT / 100)) * timesRandom


# Setting up the circle
def circleCreation():
    timesRandom = random.randint(0, 100)
    x_pos = 250 * timesRandom  # random.randint(int(WIDTH / 100), int(HEIGHT / 100))
    y_pos = 130 * timesRandom  # random.randint(int(WIDTH / 100), int(HEIGHT / 100))

    dot = (pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), 5),)
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
    firsdot = (pygame.draw.circle(screen, (255, 0, 0), (250, 175), size),)
    if gamerounds == 5:
        size += 3
    """ screenDot = 0
    if screenDot < 5:
        x_pos = random.randint(int(WIDTH / 100), 100)
        y_pos = random.randint(int(WIDTH / 100), 100)
        circleCreation()
        screenDot += 1
 """
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    gamerounds += 1
    if gamerounds > 5:
        gamerounds = 0

pygame.quit()
