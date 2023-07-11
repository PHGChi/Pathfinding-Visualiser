import pygame
import math
import sys
sys.path.append(".")
import time
from Helper.GlobalVariables import *
from Helper.ButtonHelper import Button
from Helper.TextHelper import drawText, drawTextcenter
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

            #Insert in all the buttons
            
            
            #When mouse is left clicked on the grid to change node's status
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, WIDTH)
                if row < ROWS and col < ROWS: #Why do I need this
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
                        
                #When reset button is pressed

                #When start button is pressed

                #Change button colour
                
            #When mouse is right clicked on the grid to reset the node
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, width)
                if row < ROWS and col < ROWS:
                    node = grid[row][col]
                    node.Reset()
                    #Reset start node
                    if node == start:
                        node.IsStart = -1 #What does this do
                        start = None
                    #Reset target node
                    elif node == target:
                        node.IsTarget = -1
                        target = None     
                
            #When the user is using a keyboard shortcut
            if event.type == pygame.KEYDOWN:
                #When the user wants to escape the program
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
main(WIN, WIDTH)