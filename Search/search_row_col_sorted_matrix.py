from typing import List

def matrix_search(A: List[List[int]], x: int) -> bool:
    """
    Searches for a value 'x' in a 2D array where rows and columns are sorted.

    Args:
        A: A 2D list of integers, sorted row-wise and column-wise.
        x: The integer value to search for.

    Returns:
        True if x is found in the matrix, otherwise False.
    """
    num_rows = len(A)

    # --- Step 1: Start at the top-right corner of the matrix ---
    row, col = 0, len(A[0]) - 1

    # --- Step 2: Loop as long as our pointers are within the matrix bounds ---
    while row < num_rows and col >= 0:
        current_val = A[row][col]
        
        # --- Step 3: Compare the target with the current element ---
        if current_val == x:
            return True
        elif x < current_val:
            # Target is smaller. This means it cannot be in the current column,
            # because all elements below are even larger.
            # -> Eliminate the current column and move left.
            col -= 1
        else: # x > current_val
            # Target is larger. This means it cannot be in the current row,
            # because all elements to the left are even smaller.
            # -> Eliminate the current row and move down.
            row += 1
    
    return False