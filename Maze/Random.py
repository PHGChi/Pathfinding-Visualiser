import pygame
from collections import deque
from random import randint, choice

def Random(grid, draw):
    rows, cols = len(grid), len(grid[0])
    colWalls = rows * cols * 0.08 // rows
    for col in grid:
        walls = randint(colWalls - 3, colWalls)
        idxWalls = set()
        while len(idxWalls) != walls:
            idx = randint(0, len(col) - 1)
            if idx not in idxWalls:
                idxWalls.add(idx)
                col[idx].MakeWall()
                draw()

    grid = 1