#!/usr/bin/env python3
"""
Main CLI entry point for the Python_AI package.

This script provides a command-line interface to access various
algorithms and utilities in the package.
"""
import sys
import argparse
from typing import Optional, List


def main(args: Optional[List[str]] = None) -> int:
    """
    Main entry point for the CLI.
    
    Args:
        args: Command line arguments (defaults to sys.argv[1:] if None)
    
    Returns:
        int: Exit code (0 for success)
    """
    parser = argparse.ArgumentParser(
        description="Python_AI: Collection of algorithms and AI techniques",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Maze solver command
    maze_parser = subparsers.add_parser("maze", help="Solve a maze")
    maze_parser.add_argument("maze_file", help="Path to the maze file")
    maze_parser.add_argument("-a", "--algorithm", choices=["bfs", "dfs"], default="dfs",
                            help="Algorithm to use (default: dfs)")
    maze_parser.add_argument("-o", "--output", default="maze_solution.png",
                            help="Output image filename (default: maze_solution.png)")
    maze_parser.add_argument("-e", "--show-explored", action="store_true",
                            help="Show explored states in the output image")
    
    # Sorting command
    sort_parser = subparsers.add_parser("sort", help="Sort a list of numbers")
    sort_parser.add_argument("numbers", nargs="+", type=int, help="Numbers to sort")
    sort_parser.add_argument("-a", "--algorithm", 
                            choices=["bubble", "insertion", "merge", "quick", "selection"],
                            default="quick", help="Sorting algorithm to use (default: quick)")
    
    # Knapsack command
    knapsack_parser = subparsers.add_parser("knapsack", help="Solve a knapsack problem")
    knapsack_parser.add_argument("-w", "--weights", required=True, type=int, nargs="+",
                               help="Weights of items")
    knapsack_parser.add_argument("-v", "--values", required=True, type=int, nargs="+",
                               help="Values of items")
    knapsack_parser.add_argument("-c", "--capacity", required=True, type=int,
                               help="Capacity of the knapsack")
    
    # Parse the arguments
    parsed_args = parser.parse_args(args)
    
    # Handle no command
    if not parsed_args.command:
        parser.print_help()
        return 0
    
    # Handle the different commands
    if parsed_args.command == "maze":
        from maze.maze_solver import Maze
        
        maze = Maze(parsed_args.maze_file)
        if maze.solve(algorithm=parsed_args.algorithm):
            print("Solution found!")
            maze.print()
            maze.output_image(parsed_args.output, show_explored=parsed_args.show_explored)
            print(f"Solution image saved to {parsed_args.output}")
        else:
            print("No solution found.")
            
    elif parsed_args.command == "sort":
        if parsed_args.algorithm == "bubble":
            from sorting.bubble_sort import bubble
            result = bubble(parsed_args.numbers)
        elif parsed_args.algorithm == "insertion":
            from sorting.insertion_sort import insertion_sort
            result = insertion_sort(parsed_args.numbers)
        elif parsed_args.algorithm == "merge":
            from sorting.merge_sort import merge_sort
            result = merge_sort(parsed_args.numbers)
        elif parsed_args.algorithm == "quick":
            from sorting.quick_sort import quicksort
            result = quicksort(parsed_args.numbers)
        elif parsed_args.algorithm == "selection":
            from sorting.Selection_sort import selection_sort
            result = selection_sort(parsed_args.numbers)
        
        print(f"Original: {parsed_args.numbers}")
        print(f"Sorted:   {result}")
        
    elif parsed_args.command == "knapsack":
        from sorting.Knapsack import knapsack_01
        
        if len(parsed_args.weights) != len(parsed_args.values):
            print("Error: Number of weights must match number of values.")
            return 1
        
        total_weight, total_value, num_items, selected = knapsack_01(
            parsed_args.weights, parsed_args.values, parsed_args.capacity
        )
        
        print(f"Knapsack problem with capacity {parsed_args.capacity}:")
        print(f"Total value: {total_value}")
        print(f"Total weight: {total_weight}")
        print(f"Items selected: {len(selected)}")
        print("Selected items:")
        for item in selected:
            idx = item - 1  # Convert from 1-indexed to 0-indexed
            print(f"  Item {item}: Weight = {parsed_args.weights[idx]}, Value = {parsed_args.values[idx]}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
