import pygame
import sys
sys.path.append('.')
from Helper.GlobalVariables import *
from Helper.ButtonHelper import Button
from Helper.TextHelper import DrawText, DrawTextCenter
from Grid.Node import Node
from Grid.Grid import MakeGrid, Draw, GetClickedPos
from Algorithms.AStar import AStar
from Algorithms.Dijkstras import Dijkstra

# Set the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualiser")
pygame.init()

def main(win, width):
    grid = MakeGrid(ROWS, COLS)

    start = None
    target = None
    algID = 0

    run = True
    while run:
        Draw(win, grid, ROWS, width, algID)

        for event in pygame.event.get():
            # If user wants to exit the program
            if event.type == pygame.QUIT:
                run = False

            # Change buttons colour based on whether they are selected or not
            # Add this feature in the button class
            if dropAlgorithm.Check() == True:
                dropAlgorithm.backgroundColour = DARKGREEN
            else:
                dropAlgorithm.backgroundColour = BLACK
            if btnAStar.Check() == True:
                btnAStar.backgroundColour = DARKGREEN
            else:
                btnAStar.backgroundColour = BLACK

            if btnDjikstra.Check() == True:
                btnDjikstra.backgroundColour = DARKGREEN
            else:
                btnDjikstra.backgroundColour = BLACK

            if btnDFS.Check() == True:
                btnDFS.backgroundColour = DARKGREEN
            else:
                btnDFS.backgroundColour = BLACK
            if dropWalls.Check() == True:
                dropWalls.backgroundColour = DARKGREEN
            else:
                dropWalls.backgroundColour = BLACK

            if dropExtraNodes.Check() == True:
                dropExtraNodes.backgroundColour = DARKGREEN
            else:
                dropExtraNodes.backgroundColour = BLACK

            if btnClearBoard.Check() == True:
                btnClearBoard.backgroundColour = DARKGREEN
            else:
                btnClearBoard.backgroundColour = BLACK

            if btnClearWall.Check() == True:
                btnClearWall.backgroundColour = DARKGREEN
            else:
                btnClearWall.backgroundColour = BLACK

            if btnClearPath.Check() == True:
                btnClearPath.backgroundColour = DARKGREEN
            else:
                btnClearPath.backgroundColour = BLACK

            if dropSpeed.Check() == True:
                dropSpeed.backgroundColour = DARKGREEN
            else:
                dropSpeed.backgroundColour = BLACK

            if btnHelp.Check() == True:
                btnHelp.backgroundColour = DARKGREEN
            else:
                btnHelp.backgroundColour = BLACK
                
            # When mouse is left clicked
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos)
                if row >= 0 and row < ROWS and col >= 0 and col < COLS:
                    node = grid[row][col]
                    # Choose start node
                    if not start and node != target:
                        start = node
                        start.IsStart = 1
                        start.MakeStart()
                        
                    # Choose target node
                    elif not target and node != start:
                        target = node
                        target.IsTarget = 1
                        target.MakeTarget()
                        
                    # Choose wall node
                    elif node != target and node != start:
                        node.MakeWall()
                        
                # Change the button's colour when the user click on it and run what the button is supposed to do
                # Add this feature to the button class
                if dropAlgorithm.Check() == True:
                    dropAlgorithm.backgroundColour = GRAY
                else:
                    dropAlgorithm.backgroundColour = BLACK

                if btnAStar.Check() == True:
                    btnAStar.backgroundColour = GRAY
                    algID = 0 # Change algorithm to A*
                    dropAlgorithm.UpdateText("Algorithm: A*")
                else:
                    btnAStar.backgroundColour = BLACK

                if btnDjikstra.Check() == True:
                    btnDjikstra.backgroundColour = GRAY
                    algID = 1 # Change algorithm to Djikstra's
                    dropAlgorithm.UpdateText("Algorithm: Dijkstra's")
                else:
                    btnDjikstra.backgroundColour = BLACK

                if btnDFS.Check() == True:
                    btnDFS.backgroundColour = GRAY
                    algID = 0 # Change algorithm to Depth First Search
                else:
                    btnDFS.backgroundColour = BLACK

                if dropWalls.Check() == True:
                    dropWalls.backgroundColour = GRAY
                else:
                    dropWalls.backgroundColour = BLACK

                if dropExtraNodes.Check() == True:
                    dropExtraNodes.backgroundColour = GRAY
                else:
                    dropExtraNodes.backgroundColour = BLACK

                # Visualise the algorithm when the 'Visualise' button is pressed
                if btnVisualise.Check() == True:
                    btnVisualise.backgroundColour = GRAY 
                    # Check for start and target node
                    if not start:
                        btnVisualise.backgroundColour = RED
                        btnVisualise.UpdateText("Needs start node")
                    elif not target:
                        btnVisualise.backgroundColour = RED
                        btnVisualise.UpdateText("Needs target node")
                    else:
                        for row in grid:
                            for node in row:
                                node.UpdateNeighbours(grid)

                        tempStart = start
                        tempTarget = target

                        # Run the AStar algorithm
                        if(algID == 0):
                            AStar(lambda: Draw(win, grid, ROWS, width, algID), grid, start, target)

                        # Run Dijkstra's algorithm
                        if(algID == 1):
                            Dijkstra(lambda: Draw(win, grid, ROWS, width, algID), grid, start, target)

                        # Run DFS algorithm

                        tempStart.MakeStart()
                        tempTarget.MakeTarget()
                else:
                    btnVisualise.backgroundColour = GREEN
                    btnVisualise.UpdateText("Visualise") # Reset button back to "Visualise"

                # Clear the board when the 'Clear Board' button is pressed
                if btnClearBoard.Check() == True:
                    btnClearBoard.backgroundColour = GRAY 
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)
                else:
                    btnClearBoard.backgroundColour = BLACK

                # Clear the wall nodes when the 'Clear Wall' button is pressed
                if btnClearWall.Check() == True:
                    btnClearWall.backgroundColour = GRAY
                    for row in grid:
                        for node in row:
                            if node.IsWall():
                                node.Reset()
                else:
                    btnClearWall.backgroundColour = BLACK

                # Clear the path and visited nodes when the 'Clear Path' button is pressed
                if btnClearPath.Check() == True:
                    btnClearPath.backgroundColour = GRAY
                    for row in grid:
                        for node in row:
                            if node.IsClosed() or node.IsOpen() or node.colour == ORANGE:
                                node.Reset()
                else:
                    btnClearPath.backgroundColour = BLACK

                if dropSpeed.Check() == True:
                    dropSpeed.backgroundColour = GRAY
                else:
                    dropSpeed.backgroundColour = BLACK

                if btnHelp.Check() == True:
                    btnHelp.backgroundColour = GRAY
                else:
                    btnHelp.backgroundColour = BLACK
                
            #When mouse is right clicked
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos)

                if row >= 0 and row < ROWS and col >= 0 and col < COLS:
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