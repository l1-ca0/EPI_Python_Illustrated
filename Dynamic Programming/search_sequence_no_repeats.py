def search_sequence_no_repeats(grid, pattern):
    """
    Checks if a pattern exists in a grid where a cell cannot be visited twice
    in the same path
    """
    def backtrack_dfs(x, y, offset, visited):
        """
        Backtracking search that keeps track of visited cells for the current path
        """
        # Base Case: We've successfully matched the whole pattern
        if offset == len(pattern):
            return True

        # Check for invalid moves
        # Note that we don't need boundary checks
        # if the caller ensures the first call is valid
        
        # Mark the current cell as visited for this path
        visited.add((x, y))
        
        # Explore neighbors
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_x, next_y = x + dx, y + dy
            
            # Check if neighbor is valid and not already visited
            if (0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and
                (next_x, next_y) not in visited and
                grid[next_x][next_y] == pattern[offset]):
                
                # If a path is found from the neighbor, we are done
                if backtrack_dfs(next_x, next_y, offset + 1, visited):
                    return True

        # Backtrack: Un-mark the cell so it can be used in other paths
        visited.remove((x, y))
        return False

    # Main Loop: Find a starting point
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == pattern[0]:
                # Launch the search with the starting cell and an initial offset of 1
                if backtrack_dfs(i, j, 1, set()):
                    return True
    return False
