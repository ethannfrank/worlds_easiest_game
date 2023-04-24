import pygame

from settings import *


class Map:
    def __init__(self, level):
        self.level = level
        self.board_rects = []

    def update(self, screen):
        colors = {0: ZERO_COLOR, 1: ONE_COLOR, 2: TWO_COLOR, 3: THREE_COLOR}

        for x in range(len(self.level.arr)):
            for y in range(len(self.level.arr[0])):
                if self.level.arr[x][y] != 0:
                    rect = pygame.Rect(y * SCL, x * SCL, SCL, SCL)
                    self.board_rects.append(rect)
                    pygame.draw.rect(screen, colors[self.level.arr[x][y]], rect)

        # draw bounds rects
        # for bound_rect in self.level.bounds_rects:
        #     pygame.draw.rect(screen, RED, bound_rect)
