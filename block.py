import pygame

from settings import *


def collided(self, dir):
    new_x = self.x + (dir[0] * BLOCK_SPEED)
    new_y = self.y + (dir[1] * BLOCK_SPEED)
    new_block_rect = pygame.Rect(new_x + (SCL - BLOCK_SIZE) // 2, new_y + (SCL - BLOCK_SIZE) // 2,
                                 BLOCK_SIZE, BLOCK_SIZE)
    if new_block_rect.collidelist(self.level.bounds_rects) != -1:
        return True
    else:
        return False


class Block:
    def __init__(self, level):
        self.block_rect = None
        self.score = []
        self.level = level
        self.x = level.spawn[0] * SCL
        self.y = level.spawn[1] * SCL
        self.move_set = []

    def draw(self, screen):
        self.block_rect = pygame.Rect(self.x + (SCL - BLOCK_SIZE) // 2, self.y + (SCL - BLOCK_SIZE) // 2,
                                      BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, RED, self.block_rect)

    def move(self, dir):
        if not collided(self, dir):
            self.x += dir[0] * BLOCK_SPEED
            self.y += dir[1] * BLOCK_SPEED
