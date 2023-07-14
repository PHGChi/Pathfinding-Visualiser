import pygame
import math
import sys
from Grid.Node import Node
from Helper.GlobalVariables import *
from Helper.TextHelper import DrawText, DrawTextCenter

pygame.init()
font = pygame.font.SysFont('Arial', GAP)

#Create grids to represent nodes
def MakeGrid(rows, width):
  grid = []
  #gap = width // rows
  gap = 15
  for i in range (rows):
    grid.append([])
    for j in range(rows):
      node = Node(i, j, gap, rows, [0,0], math.inf, [-1,-1], -1, -1)
      grid[i].append(node)
    
  return grid

#Initialise the grid's lines
def DrawGrid(win, rows, width):
  #gap = width // rows
  gap = 15
  for i in range(50):
    pygame.draw.line(win, GRAY, (0, i * gap), (GAP*50 - 1, i * gap))
    for j in range(50):
       pygame.draw.line(win, GRAY, (j * gap, 0), (j * gap, GAP*50 - 1))

  #Draw the sidebar
  for i in range(gap):
    pygame.draw.line(win, RED, (ROWS*GAP, i), (WIDTH, i))
    pygame.draw.line(win, RED, (ROWS*GAP, HEIGHT - GAP + i), (WIDTH, HEIGHT - GAP + i))
    pygame.draw.line(win, RED, (ROWS*GAP, (int)(HEIGHT/2) + 100 + i), (WIDTH, (int)(HEIGHT/2) + 100 + i))
    pygame.draw.line(win, RED, (ROWS*GAP, 7*GAP + 100 + i), (WIDTH, 7*GAP + 100 + i))
    pygame.draw.line(win, RED, (ROWS*GAP, 14*GAP + 100 + i), (WIDTH, 14*GAP + 100 + i))
    pygame.draw.line(win, RED, (WIDTH - GAP + i, 0), (WIDTH - GAP + i, GAP*50 - 1))
    pygame.draw.line(win, RED, (ROWS*GAP + i, 0), (ROWS*GAP + i,GAP*50 -1))

#Draw the grids
def Draw(win, grid, rows, width, algID):
  win.fill(WHITE)
    
  for row in grid:
    for node in row:
      node.Draw(win)

      #Draw the start node
      if node.isStart == 1:
        node.MakeStart()
        text = font.render(" ", True, BLACK)
        textRect = text.get_rect(center = (node.row * GAP + (int)(GAP/2), node.col * GAP + (int)(GAP/2)))
        win.blit(text, textRect)

      #Draw the target node

      #Draw the wall node

      #Draw wall nodes around the grid acting as a barrier

  DrawGrid(win, rows, width)
  font1 = pygame.font.SysFont('script', 22)

  #Display the information regarding each algorithm

  #Create the legend
  font1 = pygame.font.SysFont('calibri', 40)
  DrawTextCenter("Legend", font1, win, 960, 245, BLACK)
  font1 = pygame.font.SysFont('calibri', 22)
  DrawText("Start node", font1, win, 800, 275, BLACK)
  DrawText("Target node", font1, win, 925, 275, BLACK)
  DrawText("Wall node", font1, win, 1050, 275, BLACK)
  DrawText("Pick an algorithm to compute shortest path:", font1, win, 785, 520, BLACK)

  #Display everything
  btnAStar.Draw(win)
  btnDFS.Draw(win)
  legendStart.Draw(win)
  legendTarget.Draw(win)
  legendWall.Draw(win)
  pygame.display.update()


# Determine the position the mouse
def GetClickedPos(pos, rows, width):
  #gap = width // rows
  gap = 15
  y, x = pos

  row = y // gap
  col = x // gap

  return row, col