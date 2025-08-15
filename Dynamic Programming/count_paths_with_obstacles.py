def count_paths_with_obstacles(obstacle_grid):
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0] * n for _ in range(m)]

    # Handle the starting cell
    if obstacle_grid[0][0] == 1:
        return 0
    dp[0][0] = 1
    
    # Fill first column
    for i in range(1, m):
        if obstacle_grid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
            
    # Fill first row
    for j in range(1, n):
        if obstacle_grid[0][j] == 0:
            dp[0][j] = dp[0][j-1]

    # Fill the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            if obstacle_grid[i][j] == 1:
                dp[i][j] = 0 # This cell is blocked
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    return dp[m-1][n-1]
