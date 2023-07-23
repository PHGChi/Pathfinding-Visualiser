import pygame
import math
from Grid.Node import Node
from Helper.GlobalVariables import *
from Helper.TextHelper import DrawText, DrawTextCenter

pygame.init()
font = pygame.font.SysFont('Arial', GAP)

#Make the grids to represent nodes
def MakeGrid(rows, cols):
  grid = []

  for i in range (rows):
    grid.append([])
    for j in range(cols):
      node = Node(i, j, GAP, rows, cols, [0,0], math.inf, [-1, -1], -1, -1)
      grid[i].append(node)
    
  return grid

#Initialise the grid's lines
def DrawGrid(win, rows):
  for i in range(rows):
    pygame.draw.line(win, GRAY, (SIDEBARWIDTH, i * GAP), (SIDEBARWIDTH + GAP * rows - 1, i * GAP))
    for j in range(rows):
       pygame.draw.line(win, GRAY, (SIDEBARWIDTH + j * GAP, 0), (SIDEBARWIDTH + j * GAP, GAP * rows - 1))

# Draw everything on the screen
def Draw(win, grid, rows, width, algID):
  win.fill(WHITE)
    
  for row in grid:
    for node in row:
      node.Draw(win)

  DrawGrid(win, rows)

  #Display the information regarding each algorithm

  #Display the sidebar
  lblTitle.Draw(win)
  dropAlgorithm.Draw(win)
  btnAStar.Draw(win)
  btnDjikstra.Draw(win)
  btnDFS.Draw(win)
  dropWalls.Draw(win)
  dropExtraNodes.Draw(win)
  btnVisualise.Draw(win)
  btnClearBoard.Draw(win)
  btnClearWall.Draw(win)
  btnClearPath.Draw(win)
  dropSpeed.Draw(win)
  btnHelp.Draw(win)

  #Display the legend
  legendStart.Draw(win)
  legendTarget.Draw(win)
  legendPrelimary.Draw(win)
  legendUnvisited.Draw(win)
  legendVisited1.Draw(win)
  legendVisited2.Draw(win)
  legendPath.Draw(win)
  legendWall.Draw(win)

  #Display the legend's text (try to center this)
  legendFont = pygame.font.SysFont('sans-serif', 14)
  DrawText("Start Node", legendFont, win, legendStart.x + legendStart.width + 5, legendStart.y, BLACK)
  DrawText("Target Node", legendFont, win, legendTarget.x + legendTarget.width + 5, legendTarget.y, BLACK)
  DrawText("Prelimary Node", legendFont, win, legendPrelimary.x + legendPrelimary.width + 5, legendPrelimary.y, BLACK)
  DrawText("Unvisited Node", legendFont, win, legendUnvisited.x + legendUnvisited.width + 5, legendUnvisited.y, BLACK)
  DrawText("Visited Node", legendFont, win, legendVisited2.x + legendVisited2.width + 5, legendVisited2.y, BLACK)
  DrawText("Path Node", legendFont, win, legendPath.x + legendPath.width + 5, legendPath.y, BLACK)
  DrawText("Wall Node", legendFont, win, legendWall.x + legendWall.width + 5, legendWall.y, BLACK)
  pygame.display.update()


# Determine the position the mouse
def GetClickedPos(pos):
  x, y = pos

  row = (x - SIDEBARWIDTH) // GAP
  col = y // GAP

  return row, col