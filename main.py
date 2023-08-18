import pygame
import sys
sys.path.append('.')
from Helper.GlobalVariables import *
from Grid.Grid import MakeGrid, Draw, GetClickedPos
from Grid.Path import ResetPath
from HelpWindow import HelpSlides
from Maze.RecursiveDivision import RecursiveDivision
from Maze.Prims import Prims
from Maze.Random import Random
from Maze.BinaryTree import BinaryTree
from Algorithms.AStar import AStar
from Algorithms.Dijkstras import Dijkstra
from Algorithms.DFS import DFS
from Algorithms.Bidirectional import Bidirectional

# Set the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualiser")
pygame.init()

def main(win):
    grid = MakeGrid(ROWS, COLS)

    start = None
    target = None
    algID = 0
    noPathFound = False

    run = True
    while run:
        Draw(win, grid, ROWS)

        for event in pygame.event.get():
            # If user wants to exit the program
            if event.type == pygame.QUIT:
                run = False

            # Change colour when hovered
            btnVisualise.Check()
            btnClearBoard.Check()
            btnClearPath.Check()
            btnClearWall.Check()
            btnAStar.Check()
            btnDjikstra.Check()
            btnDFS.Check()
            btnBidirectional.Check()
            btnRecursiveDivsion.Check()
            btnPrims.Check()
            btnBinaryTree.Check()
            btnRandom.Check()
            btnHelp.Check()
        
            # When mouse is left clicked
            if pygame.mouse.get_pressed()[0]:
                noPathFound = False
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

                # Visualise the algorithm when the 'Visualise' button is pressed
                if btnVisualise.Check() == True:
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
                            if not AStar(lambda: Draw(win, grid, ROWS), grid, start, target):
                                noPathFound = True

                        # Run Dijkstra's algorithm
                        if(algID == 1):
                            ResetPath(grid)
                            if not Dijkstra(lambda: Draw(win, grid, ROWS), grid, start, target):
                                noPathFound = True

                        # Run DFS algorithm
                        if(algID == 2):
                            ResetPath(grid)
                            if not DFS(lambda: Draw(win, grid, ROWS), grid, start, target):
                                noPathFound = True

                        # Run Bidrectional BFS algorithm
                        if(algID == 3):
                            ResetPath(grid)
                            if not Bidirectional(lambda: Draw(win, grid, ROWS), grid, start, target):
                                noPathFound = True

                        tempStart.MakeStart()
                        tempTarget.MakeTarget()
                else:
                    btnVisualise.UpdateText("Visualise") # Reset button back to "Visualise"

                # Clear the board when the 'Clear Board' button is pressed
                if btnClearBoard.Check() == True:
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)

                # Clear the wall nodes when the 'Clear Wall' button is pressed
                if btnClearWall.Check() == True:
                    for row in grid:
                        for node in row:
                            if node.IsWall():
                                node.Reset()

                # Clear the path and visited nodes when the 'Clear Path' button is pressed
                if btnClearPath.Check() == True:
                    ResetPath(grid)

                if btnAStar.Check() == True:
                    algID = 0 # Change algorithm to A*
                    lblAlgorithm.UpdateText("Algorithm: A*")

                if btnDjikstra.Check() == True:
                    algID = 1 # Change algorithm to Djikstra's
                    lblAlgorithm.UpdateText("Algorithm: Dijkstra's")

                if btnDFS.Check() == True:
                    algID = 2 # Change algorithm to Depth First Search
                    lblAlgorithm.UpdateText("Algorithm: DFS")

                if btnBidirectional.Check() == True:
                    algID = 3 # Change algorithm to Bidirectional Breadth First Search
                    lblAlgorithm.UpdateText("Algorithm: Bidirectional BFS")

                # Generate maze based on algorithm
                if btnRecursiveDivsion.Check() == True:
                    # Reset board
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)

                    RecursiveDivision(lambda: Draw(win, grid, ROWS), grid, numCells)

                if btnPrims.Check() == True:
                    # Reset board
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)

                    Prims(lambda: Draw(win, grid, ROWS), grid)

                if btnBinaryTree.Check() == True:
                    # Reset board
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)

                    BinaryTree(lambda: Draw(win, grid, ROWS), grid)

                if btnRandom.Check() == True:
                    # Reset board
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, COLS)

                    Random(lambda: Draw(win, grid, ROWS), grid)

                if btnHelp.Check() == True:
                    # Show help slides
                    HelpSlides()
                    # Reset the display
                    pygame.display.set_mode((WIDTH, HEIGHT))
                    pygame.display.set_caption("Pathfinding Visualiser")
                    pygame.init()
                
            # When mouse is right clicked
            elif pygame.mouse.get_pressed()[2]:
                noPathFound = False
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
                # When the user wants to escape the program
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        # For when there is no path between start and target  node
        if noPathFound:
            lblNoPath.Draw(win)
            pygame.display.update()

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main(WIN)