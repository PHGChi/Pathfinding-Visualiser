import pygame

#Draw the path found by the algorithm
def ReconstructPath(NodesVisited, current, draw):
    while current in NodesVisited:
        current = NodesVisited[current]
        if not current.IsStart(): #Don't colour the start node
            current.MakePath()
        draw()

def DFS(draw, grid, start, target):
    stack = []
    NodesVisited = {}

    stack.append(start)
    while stack: 
        #If user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.quit():
                pygame.quit()

        posCurrent = len(stack) - 1
        current = stack.pop(posCurrent)

        #If the current node is the target node
        if current == target:
            ReconstructPath(NodesVisited, target, draw)
            target.MakeTarget()
            return True
            
        if current not in NodesVisited: #Check if the node is already visisted
            NodesVisited.append(current)

            #Check the current node's neighbours
            for neighbour in current.neighbours:
                stack.append(neighbour)
        
        draw()
        #When there is on path between the start and end node
        if current != start:
            current.MakeClosed()

    return False