def levenshtein_distance(A, B):
    """
    Computes the Levenshtein distance between two strings A and B.
    This version uses O(ab) time and O(ab) space.
    """
    # Create the DP table (a is rows, b is columns)
    # The dimensions are len+1 to accommodate the empty string prefixes
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    # Initialize the base cases
    # The first row: cost of converting an empty string to B's prefixes
    for j in range(len(B) + 1):
        dp[0][j] = j
    # The first column: cost of converting A's prefixes to an empty string
    for i in range(len(A) + 1):
        dp[i][0] = i

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            # If the characters at this position match
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Characters differ, so we take the minimum of the 3 possible edits
                substitute_cost = dp[i-1][j-1]
                delete_cost = dp[i-1][j]  
                insert_cost = dp[i][j-1]  
                
                # The cost is 1 (for the edit) + the minimum of the previous states
                dp[i][j] = 1 + min(substitute_cost, delete_cost, insert_cost)
                

    return dp[-1][-1]

def levenshtein_distance_optimized(A, B):
    """
    Computes the Levenshtein distance between strings A and B
    using O(min(len(A), len(B))) space
    """
    # Ensure s1 is the shorter string to minimize space usage
    if len(A) > len(B):
        A, B = B, A
        
    # `prev_row` stores the costs for the previous row of the DP table
    # It's initialized for the base case of an empty string
    prev_row = list(range(len(A) + 1))
    
    # Loop through each character of the longer string B
    for j in range(1, len(B) + 1):
        # `curr_row` will store the costs for the current row being calculated
        # Initialize the first element with the base case (j deletions)
        curr_row = [j] * (len(A) + 1)
        
        # Loop through each character of the shorter string A
        for i in range(1, len(A) + 1):
            # If the characters match, no new cost is added
            # The cost is the same as the diagonal element from the previous row
            if A[i-1] == B[j-1]:
                curr_row[i] = prev_row[i-1]
            else:
                # If they don't match, we add 1 to the minimum of the three
                # possible operations: substitution, deletion, or insertion
                substitute_cost = prev_row[i-1]
                delete_cost = prev_row[i]
                insert_cost = curr_row[i-1]
                curr_row[i] = 1 + min(substitute_cost, delete_cost, insert_cost)
        
        # The current row now becomes the previous row for the next iteration
        prev_row = curr_row
        
    # The final answer is the last element of the last computed row
    return prev_row[-1]

