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
    dir = [0, 0]
    # up
    if keys[pygame.K_w]:
        dir[1] = -1
    # down
    if keys[pygame.K_s]:
        dir[1] = 1
    # right
    if keys[pygame.K_d]:
        dir[0] = 1
    # left
    if keys[pygame.K_a]:
        dir[0] = -1
    return dir


def random_movement(block):
    dir = [random.randint(-1, 1), random.randint(-1, 1)]
    block.move_set.append(dir)
    return dir


def show_f3(clock):
    fps = "FPS: " + str(round(clock.get_fps()))
    pixel = "Pixel: [" + str(pygame.mouse.get_pos()[0]) + ", " + str(pygame.mouse.get_pos()[1]) + "]"
    row_col = "Row Col: [" + str(pygame.mouse.get_pos()[0] // SCL) + ", " + str(pygame.mouse.get_pos()[1] // SCL) + "]"
    fps_surface = FONT.render(fps, True, WHITE)
    pixel_surface = FONT.render(pixel, True, WHITE)
    row_col_surface = FONT.render(row_col, True, WHITE)
    SCREEN.blit(fps_surface, (5, 305))
    SCREEN.blit(pixel_surface, (5, 317))
    SCREEN.blit(row_col_surface, (5, 329))


def update():
    SCREEN.fill(BACKGROUND_COLOR)
    MAP.update(SCREEN)
    for ball in MAP.level.balls:
        ball.update(SCREEN)
    BLOCK.update(SCREEN, manual_movement())
    win(MAP.level, BLOCK.block_rect)
    update_score(BLOCK, MAP.level, SCREEN)
    # if collide_block(MAP.level, BLOCK.block_rect):
    #     pass
    show_f3(CLOCK)
    pygame.display.update()


def game_loop():
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        update()


if __name__ == "__main__":
    game_loop()
