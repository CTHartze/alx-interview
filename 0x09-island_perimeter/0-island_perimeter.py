#!/usr/bin/python3
"""Island Perimeter Problem"""


def island_perimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    # Helper function to check if cell is within the grid and is land
    def is_land(i, j):
        return 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1

    # Iterates through each cell in grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If current cell is land
                # Check each neighboring cell and perimeter if water or edge
                perimeter += 4  # Assumes 4 sides initially
                if is_land(i - 1, j):
                    perimeter -= 1
                if is_land(i + 1, j):
                    perimeter -= 1
                if is_land(i, j - 1):
                    perimeter -= 1
                if is_land(i, j + 1):
                    perimeter -= 1

    return perimeter
