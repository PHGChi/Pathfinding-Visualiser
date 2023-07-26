import pygame

def DrawDFS(path, grid, draw):
	for node in path:
		grid[node[0]][node[1]].MakePath()
		draw()

def DFS(draw, grid, start, target, path, visited):
    stack = []
    visited = []
    
    startPOS = (start.row, start.col)
    targetPOS = (target.row, target.col)
    stack.append([startPOS])
    
    path.append([startPOS])
    visited.append([startPOS])
    
    grid[startPOS[0]][startPOS[1]].MakeClosed()
        
    # When the target node is found
    if startPOS == targetPOS:
        DrawDFS(path, grid, draw)
        return

    # Find path from neighbours
    for neighbour in grid[startPOS[0]][startPOS[1]].neighbours:
        # If user want to quit
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  pygame.quit()
        
        neighbourPOS = (neighbour.row, neighbour.col)
        
        if neighbour not in visited:		
            grid[neighbourPOS[0]][neighbourPOS[1]].MakeOpen()	
            draw()
            return DFS(draw, grid, neighbour, target, path, visited) # Recursively call DFS function