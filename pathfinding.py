import pygame
from queue import PriorityQueue

# Set the display
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Algorithm Visualiser")

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

    def Draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

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
    
    def __lt__(self, other):
        return False

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
        # If user want to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

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
def DrawGrid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRAY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GRAY, (j * gap, 0), (j * gap, width))

# Draw the grids
def Draw(win, grid, rows, width):
    win.fill(WHITE)
    
    for row in grid:
        for node in row:
            node.Draw(win)

    DrawGrid(win, rows, width)
    pygame.display.update()

# Determine the position the mouse
def GetClickedPos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main(win, width):
    ROWS = 50
    grid = MakeGrid(ROWS, width)

    start = None
    target = None

    isRun = True
    while isRun:
        Draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRun = False
            
            # Left click to change node's status
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, width)
                node = grid[row][col]
                # Choose start node
                if not start and node != target:
                    start = node
                    start.MakeStart()

                # Choose target node
                elif not target and node != start:
                    target = node
                    target.MakeTarget()

                # Choose wall node
                elif node != target and node != start:
                    node.MakeWall()
            
            # Right click to change node back to white
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = GetClickedPos(pos, ROWS, width)
                node = grid[row][col]
                node.Reset()
                if node == start:
                    start = None
                elif node == target:
                    target = None

            if event.type == pygame.KEYDOWN:
                # Run the algorithm
                if event.key == pygame.K_SPACE and start and target:
                    for row in grid:
                        for node in row:
                            node.UpdateNeighbours(grid)

                    AStar(lambda: Draw(win, grid, ROWS, width), grid, start, target)
                
                # Clear the board
                if event.key == pygame.K_c:
                    start = None
                    target = None
                    grid = MakeGrid(ROWS, width)
    pygame.quit()
main(WIN, WIDTH)