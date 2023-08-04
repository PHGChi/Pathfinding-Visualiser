import pygame
from collections import deque
from random import randint, choice
from Grid.Node import UpdateAllNeighbours

class Chamber:
    def __init__(self, xMin, xMax, yMin, yMax, xToAvoid=[], yToAvoid=[]):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax

        self.xToAvoid = xToAvoid
        self.yToAvoid = yToAvoid

        self.GetWallCenter()

    def GetWallCenter(self):
        xToAvoid = set(self.xToAvoid)
        yToAvoid = set(self.yToAvoid)

        # Candidate positions to avoid building walls
        xCands = [x for x in range(self.xMin + 1, self.xMax) if x not in xToAvoid]
        yCands = [y for y in range(self.yMin + 1, self.yMax) if y not in yToAvoid]

        if xCands and yCands:
            self.centerX = choice(xCands)
            self.centerY = choice(yCands)
            self.isQualified = True
        else:
            self.isQualified = False

    def BuildWalls(self, grid, draw):
        # Build vertically
        for node in grid[self.centerX][self.yMin:self.yMax + 1]:
            node.MakeWall()
            draw()
        
        # Build horizontally
        for col in grid[self.xMin:self.xMax + 1]:
            col[self.centerY].MakeWall()
            draw()

    def BuildWallsAndDoors(self, grid, draw):
        self.BuildWalls(grid, draw)

        # Store door's position of each side
        # {wallName: [minIndex, maxIndex, (doorX, doorY)]}
        self.walls = {
            'upper': [self.yMin, self.centerY - 1,
                      (self.centerX, randint(self.yMin, self.centerY - 1))],
            'lower': [self.centerY + 1, self.yMax,
                      (self.centerX, randint(self.centerY, self.yMax))],
            'left': [self.xMin, self.centerX - 1,
                      (randint(self.xMin, self.centerX - 1), self.centerY)],
            'right': [self.centerX + 1, self.xMax,
                      (randint(self.centerX + 1, self.xMax), self.centerY)]
        }

        # Create door
        rmWall = choice(['upper', 'lower', 'left', 'right'])
        self.walls[rmWall][2] = None, None

        for vals in self.walls.values():
            x,y = vals[2]
            if x != None:
                grid[x][y].Reset()

        draw()

    # Divide into subchambers for recursive divisions  
    def BuildSubChambers(self, stack):
        for vert in ['lower', 'upper']:
            for horiz in ['right', 'left']:
                colWall = self.walls[vert]
                rowWall = self.walls[horiz]

                xMin = rowWall[0]
                xMax = rowWall[1]
                yMin = colWall[0]
                yMax = colWall[1]
                xToAvoid = [rowWall[2][0]]
                yToAvoid = [colWall[2][1]]
                
                # Check for further division
                if (xMax - xMin >=3) and (yMax - yMin >= 3):
                    for x in self.xToAvoid:
                        if x != None and (xMin <= x <= xMax):
                            xToAvoid.append(x)

                    for y in self.yToAvoid:
                        if y != None and (yMin <= y <= yMax):
                            yToAvoid.append(y)

                    subChamber = Chamber(
                        xMin, xMax,
                        yMin, yMax,
                        xToAvoid, yToAvoid
                    )

                    stack.append(subChamber)

def RecursiveDivision(draw, grid, numCells):
    numCellsH, numCellsV = numCells

    begin = Chamber(0, numCellsH - 1, 0, numCellsV - 1)
    stack = deque([begin])

    while stack:
        chamber = stack.pop()
        if chamber.isQualified:
            chamber.BuildWallsAndDoors(grid, draw)
            chamber.BuildSubChambers(stack)
    
    grid = UpdateAllNeighbours(grid, None)

    return grid
            

