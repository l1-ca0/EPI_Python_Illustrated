def solve_sudoku(board):
    """
    Solves a Sudoku puzzle in-place using backtracking
    An empty cell is represented by the number 0
    """

    # --- Step 1: Find the next empty cell ---
    # If there are no empty cells, the puzzle is solved (this is our base case)
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # --- Step 2: Try numbers 1-9 in the empty cell ---
    for num in range(1, 10):
        # --- Step 3: Check if the current number is a valid placement ---
        if is_valid(board, num, (row, col)):
            # --- Step 4 (Choose): If it's valid, place the number on the board ---
            board[row][col] = num

            # --- Step 4 (Explore): Recursively call the solver to handle the rest of the board ---
            if solve_sudoku(board):
                return True # If the recursion finds a solution, we're done

            # --- Step 5 (Backtrack): If the recursion failed, undo the choice ---
            # This happens if the number we placed led to a dead end
            board[row][col] = 0

    # If the loop finishes without finding a valid number, trigger a backtrack
    return False


def find_empty(board):
    """A helper function to find the coordinates of the next empty cell (0)"""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c) # Returns a (row, col) tuple
    return None


def is_valid(board, num, pos):
    """A helper function to check if a number is valid in a given position"""
    row, col = pos

    # Check the row
    for c in range(9):
        if board[row][c] == num and col != c:
            return False

    # Check the column
    for r in range(9):
        if board[r][col] == num and row != r:
            return False

    # Check the 3x3 box
    box_start_row = row - row % 3
    box_start_col = col - col % 3
    for r in range(box_start_row, box_start_row + 3):
        for c in range(box_start_col, box_start_col + 3):
            if board[r][c] == num and (r, c) != pos:
                return False

    return True
