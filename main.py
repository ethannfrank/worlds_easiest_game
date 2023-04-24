import math
import os.path
import random
import sys
import neat
import pygame

from map import *
from levels import *
from block import *

pygame.init()


# font
FONT = pygame.font.Font(None, 18)


def manual_movement():
    keys = pygame.key.get_pressed()
    x_dir = keys[pygame.K_d] - keys[pygame.K_a]  # calculate the x direction using subtraction
    y_dir = keys[pygame.K_s] - keys[pygame.K_w]  # calculate the y direction using subtraction
    return [x_dir, y_dir]


def random_movement():
    dir = [random.randint(-1, 1), random.randint(-1, 1)]
    return dir


def show_f3(screen, clock):
    fps = "FPS: " + str(round(clock.get_fps()))
    pixel = "Pixel: [" + str(pygame.mouse.get_pos()[0]) + ", " + str(pygame.mouse.get_pos()[1]) + "]"
    row_col = "Row Col: [" + str(pygame.mouse.get_pos()[0] // SCL) + ", " + str(pygame.mouse.get_pos()[1] // SCL) + "]"
    fps_surface = FONT.render(fps, True, WHITE)
    pixel_surface = FONT.render(pixel, True, WHITE)
    row_col_surface = FONT.render(row_col, True, WHITE)
    screen.blit(fps_surface, (55, 305))
    screen.blit(pixel_surface, (55, 317))
    screen.blit(row_col_surface, (55, 329))


def draw_lines(screen, block, balls, level):
    ball_dists = []
    block_rect_center = [block.x + (SCL - BLOCK_SIZE) // 2 + (BLOCK_SIZE // 2),
                         block.y + (SCL - BLOCK_SIZE) // 2 + (BLOCK_SIZE // 2)]
    for ball in balls:
        pygame.draw.line(screen, BALL_COLOR, block_rect_center, ball.ball_center)
        line_length = math.hypot(block_rect_center[0] - ball.ball_center[0], block_rect_center[1] - ball.ball_center[1])
        ball_dists.append(line_length)
    end_rect_center = (level.end[0] * SCL + (SCL // 2), level.end[1] * SCL + (SCL // 2))
    pygame.draw.line(screen, THREE_COLOR, block_rect_center, end_rect_center)
    # end_dist = math.hypot(block_rect_center[0] - end_rect_center[0], block_rect_center[1] - end_rect_center[1])


def draw(maze, blocks, screen, clock):
    # bg
    screen.fill(BACKGROUND_COLOR)
    # map
    maze.draw(screen)
    # balls
    for ball in maze.level.balls:
        ball.draw(screen)
    # block
    for block in blocks:
        block.draw(screen)
        if BLOCK_DRAW_LINES:
            draw_lines(screen, block, maze.level.balls, maze.level)
    show_f3(screen, clock)
    pygame.display.update()


def main(genomes, config):
    nets = []
    ge = []
    blocks = []
    maze = Map(TestingLevel())

    for g in genomes:
        net = neat.nn.FeedForwardNetwork(g, config)
        nets.append(net)
        blocks.append(Block(maze.level))
        g.fitness = 0
        ge.append(g)

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("World's Easiest Game")
    CLOCK = pygame.time.Clock()

    score = 0

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw(maze, blocks, SCREEN, CLOCK)
        for ball in maze.level.balls:
            ball.move()
        for x, block in enumerate(blocks):
            block.move(manual_movement())
            for ball in maze.level.balls:
                if block.block_rect.colliderect(pygame.Rect(ball.rect_x, ball.rect_y, BALL_RADIUS * 2, BALL_RADIUS * 2)):
                    ge[x].fitness -= 1
                    blocks.pop(x)
                    nets.pop(x)
                    ge.pop(x)
                end_rect_center = (maze.level.end[0] * SCL + (SCL // 2), maze.level.end[1] * SCL + (SCL // 2))


main(None, None)


def run(path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter)

    # winner = p.run(, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
