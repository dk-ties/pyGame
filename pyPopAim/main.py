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
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
cords = None


COLOR = RED


def randomCords():
    timesRandom = random.randint(0, 100)
    x_pos = 250  # random.randint(int(WIDTH / 100)) * timesRandom
    y_pos = 255  # random.randint(int(HEIGHT / 100)) * timesRandom
    # timesRandom = random.randint(0, 100)
    # x_pos = 250 * timesRandom  # random.randint(int(WIDTH / 100), int(HEIGHT / 100))
    #  y_pos = 130 * timesRandom  # random.randint(int(WIDTH / 100), int(HEIGHT / 100))
    cords = (x_pos, y_pos)
    return cords


rect_1 = pygame.Rect(0, 0, 25, 25)
rectMouse = pygame.Rect(0, 0, 25, 25)


# Setting up the circle
def circleCreation():
    timesRandom = random.randint(0, 100)
    x_pos = 250 * timesRandom  # random.randint(int(WIDTH / 100), int(HEIGHT / 100))
    y_pos = 130 * timesRandom  # random.randint(int(WIDTH / 100), int(HEIGHT / 100))

    dot = (pygame.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), 5),)
    return dot


while running:
    if cords == None:
        cords = randomCords()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mousePos = pygame.mouse.get_pos()
    rectMouse.center = mousePos

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    print("Igot this far", cords)
    firstdot = (pygame.draw.circle(screen, COLOR, cords, size),)
    pygame.draw.rect(screen, COLOR, rect_1)
    pygame.draw.rect(screen, COLOR, rectMouse)
    if gamerounds == 5:
        size += 3
    """ screenDot = 0
    if screenDot < 5:
        x_pos = random.randint(int(WIDTH / 100), 100)
        y_pos = random.randint(int(WIDTH / 100), 100)
        circleCreation()
        screenDot += 1
 """
    # Check for collidition
    if rectMouse.colliderect(firstdot):
        COLOR = GREEN
        size = 5

        isHit = True
        if isHit == True:
            cords = randomCords()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    gamerounds += 1
    if gamerounds > 5:
        gamerounds = 0

pygame.quit()
