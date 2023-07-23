import pygame
from queue import PriorityQueue

# Find the manhattan distance as the heuristic
def Heuristic(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  return abs(x1 - x2) + abs(y1 - y2)

# Draw the shortest path until we reach back to the start node
def ReconstructPath(predecessor, current, draw):
    while current in predecessor:
      current = predecessor[current]
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
  fScore[start] = Heuristic(start.GetPos(), target.GetPos())
  
  setOpenHash = {start}

  while not setOpen.empty(): # Break when there is no path from start to end node
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
        
    # Consider neighbour nodes of current node
    for neighbour in current.neighbours:
      tempGScore = gScore[current] + 1
      
      # Relax nodes when better distance is found
      if tempGScore < gScore[neighbour]:
        predecessor[neighbour] = current
        gScore[neighbour] = tempGScore
        fScore[neighbour] = tempGScore + Heuristic(neighbour.GetPos(), target.GetPos())
        if neighbour not in setOpenHash:
          count += 1
          setOpen.put((fScore[neighbour], count, neighbour))
          setOpenHash.add(neighbour)
          neighbour.MakeOpen()

    draw()
    if current != start:
      current.MakeClosed()
  return False

