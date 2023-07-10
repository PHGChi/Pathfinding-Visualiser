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

# When mouse is clicked on the grid
def OnMouseClick(event):
    global start, target, grid, canvas
    row, col = GetClickedPos(event, WIDTH)
    node = grid[row][col]
    if not start and node != target:
        start = node
        start.MakeStart()
    elif not target and node != start:
        target = node
        target.MakeTarget()
    elif node != target and node != start:
        node.MakeWall()
    Draw(canvas, grid, WIDTH)

# When user wants to remove a node
def OnMouseRightClick(event):
    global start, target, grid, canvas
    row, col = GetClickedPos(event, WIDTH)
    node = grid[row][col]
    node.Reset()
    if node == start:
        start = None
    elif node == target:
        target = None
    Draw(canvas, grid, WIDTH)

def OnKeyPress(event):
    # When user wants to visualise the algorithm
    global start, target, grid, canvas
    if event.keysym == "space" and start and target:
        for row in grid:
            for node in row:
                node.UpdateNeighbours(grid)
        AStar(lambda: Draw(canvas, grid, WIDTH), grid, start, target)
        Draw(canvas, grid, WIDTH)

    # When user wants to clear the grid
    elif event.char == "c":
        start = None
        target = None
        grid = MakeGrid(ROWS, WIDTH)
        Draw(canvas, grid, WIDTH)

def main():
    global canvas, start, target, grid
    start = None
    target = None
    grid = MakeGrid(ROWS, WIDTH)

    root = tk.Tk()
    root.title("Pathfinding Algorithm Visualiser")

    canvas = tk.Canvas(root, width=WIDTH, height=WIDTH)
    canvas.pack()

    canvas.bind("<Button-1>", OnMouseClick)
    canvas.bind("<Button-3>", OnMouseRightClick)
    root.bind("<Key>", OnKeyPress)

    Draw(canvas, grid, WIDTH)

    root.mainloop()

if __name__ == "__main__":
    main()