import pygame

from settings import *


class Map:
    def __init__(self, level):
        self.level = level

    def update(self, screen):
        for x in range(self.level.rows):
            for y in range(self.level.cols):
                rect = pygame.Rect(y * SCL, x * SCL, SCL, SCL)
                # blank cell
                # if self.level.arr[x][y] == 0:
                #     pygame.draw.rect(screen, ZERO_COLOR, rect)
                # darker cell
                if self.level.arr[x][y] == 1:
                    pygame.draw.rect(screen, ONE_COLOR, rect)
                # lighter cell
                elif self.level.arr[x][y] == 2:
                    pygame.draw.rect(screen, TWO_COLOR, rect)
                # spawn cell
                elif self.level.arr[x][y] == 3:
                    pygame.draw.rect(screen, THREE_COLOR, rect)
