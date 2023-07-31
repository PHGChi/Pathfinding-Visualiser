import random
from Helper.GlobalVariables import *
# Function to generate a maze using recursive division algorithm
def generate_maze_recursive_division(grid, x_start, x_end, y_start, y_end):
    # Calculate the width and height of the section
    width = x_end - x_start
    height = y_end - y_start

    if width <= 2 or height <= 2:
        return

    # Choose the orientation (horizontal or vertical) to divide the section
    if width > height:
        # Divide the section horizontally
        wall_y = random.randrange(y_start + 1, y_end, 2)  # Choose a random odd y-coordinate for the wall
        for x in range(x_start, x_end):
            if x != WIDTH // 2:  # Ensure a passage is left at the center of the grid
                grid[x][wall_y].MakeWall()

        # Create an opening in the wall at a random position
        passage_x = random.choice([x_start + 1, x_end - 1])
        grid[passage_x][wall_y].Reset()

        # Recursively generate mazes in the two sections on either side of the wall
        generate_maze_recursive_division(grid, x_start, x_end, y_start, wall_y)
        generate_maze_recursive_division(grid, x_start, x_end, wall_y + 1, y_end)
    else:
        # Divide the section vertically
        wall_x = random.randrange(x_start + 1, x_end, 2)  # Choose a random odd x-coordinate for the wall
        for y in range(y_start, y_end):
            if y != HEIGHT // 2:  # Ensure a passage is left at the center of the grid
                grid[wall_x][y].MakeWall()

        # Create an opening in the wall at a random position
        passage_y = random.choice([y_start + 1, y_end - 1])
        grid[wall_x][passage_y].Reset()

        # Recursively generate mazes in the two sections on either side of the wall
        generate_maze_recursive_division(grid, x_start, wall_x, y_start, y_end)
        generate_maze_recursive_division(grid, wall_x + 1, x_end, y_start, y_end)
