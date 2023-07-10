import tkinter as tk
from queue import PriorityQueue

# Set the display
WIDTH = 800
ROWS = 50

# Colour coordinate node's colour
RED = "#F65353"
PURPLE = "#726FC8"
GREEN = "#69B27A"
BLUE = "#58B1FF"
ORANGE = "#FFB347"
WHITE = "#FFFFFF"
BLACK = "#4C5270"
GRAY = "#9B9B9B"

# For the status of node and colour of grids
class Node:
    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.totalRows = totalRows

    # Determine where the node is
    def GetPos(self):
        return self.row, self.col
    
    # Check the colour of nodes to check its status
    def IsClosed(self):
        return self.color == BLUE
    
    def IsOpen(self):
        return self.color == GREEN
    
    def IsWall(self):
        return self.color == BLACK
    
    def IsStart(self):
        return self.color == RED
    
    def IsTarget(self):
        return self.color == PURPLE
    
    # Changing node's colour
    def Reset(self):
        self.color = WHITE

    def MakeClosed (self):
        self.color = BLUE

    def MakeOpen(self):
        self.color = GREEN

    def MakeWall(self):
        self.color = BLACK

    def MakeStart(self):
        self.color = RED

    def MakeTarget(self):
        self.color = PURPLE

    def MakePath(self):
        self.color = ORANGE

    def Draw(self, canvas):
        canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.width, fill=self.color
        )

    # Check for neighbours that are not wall nodes or outside of grid
    def UpdateNeighbours(self, grid):
        self.neighbours = []
        if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].IsWall(): # DOWN
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].IsWall(): # UP
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].IsWall(): # LEFT
            self.neighbours.append(grid[self.row][self.col - 1])

        if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].IsWall(): # RIGHT
            self.neighbours.append(grid[self.row][self.col + 1])

# Find the manhattan distance (heuristic)
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Draw the shortest path until we reach back to the start node
def ReconstructPath(predecessor, current, draw):
    while current in predecessor:
        current = predecessor[current]
        if not current.IsStart(): # Don't colour the start node
            current.MakePath()
        draw()

# Implement A* Path Finding Algorithm
def AStar(draw, grid, start, target):
    count = 0
    setOpen = PriorityQueue()
    setOpen.put((0, count, start))
    predecessor = {}
    gScore = {node: float("inf") for row in grid for node in row} # Keep track of current distance from start node to current node
    gScore[start] = 0
    fScore = {node: float("inf") for row in grid for node in row} # Keep track of predicted distance from current node to end node
    fScore[start] = h(start.GetPos(), target.GetPos())

    setOpenHash = {start} # Check if anything is in the priority queue

    # Break if check all nodes and path doesn't exist
    while not setOpen.empty(): 
        current = setOpen.get()[2]
        setOpenHash.remove(current)

        # Found the shortest path, visualise it
        if current == target: 
            ReconstructPath(predecessor, target, draw)
            target.MakeTarget()
            return True
        
        # Consider neighbour nodes to find target node
        for neighbour in current.neighbours:
            tempGScore = gScore[current] + 1

            # When a better path is found
            if tempGScore < gScore[neighbour]:
                predecessor[neighbour] = current
                gScore[neighbour] = tempGScore
                fScore[neighbour] = tempGScore + h(neighbour.GetPos(), target.GetPos())
                if neighbour not in setOpenHash:
                    count += 1
                    setOpen.put((fScore[neighbour], count, neighbour))
                    setOpenHash.add(neighbour)
                    neighbour.MakeOpen()

        draw()
        if current != start:
            current.MakeClosed()
    return False

# Create grids to represent nodes
def MakeGrid(rows, width):
    grid = []
    gap = width // rows
    for i in range (rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    
    return grid

# For drawing grid's line
def DrawGrid(canvas, width):
    gap = width // ROWS
    for i in range(ROWS):
        canvas.create_line(0, i* gap, width, i * gap, fill=GRAY)
        canvas.create_line(i * gap, 0, i * gap, width, fill=GRAY)

# Draw the grids
def Draw(canvas, grid, width):
    canvas.delete("all")
    gap = width // ROWS

    for row in grid:
        for node in row:
            x1 = node.col * gap
            y1 = node.row * gap
            x2 = x1 + gap
            y2 = y1 + gap
            canvas.create_rectangle(x1, y1, x2, y2, fill=node.color, outline="")

    DrawGrid(canvas, width)
    canvas.update()

# Determine the position the mouse
def GetClickedPos(event, width):
    gap = width // ROWS
    row = event.y // gap
    col = event.x // gap
    return row, col

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