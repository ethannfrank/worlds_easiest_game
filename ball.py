import pygame.draw

from settings import *


def switch_dir(dir):
    # up -> down
    if dir == (0, 1):
        return 0, -1
    # down -> up
    if dir == (0, -1):
        return 0, 1
    # right -> left
    if dir == (1, 0):
        return -1, 0
    # left -> right
    if dir == (-1, 0):
        return 1, 0


def collide(screen, level, ball_rect):
    collide_lines = level.lines
    for line in collide_lines:
        pygame.draw.line(screen, BLACK, (line[0][0] * SCL, line[0][1] * SCL), (line[1][0] * SCL, line[1][1] * SCL))
        if ball_rect.clipline((line[0][0] * SCL, line[0][1] * SCL), (line[1][0] * SCL, line[1][1] * SCL)):
            return True
    return False


class Ball:
    def __init__(self, level, row, col, dir):
        self.level = level
        self.row = row
        self.col = col
        self.dir = dir
        self.rect_x = self.row * SCL + (SCL // 2) - BALL_RADIUS
        self.rect_y = self.col * SCL + (SCL // 2) - BALL_RADIUS

    def update(self, screen):
        center = (self.rect_x + BALL_RADIUS, self.rect_y + BALL_RADIUS)
        pygame.draw.circle(screen, BALL_COLOR, center, BALL_RADIUS)
        ball_collide_rect = pygame.Rect(self.rect_x, self.rect_y, BALL_RADIUS * 2, BALL_RADIUS * 2)
        # red ball_collide_rect
        # pygame.draw.rect(screen, RED, ball_collide_rect)
        if collide(screen, self.level, ball_collide_rect):
            self.dir = switch_dir(self.dir)
        self.rect_x += self.dir[0] * BALL_SPEED
        self.rect_y += self.dir[1] * BALL_SPEED
