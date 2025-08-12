from typing import List

def n_queens(n: int) -> List[List[int]]:
    """
    Calculates all nonattacking placements of n queens on an n x n chessboard

    Args:
        n: The size of the chessboard and the number of queens

    Returns:
        A list of lists, where each inner list represents a valid placement
    """

    # This list will store all the valid board configurations found
    result: List[List[int]] = []
    
    # This list tracks the column placement for queens in the current attempt
    # For example, col_placement[i] is the column of the queen in row i
    col_placement: List[int] = []

    def solve_n_queens_helper(row: int):
        """
        A recursive helper function that uses backtracking to place queens row by row
        """
        
        # This is the base case for the recursion
        # If we have reached row 'n', it means we have successfully placed n queens
        if row == n:
            # We found a valid placement, so add a *copy* of it to our results
            # A copy is needed because we will continue to modify col_placement via backtracking
            result.append(list(col_placement))
            return

        # This is the recursive step
        # For the current 'row', try placing a queen in each 'col'
        for col in range(n):
            # Before placing a queen at (row, col), check if it's a valid move
            # We check if this new queen conflicts with any queens placed in previous rows
            # The 'all' function ensures the condition holds true for every previously placed queen
            # 'i' is the previous row, and 'c' is the column of the queen in that row
            if all(
                # Check for diagonal conflicts
                # If the difference in rows (row - i) equals the difference in columns abs(c - col),
                # then the two queens are on the same diagonal
                abs(c - col) != row - i and

                # Check for column conflicts
                # If 'c' and 'col' are the same, the two queens are in the same column
                c != col

                for i, c in enumerate(col_placement)
            ):
                # If the placement is valid, append the column to our current placement
                col_placement.append(col)
                
                # Recurse to place a queen in the next row
                solve_n_queens_helper(row + 1)
                
                # --- BACKTRACK ---
                # After the recursive call returns, we undo the move by removing the last placement
                # This allows us to try placing the queen in the next column of the current row
                col_placement.pop()

    # Start the recursive solving process from the very first row (row 0)
    solve_n_queens_helper(0)
    return result
