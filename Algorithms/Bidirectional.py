import pygame
from Grid.Path import ReconstructPath

def Bidirectional(draw, grid, start, target):
    visited = {node: False for row in grid for node in row}
    predecessor = {}
    queue1 = []
    queue2 = []
    queue1.append(start)
    queue2.append(target)

    while queue1 and queue2:
        # If the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current1 = queue1.pop(0)
        current2 = queue2.pop(0)

        if visited[current1]:
            continue
        visited[current1] = True

        # If target node is found
        if current1 == target:
            ReconstructPath(predecessor, target, draw)
            return True
        
        if current1 != start:
            current1.MakeClosed()