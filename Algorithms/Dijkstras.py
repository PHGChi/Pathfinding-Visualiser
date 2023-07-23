import math
import pygame

# Find the minimum weighted unexplored node from start node
def MinNode(grid):
	x = -1
	y = -1
	minDist = math.inf
	
	for rows in grid:
		for node in rows:
			# When a shorter unexplored distance is found
			if node.isVisited[0] == 0 and node.distance < minDist:
				x = node.row
				y = node.col
				minDist = node.distance

	return (x, y)	

# Draw the shortest path until we reach back to the start node
def DrawDijkstra(draw, grid, target):

	if target.predecessor[0] != (-1) and target.predecessor[1] != (-1): # Check for predecessor
		grid[target.predecessor[0]][target.predecessor[1]].MakePath()
		draw()
		DrawDijkstra(draw, grid, grid[target.predecessor[0]][target.predecessor[1]])

# Main implementation of the Dijkstra's algorithm
def Dijkstra(draw, grid, start, target):
	queue = []
	predecessor = {}

	# Add current node to the queue
	for rows in grid:
		for node in rows:
			startNode = (node.row, node.col)
			queue.append(startNode)

	grid[start.row][start.col].distance = 0

	while len(queue) > 0:
		# If user want to quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
	
		current = MinNode(grid)

		# Found shortest path, visualise it
		if(current[0] == target.row and current[1] == target.col):
			DrawDijkstra(draw, grid, target)
			return
		
		# Remove current node from queue and add it to visited nodes
		queue.remove(current)
		grid[current[0]][current[1]].isVisited[0] = 1
		grid[current[0]][current[1]].MakeClosed()

		# When there are no path from start to end node
		if(grid[current[0]][current[1]].distance == math.inf):
			return
		
		# Consider neighbour nodes of current node
		for neighbour in grid[current[0]][current[1]].neighbours:
			newDist = grid[current[0]][current[1]].distance + 1

			# Relax nodes when a shorter distance is found
			if newDist < neighbour.distance:
				neighbour.distance = newDist
				neighbour.predecessor = [current[0], current[1]]
				neighbour.MakeOpen()
				draw()