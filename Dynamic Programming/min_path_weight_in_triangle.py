def min_path_in_triangle(triangle):
    """
    Finds the minimum path sum using a 2D DP table
    """
    if not triangle:
        return 0

    num_rows = len(triangle)
    # min_sums[i][j] will store the minimum path sum to that cell
    min_sums = [row[:] for row in triangle]

    for i in range(1, num_rows):
        for j in range(len(triangle[i])):
            # If a parent is out of bounds, its path sum is treated as infinity
            parent_left = min_sums[i-1][j-1] if j > 0 else float('inf')
            parent_right = min_sums[i-1][j] if j < i else float('inf')
            
            # The min path to this cell is its value plus the min of its parent paths
            min_sums[i][j] += min(parent_left, parent_right)

    return min(min_sums[-1])

# Example
'''
triangle = [
    [2],
    [4, 4],
    [8, 5, 6],
    [4, 2, 6, 3]
]
'''

def min_path_in_triangle_optimized(triangle):
    """
    Finds the minimum path sum by modifying the triangle in-place
    This uses O(1) extra space
    """
    if not triangle:
        return 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # If a parent is out of bounds, its path sum is treated as infinity
            parent_left = triangle[i-1][j-1] if j > 0 else float('inf')
            parent_right = triangle[i-1][j] if j < i else float('inf')
            
            # Update the cell with the minimum path sum required to reach it
            triangle[i][j] += min(parent_left, parent_right)

    return min(triangle[-1])
