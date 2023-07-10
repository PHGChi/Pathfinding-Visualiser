import pygame
from queue import PriorityQueue

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

