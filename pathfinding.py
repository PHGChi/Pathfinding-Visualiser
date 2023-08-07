import pygame
import sys
sys.path.append('.')
from Helper.GlobalVariables import *
from Grid.Grid import MakeGrid, Draw, GetClickedPos
from Grid.Path import ResetPath
from Grid.HelpWindow import HelpSlides
from Maze.RecursiveDivision import RecursiveDivision
from Maze.Prims import Prims
from Maze.Random import Random
from Maze.BinaryTree import BinaryTree
from Algorithms.AStar import AStar
from Algorithms.Dijkstras import Dijkstra
from Algorithms.DFS import DFS
from Algorithms.BFS import BFS
from Algorithms.Bidirectional import Bidirectional

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

            # Change buttons colour when hovered over    
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

            if btnBidirectional.Check() == True:
                btnBidirectional.backgroundColour = DARKGREEN
            else:
                btnBidirectional.backgroundColour = BLACK

            if btnRecursiveDivsion.Check() == True:
                btnRecursiveDivsion.backgroundColour = DARKGREEN
            else:
                btnRecursiveDivsion.backgroundColour = BLACK
            
            if btnPrims.Check() == True:
                btnPrims.backgroundColour = DARKGREEN
            else:
                btnPrims.backgroundColour = BLACK

            if btnBinaryTree.Check() == True:
                btnBinaryTree.backgroundColour = DARKGREEN
            else:
                btnBinaryTree.backgroundColour = BLACK

            if btnRandom.Check() == True:
                btnRandom.backgroundColour = DARKGREEN
            else:
                btnRandom.backgroundColour = BLACK

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
            
            if btnHelp.Check() == True:
                btnHelp.textColour = GRAY
                btnHelp.borderColour = GRAY
            else:
                btnHelp.textColour = BLACK
                btnHelp.borderColour = BLACK
        
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
                if btnAStar.Check() == True:
                    btnAStar.backgroundColour = GRAY
                    algID = 0 # Change algorithm to A*
                    lblAlgorithm.UpdateText("Algorithm: A*")
                else:
                    btnAStar.backgroundColour = BLACK

                if btnDjikstra.Check() == True:
                    btnDjikstra.backgroundColour = GRAY
                    algID = 1 # Change algorithm to Djikstra's
                    lblAlgorithm.UpdateText("Algorithm: Dijkstra's")
                else:
                    btnDjikstra.backgroundColour = BLACK

                if btnDFS.Check() == True:
                    btnDFS.backgroundColour = GRAY
                    algID = 2 # Change algorithm to Depth First Search
                    lblAlgorithm.UpdateText("Algorithm: DFS")
                else:
                    btnDFS.backgroundColour = BLACK

                if btnBidirectional.Check() == True:
                    btnBidirectional.backgroundColour = GRAY
                    algID = 3 # Change algorithm to Bidirectional Breadth First Search
                    lblAlgorithm.UpdateText("Algorithm: Bidirectional BFS")
                else:
                    btnBidirectional.backgroundColour = BLACK

                if btnRecursiveDivsion.Check() == True:
                    btnRecursiveDivsion.backgroundColour = GRAY
                    # Reset board
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)

                    RecursiveDivision(lambda: Draw(win, grid, ROWS, width, algID), grid, numCells)
                else:
                    btnRecursiveDivsion.backgroundColour = BLACK

                if btnPrims.Check() == True:
                    btnPrims.backgroundColour = GRAY
                    # Reset board
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)

                    Prims(lambda: Draw(win, grid, ROWS, width, algID), grid)
                else:
                    btnPrims.backgroundColour = BLACK

                if btnBinaryTree.Check() == True:
                    btnBinaryTree.backgroundColour = GRAY
                    # Reset board
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)

                    BinaryTree(grid)
                else:
                    btnBinaryTree.backgroundColour = BLACK

                if btnRandom.Check() == True:
                    btnRandom.backgroundColour = GRAY
                    # Reset board
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)

                    Random(lambda: Draw(win, grid, ROWS, width, algID), grid)
                else:
                    btnRandom.backgroundColour = BLACK

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
                            ResetPath(grid)
                            AStar(lambda: Draw(win, grid, ROWS, width, algID), grid, start, target)

                        # Run Dijkstra's algorithm
                        if(algID == 1):
                            ResetPath(grid)
                            Dijkstra(lambda: Draw(win, grid, ROWS, width, algID), grid, start, target)

                        # Run DFS algorithm
                        if(algID == 2):
                            ResetPath(grid)
                            DFS(lambda: Draw(win, grid, ROWS, width, algID), grid, start, target)

                        # Run Bidrectional BFS algorithm
                        if(algID == 3):
                            ResetPath(grid)
                            Bidirectional(lambda: Draw(win, grid, ROWS, width, algID), grid, start, target)

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
                    ResetPath(grid)
                else:
                    btnClearPath.backgroundColour = BLACK

                if btnHelp.Check() == True:
                    btnHelp.textColour = LIGHTGRAY
                    btnHelp.borderColour = LIGHTGRAY

                    # Show help slides
                    HelpSlides()
                    # Reset the display
                    pygame.display.set_mode((WIDTH, HEIGHT))
                    pygame.display.set_caption("Pathfinding Visualiser")
                    pygame.init()

                    # Reset button's colour after showing the slides
                    # btnHelp.textColour = BLACK
                    # btnHelp.borderColour = BLACK
                else:
                    btnHelp.textColour = BLACK
                    btnHelp.borderColour = BLACK
                
            # When mouse is right clicked
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
                
            # When the user is using a keyboard shortcut
            if event.type == pygame.KEYDOWN:
                #When the user wants to escape the program
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    pygame.quit()
main(WIN, WIDTH)