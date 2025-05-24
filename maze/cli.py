#!/usr/bin/env python3
"""
Command line interface for the maze solver.

Usage:
  python -m maze.cli [maze_file] [options]

Options:
  --algorithm/-a: Specify the algorithm ('bfs' or 'dfs', default: 'dfs')
  --output/-o: Output image filename (default: 'maze_solution.png')
  --show-explored/-e: Show explored states in the output image
"""
import sys
import argparse
from maze.maze_solver import Maze

def main():
    """Run the maze solver from the command line."""
    parser = argparse.ArgumentParser(description="Solve a maze using BFS or DFS")
    parser.add_argument("maze_file", help="Path to the maze file")
    parser.add_argument("-a", "--algorithm", choices=["bfs", "dfs"], default="dfs",
                        help="Algorithm to use (default: dfs)")
    parser.add_argument("-o", "--output", default="maze_solution.png",
                        help="Output image filename (default: maze_solution.png)")
    parser.add_argument("-e", "--show-explored", action="store_true",
                        help="Show explored states in the output image")
    
    args = parser.parse_args()
    
    try:
        print(f"Loading maze from {args.maze_file}...")
        maze = Maze(args.maze_file)
        
        print(f"Solving maze using {args.algorithm.upper()}...")
        maze.solve(algorithm=args.algorithm)
        
        print("Maze solution:")
        maze.print()
        
        print(f"Saving solution to {args.output}...")
        maze.output_image(args.output, show_explored=args.show_explored)
        
        print("Done!")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
