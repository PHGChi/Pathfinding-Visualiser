import pygame
from Grid.Path import ReconstructPath

def BFS(draw, grid, start, target):
    visited = {node: False for row in grid for node in row}
    predecessor = {}
    queue = []
    queue.append(start)

    while queue:
        # If the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = queue.pop(0)

        if visited[current]:
            continue
        visited[current] = True

        # If target node is found
        if current == target:
            ReconstructPath(predecessor, target, draw)
            return True
        
        if current != start:
            current.MakeClosed()
        
        # Check the neighbours of the current node
        for neighbour in current.neighbours:
            if neighbour != start and not visited[neighbour]:
                predecessor[neighbour] = current
                queue.append(neighbour)
            if neighbour != target and neighbour != start and not visited[neighbour]:
                neighbour.MakeOpen()  
        draw()
    return False