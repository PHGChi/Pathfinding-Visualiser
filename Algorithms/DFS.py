def ReconstructDFS(path, grid, draw):
    for node in path:
        grid[node[0]][node[1]].MakePath()
        draw()

def DFS (draw, grid, start, target, path, visited):
    startNode = (start.row, start.col)
    targetNode = (target.row, target.col)

    if startNode in visited:
        return path
    
    path += [startNode]
    visited += [startNode]

    grid[startNode[0]][startNode[1]].MakeClosed()

    # When the target node is found
    if startNode == targetNode:
        ReconstructDFS(path, grid, draw)
        return
    
    # Check neighbour
    for neighbour in grid[startNode[0]][startNode[1]].neighbours:
        neighbourNode = (neighbour.row, neighbour.col)

        if neighbour not in visited:
            grid[neighbourNode[0]][neighbourNode[1]].MakeOpen()
            draw()
            return DFS(draw, grid, neighbour, target, path, visited) # Recursively call DFS