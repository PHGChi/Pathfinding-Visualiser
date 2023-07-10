import pygame
import math
import sys
from Grid.Node import Node
from Helper.GlobalVariables import *

pygame.init()
font = pygame.font.SysFont('Arial', GAP)

# Create grids to represent nodes
def MakeGrid(rows, width):
  grid = []
  gap = width // rows
  for i in range (rows):
    grid.append([])
    for j in range(rows):
      node = Node(i, j, gap, rows)
      grid[i].append(node)
    
  return grid

# For drawing grid's line
def DrawGrid(win, rows, width):
  gap = width // rows
  for i in range(rows):
    pygame.draw.line(win, GRAY, (0, i * gap), (width, i * gap))
    for j in range(rows):
       pygame.draw.line(win, GRAY, (j * gap, 0), (j * gap, width))

# Draw the grids
def Draw(win, grid, rows, width):
  win.fill(WHITE)
    
  for row in grid:
    for node in row:
      node.Draw(win)

  DrawGrid(win, rows, width)
  pygame.display.update()

# Determine the position the mouse
def GetClickedPos(pos, rows, width):
  gap = width // rows
  y, x = pos

  row = y // gap
  col = x // gap

  return row, col