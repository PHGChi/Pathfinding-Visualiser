import random
from Helper.GlobalVariables import *

def Prims(draw, grid):
    # Fill the grid with wall nodes
    for row in grid:
        for node in row:
            node.MakeWall()
    # Set a random start node
    startRow = random.randint(0, ROWS - 1)
    startCol = random.randint(0, COLS - 1)

    frontier = [(startRow, startCol)] # Holds all nodes to be considered
    grid[startRow][startCol].Reset()

    while frontier:
        current = frontier.pop(random.randint(0, len(frontier) - 1))

        # Get the neighbours of the current cell
        # The neighbours are all two nodes away from each other
        neighbours = []
        row, col = current
        if row >= 2: neighbours.append((row - 2, col))
        if row < ROWS - 2: neighbours.append((row + 2, col))
        if col >= 2: neighbours.append((row, col - 2))
        if col < COLS - 2: neighbours.append((row, col + 2))

        random.shuffle(neighbours)

        for rowNeighbour, colNeighbour in neighbours:
            if grid[rowNeighbour][colNeighbour].IsWall():
                # Create a path between the current and neighbour node
                grid[rowNeighbour][colNeighbour].Reset()
                grid[row + (rowNeighbour - row) // 2][col + (colNeighbour - col) // 2].Reset()
                frontier.append((rowNeighbour, colNeighbour))
        draw()
    
