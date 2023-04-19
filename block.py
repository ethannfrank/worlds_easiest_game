import math

import pygame

from settings import *


def collide_wall(screen, level, block_rect, dir):
    collide_lines = level.lines
    future_block_rect = block_rect
    # n
    if dir == [0, -1]:
        future_block_rect = pygame.Rect(block_rect.x, block_rect.y - BLOCK_COLLISION,
                                        block_rect.width, block_rect.height)
    # ne
    elif dir == [1, -1]:
        future_block_rect = pygame.Rect(block_rect.x, block_rect.y - BLOCK_COLLISION,
                                        block_rect.width + BLOCK_COLLISION, block_rect.height)
    # e
    elif dir == [1, 0]:
        future_block_rect = pygame.Rect(block_rect.x, block_rect.y,
                                        block_rect.width + BLOCK_COLLISION, block_rect.height)
    # se
    elif dir == [1, 1]:
        future_block_rect = pygame.Rect(block_rect.x, block_rect.y,
                                        block_rect.width + BLOCK_COLLISION, block_rect.height + BLOCK_COLLISION)
    # s
    elif dir == [0, 1]:
        future_block_rect = pygame.Rect(block_rect.x, block_rect.y,
                                        block_rect.width, block_rect.height + BLOCK_COLLISION)
    # sw
    elif dir == [-1, 1]:
        future_block_rect = pygame.Rect(block_rect.x - BLOCK_COLLISION, block_rect.y,
                                        block_rect.width, block_rect.height + BLOCK_COLLISION)
    # w
    elif dir == [-1, 0]:
        future_block_rect = pygame.Rect(block_rect.x - BLOCK_COLLISION, block_rect.y,
                                        block_rect.width, block_rect.height)
    # nw
    elif dir == [-1, 1]:
        future_block_rect = pygame.Rect(block_rect.x - BLOCK_COLLISION, block_rect.y - BLOCK_COLLISION,
                                        block_rect.width, block_rect.height)
    for line in collide_lines:
        pygame.draw.line(screen, BLACK, (line[0][0] * SCL, line[0][1] * SCL), (line[1][0] * SCL, line[1][1] * SCL))
        if future_block_rect.clipline((line[0][0] * SCL, line[0][1] * SCL), (line[1][0] * SCL, line[1][1] * SCL)):
            return True
    return False


def collide_block(level, block_rect):
    for ball in level.balls:
        ball_collide_rect = pygame.Rect(ball.rect_x, ball.rect_y, BALL_RADIUS * 2, BALL_RADIUS * 2)
        if block_rect.colliderect(ball_collide_rect):
            return True
    return False


def win(level, block_rect):
    win_rect = pygame.Rect(level.win[0] * SCL, level.win[1] * SCL, SCL, SCL)
    if block_rect.colliderect(win_rect):
        print("win")


def update_score(self, level, screen):
    x_center = self.x + (SCL // 2)
    y_center = self.y + (SCL // 2)
    level = level
    for checkpoint in level.checkpoints:
        checkpoint_center = [checkpoint[0] * SCL + (SCL // 2), checkpoint[1] * SCL + (SCL // 2)]
        pygame.draw.line(screen, WHITE, (x_center, y_center), (checkpoint_center[0], checkpoint_center[1]))
        self.score = math.hypot(x_center - checkpoint_center[0], y_center - checkpoint_center[1])


class Block:
    def __init__(self, level):
        self.block_rect = None
        self.score = []
        self.level = level
        self.x = level.spawn[0] * SCL
        self.y = level.spawn[1] * SCL
        self.move_set = []

    def update(self, screen, dir):
        self.block_rect = pygame.Rect(self.x + (SCL - BLOCK_SIZE) // 2, self.y + (SCL - BLOCK_SIZE) // 2,
                                      BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, RED, self.block_rect)
        if not collide_wall(screen, self.level, self.block_rect, dir):
            self.x += dir[0] * BLOCK_SPEED
            self.y += dir[1] * BLOCK_SPEED
