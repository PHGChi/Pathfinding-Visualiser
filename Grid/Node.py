import pygame
from Helper.GlobalVariables import *

# For the status of node and colour of grids
class Node:
  def __init__(self, row, col, width, totalRows, isVisited, distance, predecessor, isStart, isTarget):
    self.row = row
    self.col = col
    self.x = row * width
    self.y = col * width
    self.color = WHITE
    self.neighbours = []
    self.width = width
    self.totalRows = totalRows
    self.isVisited = [0,0]
    self.distance = distance
    self.predecessor = [-1, -1]
    self.isStart = isStart
    self.isTarget = isTarget

  # Determine where the node is
  def GetPos(self):
    return self.row, self.col
    
  # Check the colour of nodes to check its status
  def IsClosed(self):
    return self.color == BLUE
    
  def IsOpen(self):
    return self.color == GREEN
    
  def IsWall(self):
    return self.color == BLACK
    
  def IsStart(self):
    return self.color == RED
    
  def IsTarget(self):
    return self.color == PURPLE
    
  # Changing node's colour
  def Reset(self):
    self.color = WHITE

  def MakeClosed (self):
    self.color = BLUE

  def MakeOpen(self):
    self.color = GREEN

  def MakeWall(self):
    self.color = BLACK

  def MakeStart(self):
    self.color = RED

  def MakeTarget(self):
    self.color = PURPLE

  def MakePath(self):
    self.color = ORANGE

  def GetVisited(self):
    return self.isVisited[0], self.isVisited[1]
  
  def GetDistance(self):
    return self.distance
  
  def GetPredecessor(self):
    return self.predecessor[0], self.predecessor[1]
  
  def GetStart(self):
    return self.isStart
  
  def GetTarget(self):
    return self.isTarget
    
  def Draw(self, win):
    pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

  # Check for neighbours that are not wall nodes or outside of grid
  def UpdateNeighbours(self, grid):
    self.neighbours = []
    if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].IsWall(): # DOWN
      self.neighbours.append(grid[self.row + 1][self.col])

    if self.row > 0 and not grid[self.row - 1][self.col].IsWall(): # UP
      self.neighbours.append(grid[self.row - 1][self.col])

    if self.col > 0 and not grid[self.row][self.col - 1].IsWall(): # LEFT
      self.neighbours.append(grid[self.row][self.col - 1])

    if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].IsWall(): # RIGHT
      self.neighbours.append(grid[self.row][self.col + 1])
    
  def __lt__(self, other):
    return False
