def count_unique_paths(m, n):
    """
    Calculates the number of unique paths in an m x n grid
    from (0,0) to (m-1, n-1) moving only right and down.
    """
    # Create a 2D array to store the number of paths to each cell
    dp = [[0] * n for _ in range(m)]

    # Base case: There's 1 way to reach any cell in the first row or column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
        
    # Fill the rest of the grid using the recurrence relation
    for i in range(1, m):
        for j in range(1, n):
            # Ways to reach here = (ways from above) + (ways from left)
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    # The bottom-right corner holds the final answer
    return dp[m-1][n-1]

