def count_unique_paths_optimized(m, n):
    """
    Solves the standard path counting problem using O(n) space.
    """
    # dp array represents one row of the grid
    dp = [1] * n

    # Iterate for each row, starting from the second row
    for i in range(1, m):
        # Iterate for each column, starting from the second column
        for j in range(1, n):
            # dp[j] still holds the value from the row above
            # dp[j-1] holds the new value from the left in the current row
            dp[j] = dp[j] + dp[j-1]
            
    return dp[n-1]

