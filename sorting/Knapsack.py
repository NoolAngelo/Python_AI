def knapsack_01(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights (list): List of item weights.
        values (list): List of item values.
        capacity (int): Maximum capacity of the knapsack.
    
    Returns:
        tuple: (total_weight, total_value, total_items_used, selected_items)
    """
    if not weights or not values or capacity <= 0:
        raise ValueError("Invalid input: weights, values, and capacity must be positive.")
    
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    included_items = set()

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    # Trace back to find the selected items
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            included_items.add(i)
            w -= weights[i - 1]
        i -= 1

    total_weight = sum(weights[i - 1] for i in included_items)
    total_value = sum(values[i - 1] for i in included_items)
    total_items_used = len(included_items)
    selected_items = sorted(list(included_items))

    return total_weight, total_value, total_items_used, selected_items

# Interactive example usage
if __name__ == "__main__":
    try:
        weights_input = input("Enter weights separated by spaces: ")
        values_input = input("Enter values separated by spaces: ")
        capacity_input = input("Enter knapsack capacity: ")

        weights = list(map(int, weights_input.split()))
        values = list(map(int, values_input.split()))
        capacity = int(capacity_input)

        total_weight, total_value, total_items_used, selected_items = knapsack_01(weights, values, capacity)

        print("Selected items:")
        for item in selected_items:
            print(f"Item {item}: Weight {weights[item - 1]}, Value {values[item - 1]}")

        print("\nTotal Weight of Selected Items:", total_weight)
        print("Total Value of Selected Items:", total_value)
        print("Total Items Used:", total_items_used)
    except ValueError as e:
        print(f"Error: {e}")
