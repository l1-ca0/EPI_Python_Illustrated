def search_sequence_in_grid(grid, pattern):
    """
    Checks if a pattern exists in a grid where the same cell can be revisited
    """
    # A cache to store failed attempts to avoid re-computation
    # Key: (x, y, offset) -> bool
    # Value `True` means we've already confirmed this sub-path fails
    memo = set()
    
    def dfs(x, y, offset):
        """
        Recursively searches for the rest of the pattern (pattern[offset:])
        starting from grid cell (x, y)
        """
        # Base Case: Successfully found the entire pattern
        if offset == len(pattern):
            return True

        # Check for invalid states:
        # 1. Out of grid bounds
        # 2. Current grid cell doesn't match the pattern
        # 3. This sub-path fails (memoization)
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or \
           grid[x][y] != pattern[offset] or (x, y, offset) in memo:
            return False

        # Recursive Step: Explore all 4 neighbors for the next pattern element
        # If any neighbor finds a valid path, we succeed immediately
        # The expression `any(...)` returns True as soon as the first True is found
        if any(dfs(x + dx, y + dy, offset + 1) for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]):
            return True
        
        # If all neighbors fail, cache this failure and return False
        memo.add((x, y, offset))
        return False

    # Main Loop: Iterate through every cell to find a potential starting point
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If a starting cell is found, launch the DFS
            if dfs(i, j, 0):
                return True
                
    return False
