"""
Tests for the knapsack problem solver.
"""

import sys
import os

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sorting.Knapsack import knapsack_01


def test_knapsack_basic():
    """Test basic knapsack functionality."""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    total_weight, total_value, num_items, selected = knapsack_01(
        weights, values, capacity
    )

    # For this test case, optimal solution should include items 2 and 3 (1-indexed)
    # which corresponds to weights [20, 30] and values [100, 120]
    assert total_value == 220  # 100 + 120
    assert total_weight == 50  # 20 + 30
    assert set(selected) == {2, 3}  # Items 2 and 3 (1-indexed)


def test_knapsack_empty():
    """Test knapsack with empty inputs."""
    try:
        knapsack_01([], [], 50)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_knapsack_no_capacity():
    """Test knapsack with no capacity."""
    weights = [10, 20, 30]
    values = [60, 100, 120]

    try:
        knapsack_01(weights, values, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_knapsack_large():
    """Test knapsack with larger inputs."""
    weights = [10, 20, 30, 40, 50]
    values = [60, 100, 120, 140, 160]
    capacity = 100

    total_weight, total_value, num_items, selected = knapsack_01(
        weights, values, capacity
    )

    # The optimal solution is to take items 1,2,3,4 (1-indexed)
    # which yields total value of 420 (60+100+120+140) and weight 100
    assert total_value == 420
    assert total_weight == 100
    assert set(selected) == {1, 2, 3, 4}


if __name__ == "__main__":
    # Run all tests
    test_knapsack_basic()
    test_knapsack_empty()
    test_knapsack_no_capacity()
    test_knapsack_large()
    print("All knapsack tests completed.")
