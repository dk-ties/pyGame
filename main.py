# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


def ost():
    pygame.draw.circle(screen, (255, 0, 0), (50, 300), 10)


def snake(x, y):
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 15, 15))
    # rect = pygame.Rect(x, y, width, height)


def moveSnake(snake, x, y):
    pygame.Rect.move(snake, x, y)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveSnake(snake, 15, 250)
                print("Jeg burde flytte")

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    # RENDER YOUR GAME HERE
    snake(100, 15)
    ost()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
