# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

x1 = 300
y1 = 300

x1Change = 0
y1Change = 0

RED = (255, 0, 0)
BLUE = (0, 255, 0)

rect_1 = pygame.Rect(x1, y1, 10, 10)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        """ if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Jeg burde flytte")
                pygame.Rect.move(activeSnake, 25, 150) """

    # screen.blit(rect_1)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        rect_1.move_ip(-10, 0)
    if key[pygame.K_d] == True:
        rect_1.move_ip(10, 0)
    if key[pygame.K_w] == True:
        rect_1.move_ip(0, -10)
    if key[pygame.K_s] == True:
        rect_1.move_ip(0, 10)

    y1 += y1Change
    x1 += x1Change

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, RED, rect_1)
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(30)  # limits FPS to 60

pygame.quit()
