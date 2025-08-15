def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # Fill first column
    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i-1][0]
    # Fill first row
    for j in range(1, n):
        dp[0][j] = grid[0][j] + dp[0][j-1]

    # Fill the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            # Cost of this cell + the minimum cost from the previous cells
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
            
    return dp[m-1][n-1]

