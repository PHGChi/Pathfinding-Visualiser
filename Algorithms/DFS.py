import pygame
from Grid.Path import ReconstructPath

def DFS(draw, grid, start, target):
    visited = {node: False for row in grid for node in row}
    predecessor = {}
    stack = []
    stack.append(start)

    while stack:
        # If the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        lastNode = len(stack) - 1
        current = stack.pop(lastNode)

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
                stack.append(neighbour)
            if neighbour != target and neighbour != start and not visited[neighbour]:
                neighbour.MakeOpen()  
        draw()
    return False