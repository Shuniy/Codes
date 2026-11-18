def rat_in_maze(maze: list[list[int]]):
    """
    Solves the rat in a maze problem using backtracking.

    Given a maze represented as a 2D list of integers where 1 indicates a path and 0 indicates a wall,
    this function finds all possible paths from the top-left corner to the bottom-right corner of the maze.
    Each path is represented as a string of directions: 'l' for left, 'r' for right, 'd' for down, and 'u' for up.

    Args:
        maze (list[list[int]]): A 2D list representing the maze layout.

    Returns:
        list: A list of strings, each string representing a valid path through the maze.
    """

    result = []
    directions = {(0, -1): "l", (0, 1): "r", (1, 0): "d", (-1, -0): "u"}
    rat_in_mazeHelper(maze, directions, 0, 0, "", result)
    return result

def rat_in_mazeHelper(maze: list[list[int]], directions: dict, i: int, j: int, path: str, result: list):
    """
    A helper function for the rat_in_maze function.

    This function is a recursive helper for the rat_in_maze function. It takes a maze, a dictionary of directions,
    the current coordinates, the current path, and a list of solutions. It checks if the current coordinates are
    within the maze, then checks if the current coordinates are at the end of the maze. If they are, it adds the
    current path to the list of solutions. If not, it sets the current cell in the maze to 0, then recursively calls
    itself for each direction in the directions dictionary. Finally, it sets the current cell back to its original
    value.

    Args:
        maze (list[list[int]]): A 2D list representing the maze layout.
        directions (dict): A dictionary mapping tuples of two integers to strings representing directions.
        i (int): The current row index in the maze.
        j (int): The current column index in the maze.
        path (str): The current path through the maze.
        result (list): A list of strings, each string representing a valid path through the maze.
    """
    if i < 0 or i >= len(maze) or j >= len(maze[0]) or j < 0 or maze[i][j] == 0:
        return
    if i == len(maze) - 1 and j == len(maze[0]) - 1:
        result.append(path)
        return
    maze[i][j] = 0
    for direction in directions:
        rat_in_mazeHelper(maze, directions, i + direction[0], j + direction[1], path + directions[direction], result)
    maze[i][j] = 1

# test cases
print(rat_in_maze([[1, 0, 0, 0], 
                   [1, 1, 0, 1], 
                   [0, 1, 0, 0], 
                   [1, 1, 1, 1]]))
print(rat_in_maze([[1, 0, 0, 0], 
                   [1, 1, 0, 1], 
                   [1, 1, 0, 0], 
                   [0, 1, 1, 1]]))
print(rat_in_maze([[1, 0, 0, 0], 
                   [1, 1, 0, 1], 
                   [0, 0, 1, 0], 
                   [1, 1, 1, 1]]))
print(rat_in_maze([[1, 0], 
                   [1, 0]]))
print(rat_in_maze([[1, 1, 1], 
                   [1, 0, 1], 
                   [1, 1, 1]]))