import random

# Recursive Division algorithm to create a maze
def RecursiveDivisionA(grid, startRow, endRow, startCol, endCol):
    # Base case: If the region is too small, return
    if endRow <= startRow + 2 or endCol <= startCol + 2:
        return

    # Choose whether to divide horizontally or vertically
    if endRow - startRow > endCol - startCol:
        DivideHorizontally(grid, startRow, endRow, startCol, endCol)
    else:
        DivideVertically(grid, startRow, endRow, startCol, endCol)

# Divide the region horizontally and create gaps
def DivideHorizontally(grid, startRow, endRow, startCol, endCol):
    wallRow = startRow + 2 + random.randint(0, (endRow - startRow - 2) // 2) * 2
    for col in range(startCol, endCol + 1):
        grid[wallRow][col].MakeWall()

    gapCol = startCol + random.randint(0, (endCol - startCol) // 2) * 2
    grid[wallRow][gapCol].Reset()

    RecursiveDivisionA(grid, startRow, wallRow - 1, startCol, endCol)
    RecursiveDivisionA(grid, wallRow + 1, endRow, startCol, endCol)

# Divide the region vertically and create gaps
def DivideVertically(grid, startRow, endRow, startCol, endCol):
    wallCol = startCol + 2 + random.randint(0, (endCol - startCol - 2) // 2) * 2
    for row in range(startRow, endRow + 1):
        grid[row][wallCol].MakeWall()

    gapRow = startRow + random.randint(0, (endRow - startRow) // 2) * 2
    grid[gapRow][wallCol].Reset()

    RecursiveDivisionA(grid, startRow, endRow, startCol, wallCol - 1)
    RecursiveDivisionA(grid, startRow, endRow, wallCol + 1, endCol)