
    """The probability distribution given represents the probabilities of getting 0, 1, 2, or 3 heads when flipping three coins. 

The statement P(H < 3) = 0.875 represents the probability of getting less than 3 heads. This is the sum of the probabilities of getting 0, 1, or 2 heads, which is 0.125 + 0.375 + 0.375 = 0.875.

Here's how you can calculate this in Python:

```python
# Probability distribution
prob_distribution = {0: 0.125, 1: 0.375, 2: 0.375, 3: 0.125}

# Calculate P(H < 3)
p_h_less_than_3 = sum(value for key, value in prob_distribution.items() if key < 3)

print(p_h_less_than_3)  # Output: 0.875
```

This code first defines the probability distribution as a dictionary. 
It then calculates the sum of the probabilities for keys less than 3 
(i.e., 0, 1, and 2), and prints the result.
    """


# Probability distribution
prob_distribution = {0: 0.125, 1: 0.375, 2: 0.375, 3: 0.125}

# Calculate P(H < 3)
p_h_less_than_3 = sum(value for key, value in prob_distribution.items() if key < 3)

print(p_h_less_than_3)  # Output: 0.875


