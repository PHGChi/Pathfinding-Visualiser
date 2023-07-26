import pygame

def DrawBFS(path, grid, draw):
       for node in path:
             grid[node[0]][node[1]].MakePath()
             draw()

def BFS(draw, grid, start, target):
    queue = []
    startPOS = (start.row, start.col)
    queue.append([startPOS])

    while queue:
        # If the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        path = []
        path = queue.pop(0)
        current = path[-1]

        grid[current[0]][current[1]].isVisited[0] = 1
        grid[current[0]][current[1]].MakeClosed()

        if grid[current[0]][current[1]] == target:
               DrawBFS(path, grid, draw)
               return
        
        # Check neighbour's node
        for neighbour in grid[current[0]][current[1]].neighbours:
               if grid[neighbour.row][neighbour.col].isVisited[0] == 0:
                      neighbour.MakeOpen()
                      newPath = list(path)
                      neighbourPOS = (neighbour.row, neighbour.col)
                      newPath.append(neighbourPOS)
                      queue.append(newPath)
                      grid[neighbour.row][neighbour.col].isVisisted = 1
                      draw()