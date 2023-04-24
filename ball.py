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


def collided(self):
    new_x = self.rect_x + (self.dir[0] * BALL_SPEED)
    new_y = self.rect_y + (self.dir[1] * BALL_SPEED)
    new_ball_rect = pygame.Rect(new_x, new_y, BALL_RADIUS * 2, BALL_RADIUS * 2)
    if new_ball_rect.collidelist(self.level.bounds_rects) != -1:
        return True
    else:
        return False


class Ball:
    def __init__(self, level, row, col, dir):
        self.level = level
        self.row = row
        self.col = col
        self.dir = dir
        self.rect_x = self.row * SCL + (SCL // 2) - BALL_RADIUS
        self.rect_y = self.col * SCL + (SCL // 2) - BALL_RADIUS

    def draw(self, screen):
        center = (self.rect_x + BALL_RADIUS, self.rect_y + BALL_RADIUS)
        pygame.draw.circle(screen, BALL_COLOR, center, BALL_RADIUS)

    def move(self):
        if collided(self):
            self.dir = switch_dir(self.dir)
        self.rect_x += self.dir[0] * BALL_SPEED
        self.rect_y += self.dir[1] * BALL_SPEED
