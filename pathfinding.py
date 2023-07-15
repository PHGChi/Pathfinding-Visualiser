import pygame
import sys
sys.path.append('.')
from Helper.GlobalVariables import *
from Helper.ButtonHelper import Button
from Helper.TextHelper import DrawText, DrawTextCenter
from Grid.Node import Node
from Grid.Grid import MakeGrid, Draw, GetClickedPos
from Algorithms.AStar import AStar

# Set the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualiser")
pygame.init()

def main(win, width):
    grid = MakeGrid(ROWS)
    allFonts = pygame.font.get_fonts()

    start = None
    target = None
    algID = 0

    run = True
    while run:
        Draw(win, grid, ROWS, width, algID)

        for event in pygame.event.get():
            #If user wants to exit the program
            if event.type == pygame.QUIT:
                run = False

            #Change buttons colour based on whether they are selected or not
            #Add this feature in the button class
            if dropAlgorithm.Check() == True:
                dropAlgorithm.backgroundColour = SELECTEDBUTTON
            else:
                dropAlgorithm.backgroundColour = UNSELECTEDBUTTON

            if btnAStar.Check() == True:
                btnAStar.backgroundColour = SELECTEDBUTTON
            else:
                btnAStar.backgroundColour = UNSELECTEDBUTTON

            if btnDjikstra.Check() == True:
                btnDjikstra.backgroundColour = SELECTEDBUTTON
            else:
                btnDjikstra.backgroundColour = UNSELECTEDBUTTON

            if btnDFS.Check() == True:
                btnDFS.backgroundColour = SELECTEDBUTTON
            else:
                btnDFS.backgroundColour = UNSELECTEDBUTTON

            if dropWalls.Check() == True:
                dropWalls.backgroundColour = SELECTEDBUTTON
            else:
                dropWalls.backgroundColour = UNSELECTEDBUTTON

            if dropExtraNodes.Check() == True:
                dropExtraNodes.backgroundColour = SELECTEDBUTTON
            else:
                dropExtraNodes.backgroundColour = UNSELECTEDBUTTON

            if btnVisualise.Check() == True:
                btnVisualise.backgroundColour = SELECTEDBUTTON
            else:
                btnVisualise.backgroundColour = UNSELECTEDBUTTON

            if btnClearBoard.Check() == True:
                btnClearBoard.backgroundColour = SELECTEDBUTTON
            else:
                btnClearBoard.backgroundColour = UNSELECTEDBUTTON

            if btnClearWall.Check() == True:
                btnClearWall.backgroundColour = SELECTEDBUTTON
            else:
                btnClearWall.backgroundColour = UNSELECTEDBUTTON

            if btnClearPath.Check() == True:
                btnClearPath.backgroundColour = SELECTEDBUTTON
            else:
                btnClearPath.backgroundColour = UNSELECTEDBUTTON

            if dropSpeed.Check() == True:
                dropSpeed.backgroundColour = SELECTEDBUTTON
            else:
                dropSpeed.backgroundColour = UNSELECTEDBUTTON

            if btnHelp.Check() == True:
                btnHelp.backgroundColour = SELECTEDBUTTON
            else:
                btnHelp.backgroundColour = UNSELECTEDBUTTON
                
            #When mouse is left clicked on the grid to change node's status
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, width)
                if row < ROWS and col < ROWS:
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
                elif btnClearBoard.Check() == True:
                    start = None
                    target = None
                    grid = MakeGrid(ROWS)

                #When start button is pressed
                if btnVisualise.Check() == True and start and target:
                    for row in grid:
                        for node in row:
                            node.UpdateNeighbours(grid)

                    tempStart = start
                    tempTarget = target

                    #Run the AStar algorithm
                    if(algID == 0):
                        AStar(lambda: Draw(win, grid, ROWS, width, algID), grid, start, target)

                    #Run Dijkstra's algorithm

                    #Run DFS algorithm

                    tempStart.MakeStart()
                    tempTarget.MakeTarget()

                #Change algorithm status when user choose an algorithm
                #Add this feature to the button class
                if dropAlgorithm.Check() == True:
                    dropAlgorithm.backgroundColour = GRAY
                    algID = 0
                else:
                    dropAlgorithm.backgroundColour = UNSELECTEDBUTTON

                if btnAStar.Check() == True:
                    btnAStar.backgroundColour = GRAY
                    algID = 0
                else:
                    btnAStar.backgroundColour = UNSELECTEDBUTTON

                if btnDjikstra.Check() == True:
                    btnDjikstra.backgroundColour = GRAY
                    algID = 0 #Change this
                else:
                    btnDjikstra.backgroundColour = UNSELECTEDBUTTON

                if btnDFS.Check() == True:
                    btnDFS.backgroundColour = GRAY
                    algID = 0 #Change this
                else:
                    btnDFS.backgroundColour = UNSELECTEDBUTTON

                if dropWalls.Check() == True:
                    dropWalls.backgroundColour = GRAY
                else:
                    dropWalls.backgroundColour = UNSELECTEDBUTTON

                if dropExtraNodes.Check() == True:
                    dropExtraNodes.backgroundColour = GRAY
                else:
                    dropExtraNodes.backgroundColour = UNSELECTEDBUTTON

                if btnVisualise.Check() == True:
                    btnVisualise.backgroundColour = GRAY
                else:
                    btnVisualise.backgroundColour = UNSELECTEDBUTTON

                if btnClearBoard.Check() == True:
                    btnClearBoard.backgroundColour = GRAY
                else:
                    btnClearBoard.backgroundColour = UNSELECTEDBUTTON

                if btnClearWall.Check() == True:
                    btnClearWall.backgroundColour = GRAY
                else:
                    btnClearWall.backgroundColour = UNSELECTEDBUTTON

                if btnClearPath.Check() == True:
                    btnClearPath.backgroundColour = GRAY
                else:
                    btnClearPath.backgroundColour = UNSELECTEDBUTTON

                if dropSpeed.Check() == True:
                    dropSpeed.backgroundColour = GRAY
                else:
                    dropSpeed.backgroundColour = UNSELECTEDBUTTON

                if btnHelp.Check() == True:
                    btnHelp.backgroundColour = GRAY
                else:
                    btnHelp.backgroundColour = UNSELECTEDBUTTON
                
            #When mouse is right clicked on the grid to reset the node
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, width)
                if row < ROWS and col < ROWS:
                    node = grid[row][col]
                    node.Reset()
                    #Reset start node
                    if node == start:
                        node.IsStart = - 1
                        start = None
                    #Reset target node
                    elif node == target:
                        node.IsTarget = - 1
                        target = None     
                
            #When the user is using a keyboard shortcut
            if event.type == pygame.KEYDOWN:
                #When the user wants to escape the program
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
main(WIN, WIDTH)