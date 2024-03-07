# Probability distribution
prob_distribution = {0: 0.125, 1: 0.375, 2: 0.375, 3: 0.125}

# Calculate P(H < 3)
p_h_less_than_3 = sum(value for key, value in prob_distribution.items() if key < 3)

print(p_h_less_than_3)  # Output: 0.875