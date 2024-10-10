# Function to solve the 0/1 Knapsack problem
def knapsack(capacity, weights, values, n):
    # Create an array to store the maximum for subproblems
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Item can be included: choose the maximum of including or not including the item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Item cannot be included, take the value without this item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # The maximum value with all items considered and full capacity


# Example usage
values = [30, 80, 110]  # Values of the items
weights = [15, 20, 25]   # Weights of the items
capacity = 40            # Maximum weight capacity of the knapsack
n = len(values)          # Number of items

max_value = knapsack(capacity, weights, values, n)
print(f"The maximum value that can be put in the knapsack is {max_value}")
