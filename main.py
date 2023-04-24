import random
import sys

from map import *
from levels import *
from block import *

pygame.init()

# window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World's Easiest Game")
# clock
CLOCK = pygame.time.Clock()
# font
FONT = pygame.font.Font(None, 18)
# map
MAP = Map(TestingLevel())
# blocks
BLOCK = Block(MAP.level)


def manual_movement():
    keys = pygame.key.get_pressed()
    x_dir = keys[pygame.K_d] - keys[pygame.K_a]  # calculate the x direction using subtraction
    y_dir = keys[pygame.K_s] - keys[pygame.K_w]  # calculate the y direction using subtraction
    return [x_dir, y_dir]


def random_movement():
    dir = [random.randint(-1, 1), random.randint(-1, 1)]
    return dir


def show_f3(clock):
    fps = "FPS: " + str(round(clock.get_fps()))
    pixel = "Pixel: [" + str(pygame.mouse.get_pos()[0]) + ", " + str(pygame.mouse.get_pos()[1]) + "]"
    row_col = "Row Col: [" + str(pygame.mouse.get_pos()[0] // SCL) + ", " + str(pygame.mouse.get_pos()[1] // SCL) + "]"
    fps_surface = FONT.render(fps, True, WHITE)
    pixel_surface = FONT.render(pixel, True, WHITE)
    row_col_surface = FONT.render(row_col, True, WHITE)
    SCREEN.blit(fps_surface, (55, 305))
    SCREEN.blit(pixel_surface, (55, 317))
    SCREEN.blit(row_col_surface, (55, 329))


def load_map():
    global MAP
    MAP = Map(TestingLevel())


def update():
    # bg
    SCREEN.fill(BACKGROUND_COLOR)
    # map
    MAP.update(SCREEN)
    # balls
    for ball in MAP.level.balls:
        ball.draw(SCREEN)
    # block
    BLOCK.draw(SCREEN)
    # draw score line
    update_score(BLOCK, SCREEN)
    show_f3(CLOCK)
    pygame.display.update()


def move():
    for ball in MAP.level.balls:
        ball.move()
    BLOCK.move(manual_movement())


def game_loop():
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        update()
        move()


if __name__ == "__main__":
    load_map()
    game_loop()
