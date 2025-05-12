# Topic 14: Dynamic Programming (DP)

# Task 1: Implementing the Fibonacci Sequence Using DP (Memoization & Tabulation)

# Fibonacci using Memoization (Top-Down Approach)
def fib_memoization(n, memo={}):
    if n in memo:  # Check if result is already computed
        return memo[n]
    if n <= 1:  # Base cases
        return n
    # Recursive computation with memoization
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

# Fibonacci using Tabulation (Bottom-Up Approach)
def fib_tabulation(n):
    if n <= 1:  # Base cases
        return n
    # Initialize the table to store Fibonacci values
    table = [0] * (n + 1)
    table[1] = 1
    # Fill the table iteratively
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

# Example Input & Output
print(fib_memoization(10))  # Output: 55
print(fib_tabulation(10))  # Output: 55

# Performance Comparison
import time

n = 35  # Test with a larger value for performance comparison

# Measure time for Memoization
start_time = time.time()
fib_memoization(n)
memoization_time = time.time() - start_time

# Measure time for Tabulation
start_time = time.time()
fib_tabulation(n)
tabulation_time = time.time() - start_time

print(f"Memoization Time: {memoization_time:.6f} seconds")
print(f"Tabulation Time: {tabulation_time:.6f} seconds")

# Task 2: Implementing the Longest Common Subsequence (LCS) Algorithm

# LCS using Recursion + Memoization
def lcs_memoization(X, Y, m, n, memo):
    if m == 0 or n == 0:  # Base case: if either string is empty
        return 0
    if (m, n) in memo:  # Check if result is already computed
        return memo[(m, n)]
    if X[m - 1] == Y[n - 1]:  # If last characters match
        memo[(m, n)] = 1 + lcs_memoization(X, Y, m - 1, n - 1, memo)
    else:  # If last characters don't match
        memo[(m, n)] = max(lcs_memoization(X, Y, m - 1, n, memo),
                           lcs_memoization(X, Y, m, n - 1, memo))
    return memo[(m, n)]

# LCS using Tabulation (Bottom-Up Approach)
def lcs_tabulation(X, Y):
    m, n = len(X), len(Y)
    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Fill the table iteratively
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # If characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # If characters don't match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# Example Input & Output
X = "AGGTAB"
Y = "GXTXAYB"

# Using Memoization
memo = {}
lcs_length_memo = lcs_memoization(X, Y, len(X), len(Y), memo)
print(f"LCS Length (Memoization): {lcs_length_memo}")  # Output: 4

# Using Tabulation
lcs_length_tab = lcs_tabulation(X, Y)
print(f"LCS Length (Tabulation): {lcs_length_tab}")  # Output: 4


# Task 3: Implementing the 0/1 Knapsack Problem Using Dynamic Programming

# 0/1 Knapsack Problem using Tabulation (Bottom-Up Approach)
def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP table where dp[i][w] represents the maximum value
    # that can be achieved with the first i items and weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table iteratively
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # If the current item's weight is less than or equal to w
                # Include the item or exclude it, take the maximum value
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]

    # The maximum value is stored in dp[n][capacity]
    return dp[n][capacity]

# Example Input & Output
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

# Maximum value that can be obtained
max_value = knapsack(weights, values, capacity)
print(f"Maximum Value: {max_value}")  # Output: 7

