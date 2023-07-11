import pygame
import math
import sys
sys.path.append(".")
import time
from Helper.GlobalVariables import *
from Grid.Node import Node
from Grid.Grid import MakeGrid, DrawGrid, Draw, GetClickedPos
from Algorithms.AStar import AStar

# Set the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualiser")
pygame.init()

def main(win, width):
    grid = MakeGrid(ROWS, width)
    allFonts = pygame.font.get_font() #What does this do

    start = None
    tartget = None
    algID = 0

    run = True
    while run:
        Draw(WIN, grid, ROWS, width, algID)

        for event in pygame.even.get():
            if event.type == pygame.QUIT:
                run = False
            
            #When mouse is left clicked on the grid to change node's status
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, WIDTH)
                node = grid[row][col]

                #Choose start node
                if not start and node != target:
                    start = node
                    start.MakeStart()

                #Choose target node
                elif not target and node != start:
                    target = node
                    target.MakeTarget()

                #Choose wall node
                elif node != target and node != start:
                    node.MakeWall()
                
            #When mouse is right clicked on the grid to reset the node
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, WIDTH)
                node = grid[row][col]
                node.Reset()
                if node == start:
                    start = None
                elif node == target:
                    target = None     
                
            #When the user is using a keyboard shortcut
            if event.type == pygame.KEYDOWN:
                #Press space bar to run the algorithm
                if event.key == pygame.K_SPACE and start and target:
                    for row in grid:
                        for node in row:
                            node.UpdateNeighbours(grid)
                                
                    AStar(lambda: Draw(WIN, grid, ROWS, WIDTH), grid, start, target)
                        
                # When user wants to clear the grid
                elif event.key == pygame.K_c:
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, WIDTH)
    pygame.quit()
main(WIN, WIDTH)