#!/usr/bin/env python3
"""
Example script demonstrating the knapsack problem solver.

This script shows how to use the knapsack solver with different problem instances.
"""
from typing import List, Tuple

from sorting.Knapsack import knapsack_01


def print_knapsack_solution(
    weights: List[int], values: List[int], capacity: int
) -> None:
    """
    Print the solution to a knapsack problem.

    Args:
        weights: List of item weights
        values: List of item values
        capacity: Knapsack capacity
    """
    print(f"Problem: Capacity = {capacity}")
    print("Items:")
    for i, (w, v) in enumerate(zip(weights, values), 1):
        print(f"  Item {i}: Weight = {w}, Value = {v}")

    try:
        total_weight, total_value, num_items, selected_items = knapsack_01(
            weights, values, capacity
        )

        print("\nSolution:")
        print(f"  Total value: {total_value}")
        print(f"  Total weight: {total_weight}/{capacity}")
        print(f"  Number of items: {num_items}")
        print("  Selected items:")
        for item in selected_items:
            idx = item - 1  # Convert from 1-indexed to 0-indexed
            print(f"    Item {item}: Weight = {weights[idx]}, Value = {values[idx]}")

        print(f"\n  Efficiency: {total_value/total_weight:.2f} value/weight")
    except ValueError as e:
        print(f"Error: {e}")

    print("\n" + "-" * 50 + "\n")


def main() -> None:
    """Run examples of the knapsack problem."""
    print("Knapsack Problem Examples")
    print("========================")

    # Example 1: Basic problem
    weights1 = [10, 20, 30]
    values1 = [60, 100, 120]
    capacity1 = 50
    print_knapsack_solution(weights1, values1, capacity1)

    # Example 2: Larger problem
    weights2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    values2 = [50, 120, 150, 200, 300, 350, 500, 700, 900]
    capacity2 = 200
    print_knapsack_solution(weights2, values2, capacity2)

    # Example 3: Items with same ratio of value to weight
    weights3 = [10, 20, 30, 40]
    values3 = [10, 20, 30, 40]  # All have value/weight ratio = 1
    capacity3 = 50
    print_knapsack_solution(weights3, values3, capacity3)

    # Example 4: Problem with some heavy but valuable items
    weights4 = [5, 10, 15, 20, 100]
    values4 = [10, 30, 20, 50, 300]
    capacity4 = 100
    print_knapsack_solution(weights4, values4, capacity4)


if __name__ == "__main__":
    main()
