import pygame
from Grid.Path import ReconstructPath
from Helper.GlobalVariables import *

def Bidirectional(draw, grid, start, target):
    forwardQueue = [start]
    backwardQueue = [target]
    forwardVisited = {node: False for row in grid for node in row}
    backwardVisited = {node: False for row in grid for node in row}
    forwardPredecessor = {}
    backwardPredecessor = {}

    while forwardQueue and backwardQueue:
        # If the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Forward BFS
        currentForward = forwardQueue.pop(0)
        if forwardVisited[currentForward]:
            continue
        forwardVisited[currentForward] = True
        if currentForward != start:
            currentForward.MakeClosed()

        # Check forward node's neighbour
        for neighbour in currentForward.neighbours:
            if neighbour != start and not forwardVisited[neighbour]:
                forwardPredecessor[neighbour] = currentForward
                forwardQueue.append(neighbour)
                if neighbour != start and neighbour != target and not forwardVisited[neighbour]:
                    neighbour.MakeOpen()  

                # Check for meeting point between forward and backward searches
                if backwardVisited[neighbour]:
                    meetingNode = neighbour
                    # Merge the two paths and reconstruct the full path
                    path = []
                    while currentForward:
                        path.insert(0, currentForward)
                        currentForward = forwardPredecessor.get(currentForward)
                    currentBackward = backwardPredecessor.get(meetingNode)
                    while currentBackward:
                        path.append(currentBackward)
                        currentBackward = backwardPredecessor.get(currentBackward)
                    ReconstructPath(forwardPredecessor, meetingNode, draw)
                    ReconstructPath(backwardPredecessor, meetingNode, draw)
                    return True
        
        # Backward BFS
        currentBackward = backwardQueue.pop(0)
        if backwardVisited[currentBackward]:
            continue
        backwardVisited[currentBackward] = True
        if currentBackward != target:
            currentBackward.MakeClosed()

        # Check for backward's node neighbour
        for neighbour in currentBackward.neighbours:
            if neighbour != target and not backwardVisited[neighbour]:
                backwardPredecessor[neighbour] = currentBackward
                backwardQueue.append(neighbour)
                if neighbour != start and neighbour != target and not backwardVisited[neighbour]:
                    neighbour.MakeOpen()  

                # Check for meeting point between forward and backward searches
                if forwardVisited[neighbour]:
                    meetingNode = neighbour
                    # Merge the two paths and reconstruct the full path
                    path = []
                    while currentForward:
                        path.insert(0, currentForward)
                        currentForward = forwardPredecessor.get(currentForward)
                    currentBackward = backwardPredecessor.get(meetingNode)
                    while currentBackward:
                        path.append(currentBackward)
                        currentBackward = backwardPredecessor.get(currentBackward)
                    ReconstructPath(forwardPredecessor, meetingNode, draw)
                    ReconstructPath(backwardPredecessor, meetingNode, draw)
                    return True
        
        draw()
    return False # No path found