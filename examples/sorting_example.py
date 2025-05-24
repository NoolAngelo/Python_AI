#!/usr/bin/env python3
"""
Example script demonstrating the sorting algorithms in the package.

This script runs each sorting algorithm on the same input data and compares their results.
"""
from typing import List, Callable, Any
import time
import random

# Import all sorting algorithms
from sorting.bubble_sort import bubble
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort as quicksort
from sorting.Selection_sort import selection_sort


def benchmark_sort(
    sort_func: Callable[[List[int]], List[int]], data: List[int], name: str
) -> None:
    """
    Benchmark a sorting function and print its execution time.

    Args:
        sort_func: The sorting function to benchmark
        data: The input data to sort (will be copied to avoid modifying original)
        name: Name of the sorting algorithm
    """
    # Create a copy of the data to avoid modifying the original
    data_copy = data.copy()

    # Measure execution time
    start = time.time()
    result = sort_func(data_copy)
    end = time.time()

    # Print results
    print(
        f"{name:15} | Time: {end - start:.6f} seconds | Sorted correctly: {is_sorted(result)}"
    )


def is_sorted(data: List[Any]) -> bool:
    """
    Check if a list is sorted.

    Args:
        data: List to check

    Returns:
        bool: True if the list is sorted, False otherwise
    """
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))


def main() -> None:
    """Run benchmarks for all sorting algorithms."""
    print("Sorting Algorithm Benchmarks")
    print("===========================")

    # Generate random data
    data_sizes = [100, 1000, 5000]

    for size in data_sizes:
        print(f"\nData size: {size} elements")
        print("-" * 40)

        # Generate random data
        random.seed(42)  # For reproducible results
        data = [random.randint(1, 10000) for _ in range(size)]

        # Benchmark each algorithm
        benchmark_sort(bubble, data, "Bubble Sort")
        benchmark_sort(insertion_sort, data, "Insertion Sort")
        benchmark_sort(merge_sort, data, "Merge Sort")
        benchmark_sort(quicksort, data, "Quick Sort")
        benchmark_sort(selection_sort, data, "Selection Sort")

        # Also benchmark Python's built-in sort for comparison
        start = time.time()
        sorted_data = sorted(data)
        end = time.time()
        print(
            f"{'Python sorted()':15} | Time: {end - start:.6f} seconds | Sorted correctly: {is_sorted(sorted_data)}"
        )


if __name__ == "__main__":
    main()
