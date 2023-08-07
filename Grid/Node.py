import pygame
from Helper.GlobalVariables import *

# For the status of node and colour of grids
class Node:
  def __init__(self, row, col, width, totalRows, totalCols):
    self.row = row
    self.col = col
    self.x = row * width + SIDEBARWIDTH
    self.y = col * width
    self.colour = WHITE
    self.neighbours = []
    self.width = width
    self.totalRows = totalRows
    self.totalCols = totalCols

  # Determine where the node is
  def GetPos(self):
    return self.row, self.col
  
  # Checking node's colour to determine status
  def IsReset(self):
    return self.colour == WHITE
  
  def IsClosed(self):
    return self.colour == BLUE
    
  def IsOpen(self):
    return self.colour == GREEN
    
  def IsWall(self):
    return self.colour == BLACK
    
  def IsStart(self):
    return self.colour == RED
    
  def IsTarget(self):
    return self.colour == PURPLE
    
  # Changing node's colour
  def Reset(self):
    self.colour = WHITE

  def MakeClosed (self):
    self.colour = BLUE

  def MakeOpen(self):
    self.colour = GREEN

  def MakeWall(self):
    self.colour = BLACK

  def MakeStart(self):
    self.colour = RED

  def MakeTarget(self):
    self.colour = PURPLE

  def MakePath(self):
    self.colour = ORANGE

  def Draw(self, win):
    pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

  # Check for neighbours that are not wall nodes or outside of grid
  def UpdateNeighbours(self, grid):
    self.neighbours = []
    if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].IsWall(): # DOWN
      self.neighbours.append(grid[self.row + 1][self.col])

    if self.row > 0 and not grid[self.row - 1][self.col].IsWall(): # UP
      self.neighbours.append(grid[self.row - 1][self.col])

    if self.col > 0 and not grid[self.row][self.col - 1].IsWall(): # LEFT
      self.neighbours.append(grid[self.row][self.col - 1])

    if self.col < self.totalCols - 1 and not grid[self.row][self.col + 1].IsWall(): # RIGHT
      self.neighbours.append(grid[self.row][self.col + 1])
    
  def __lt__(self, other):
    return False
  
def UpdateAllNeighbours(grid, draw):
  for col in grid:
    for node in col:
      node.UpdateNeighbours(grid)

  return grid
