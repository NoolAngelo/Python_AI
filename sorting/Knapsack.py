def knapsack_01(weights, values, capacity):
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

# Example usage
weights = [15, 10, 25, 8, 20, 18, 12, 5, 22, 14]
values = [30, 20, 40, 12, 35, 30, 18, 10, 45, 25]
capacity = 100

total_weight, total_value, total_items_used, selected_items = knapsack_01(weights, values, capacity)

print("Selected items:")
for item in selected_items:
    print(f"Item {item}: Weight {weights[item - 1]}, Value {values[item - 1]}")

print("\nTotal Weight of Selected Items:", total_weight)
print("Total Value of Selected Items:", total_value)
print("Total Items Used:", total_items_used)
