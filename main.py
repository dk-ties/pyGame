# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


def ost():
    pygame.draw.circle(screen, (255, 0, 0), (50, 300), 10)


rect_1 = pygame.Rect(200, 100, 150, 100)


def redSnake(x, y):
    redSnake = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 15, 15))

    # rect = pygame.Rect(x, y, width, height)

    def moveSnake(snake, x, y):
        pygame.Rect.move(snake, x, y)


# activeSnake = redSnake(150, 250)

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

    pygame.draw.rect(screen, (255, 0, 0), rect_1)
    # screen.blit(rect_1)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        rect_1.x += 5
    if key[pygame.K_d] == True:
        rect_1.move_ip(5, 0)
    if key[pygame.K_w] == True:
        rect_1.move_ip(0, -5)
    if key[pygame.K_s] == True:
        rect_1.move_ip(0, 5)

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
