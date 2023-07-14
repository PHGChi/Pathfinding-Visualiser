import pygame
import math
import sys
sys.path.append('.')
from Helper.GlobalVariables import *
from Helper.ButtonHelper import Button
from Helper.TextHelper import DrawText, DrawTextCenter
from Grid.Node import Node
from Grid.Grid import MakeGrid, DrawGrid, Draw, GetClickedPos
from Algorithms.AStar import AStar

# Set the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualiser")
pygame.init()

def main(win, width):
    grid = MakeGrid(ROWS, width)
    allFonts = pygame.font.get_fonts()

    start = None
    target = None
    algID = 0

    run = True
    while run:
        Draw(win, grid, ROWS, width, algID)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #Change buttons colour based on whether they are selected or not
            if btnAStar.Check() == True and algID != 0:
                btnAStar.backgroundColour = SELECTEDBUTTON
            else:
                btnAStar.backgroundColour = UNSELECTEDBUTTON

            if btnReset.Check() == True:
                btnReset.backgroundColour = SELECTEDBUTTON
            else:
                btnReset.backgroundColour = UNSELECTEDBUTTON
                
            #When mouse is left clicked on the grid to change node's status
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, width)
                if row < ROWS and col < ROWS: #Why do I need this
                    node = grid[row][col]
                    #Choose start node
                    if not start and node != target:
                        start = node
                        start.IsStart = 1
                        start.MakeStart()
                        
                    #Choose target node
                    elif not target and node != start:
                        target = node
                        target.IsTarget = 1
                        target.MakeTarget()
                        
                    #Choose wall node
                    elif node != target and node != start:
                        node.MakeWall()
                        
                #Reset the grid when the rest button is checked
                elif btnReset.check() == True:
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, width)

                #When start button is pressed
                if btnStart.Check() == True and start and target:
                    for row in grid:
                        for node in row:
                            node.UpdateNeighbours(grid)

                    tempStart = start
                    tempTarget = target

                    #Run the AStar algorithm
                    if(algID == 0):
                        AStar(lambda: Draw(win, grid, ROWS, width, algID, 0), grid, start, target)

                    tempStart.MakeStart()
                    tempTarget.MakeTarget()

                #Change algorithm status when user choose an algorithm
                if btnAStar.Check() == True:
                    algID = 0
                else:
                    btnAStar.backgroundColour = UNSELECTEDBUTTON
                
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