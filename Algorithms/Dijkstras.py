import math
import pygame
from queue import PriorityQueue
from Grid.Path import ReconstructPath

def Dijkstra(draw, grid, start, target):
	visited = {node: False for row in grid for node in row}
	distance = {node: math.inf for row in grid for node in row}
	distance[start] = 0
	predecessor = {}
	pQueue = PriorityQueue()
	pQueue.put((0, start))

	while not pQueue.empty():
		# If user want to quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = pQueue.get()[1]

		if visited[current]:
			continue
		visited[current] = True

		# If the target node is found
		if current == target:
			ReconstructPath(predecessor, target, draw)
			return True
		
		if current != start:
			current.MakeClosed()

		# Check the neighbours of current nodes
		for neighbour in current.neighbours:
			# Relax the edges
			if distance[current] + 1 < distance[neighbour]:
				predecessor[neighbour] = current
				distance[neighbour] = distance[current] + 1
				pQueue.put((distance[neighbour], neighbour))
			if neighbour != target and neighbour != start and not visited[neighbour]:
				neighbour.MakeOpen()
		draw()
	return False