#!/usr/bin/env python3
"""
Example script demonstrating the maze solver.

This script shows how to use the maze solver with different algorithms and settings.
"""
import os
import sys
from typing import List

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from maze.maze_solver import Maze


def create_example_maze(filename: str) -> None:
    """
    Create an example maze file.
    
    Args:
        filename: Path to save the maze file
    """
    maze_data = [
        "####################",
        "#A        #        #",
        "#         #        #",
        "######### #        #",
        "#         #        #",
        "#    ######        #",
        "#         #        #",
        "#    #    #        #",
        "#    #    #        #",
        "#    #             #",
        "#    ###############",
        "#                  #",
        "#                  #",
        "#                 B#",
        "####################"
    ]
    
    with open(filename, 'w') as f:
        for line in maze_data:
            f.write(line + '\n')


def solve_maze(maze_file: str, output_prefix: str) -> None:
    """
    Solve a maze using both BFS and DFS algorithms.
    
    Args:
        maze_file: Path to the maze file
        output_prefix: Prefix for the output image files
    """
    # Solve with DFS
    print(f"Solving maze {maze_file} with DFS...")
    maze = Maze(maze_file)
    if maze.solve(algorithm="dfs"):
        print("DFS Solution:")
        maze.print()
        dfs_output = f"{output_prefix}_dfs_solution.png"
        maze.output_image(dfs_output, show_explored=True)
        print(f"DFS solution saved to {dfs_output}")
    else:
        print("No DFS solution found.")
    
    # Solve with BFS
    print(f"\nSolving maze {maze_file} with BFS...")
    maze = Maze(maze_file)
    if maze.solve(algorithm="bfs"):
        print("BFS Solution:")
        maze.print()
        bfs_output = f"{output_prefix}_bfs_solution.png"
        maze.output_image(bfs_output, show_explored=True)
        print(f"BFS solution saved to {bfs_output}")
    else:
        print("No BFS solution found.")


def main() -> None:
    """Run the maze solver examples."""
    print("Maze Solver Examples")
    print("===================")
    
    # Create an example maze file
    example_maze = "example_maze.txt"
    create_example_maze(example_maze)
    print(f"Created example maze in {example_maze}")
    
    # Solve the example maze
    solve_maze(example_maze, "example_maze")
    
    # If a maze.txt file exists in the project, also solve that
    project_maze = os.path.join(os.path.dirname(__file__), "..", "maze.txt")
    if os.path.exists(project_maze):
        print(f"\nFound project maze at {project_maze}")
        solve_maze(project_maze, "project_maze")


if __name__ == "__main__":
    main()
