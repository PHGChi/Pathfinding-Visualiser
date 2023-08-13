import random
from Helper.GlobalVariables import *

def BinaryTree(draw, grid):
    for row in range(ROWS):
        for col in range(COLS):
            node = grid[row][col]

            # Initialise odd row or column as wall
            if row % 2 != 0 and col % 2 != 0:
                node.Reset()
            else:
                node.MakeWall()

    # Randomly carve passages
    for row in range(1, ROWS, 2):
        for col in range(1, COLS, 2):
            node = grid[row][col]  

            # Randomly choose to carve either up or left
            if random.choice([True, False]):
                if row >= 1:
                    grid[row - 1][col].Reset() # Carve up
                else:
                    grid[row][col - 1].Reset() # Carve left
            else:
                if col >= 1:
                    grid[row][col - 1].Reset() # Carve left
                else:
                    grid[row - 1][col].Reset() # Carve up
            
        draw()