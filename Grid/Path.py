from Helper.GlobalVariables import *

# Draw the shortest path until we reach back to the start node
def ReconstructPath(predecessor, current, draw):
    while current in predecessor:
      current = predecessor[current]
      current.MakePath()
      draw()

def ResetPath(grid):
   # Reset previous paths
    for row in grid:
        for node in row:
            if node.IsClosed() or node.IsOpen() or node.colour == ORANGE:
                node.Reset()