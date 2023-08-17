# Example file showing a basic pygame "game loop"
import pygame
import random
import os

# pygame setup
WIDTH = 1280
HEIGHT = 720

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

x1 = 300
y1 = 300

x1Change = 0
y1Change = 0

TAIL = 10

RED = (255, 0, 0)
BLUE = (0, 255, 0)

COL = BLUE
SCORE = 0


rect_1 = pygame.Rect(x1, y1, TAIL, 10)


ost = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 10, 10)

while running:
    font = pygame.font.Font(None, 36)
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

    # Things to happen

    if rect_1.colliderect(ost):
        COL = RED
        ost = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 10, 10)
        TAIL += 10
        oldRect = rect_1.copy()
        rect_1.update(x1, y1, TAIL, 10)
        SCORE += 1
        print(f"Yes you hit a Cheese and now have {SCORE} Point. Good Job")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, COL, rect_1)
    pygame.draw.rect(screen, (255, 255, 0), ost)
    # Draw the score to the screen
    score_text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(30)  # limits FPS to 60

pygame.quit()
