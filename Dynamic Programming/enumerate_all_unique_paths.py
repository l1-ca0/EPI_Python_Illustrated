def enumerate_all_unique_paths(grid, pattern):
    """
    Finds all unique, non-repeating paths for a pattern in a grid
    """
    all_valid_paths = []
    
    def backtrack_enumerate(x, y, offset, current_path):
        """
        Backtracking search that enumerates all valid paths
        `current_path` is a list of (x,y) tuples
        """
        # Base Case: Successfully reached the end of the pattern
        if offset == len(pattern):
            all_valid_paths.append(list(current_path)) # Add a copy of the path
            return

        # Explore neighbors
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_x, next_y = x + dx, y + dy
            
            # Check if neighbor is valid, matches the pattern, and not in the current path
            if (0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and
                grid[next_x][next_y] == pattern[offset] and
                (next_x, next_y) not in current_path):
                
                # Recurse: Add the new cell and continue the search
                current_path.append((next_x, next_y))
                backtrack_enumerate(next_x, next_y, offset + 1, current_path)
                
                # Backtrack: Remove the cell to explore other branches
                current_path.pop()

    # Main Loop: Find all possible starting points
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == pattern[0]:
                # Launch the search for each starting point
                backtrack_enumerate(i, j, 1, [(i, j)])
                
    return all_valid_paths

