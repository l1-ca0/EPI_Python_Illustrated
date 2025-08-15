def longest_common_subsequence(A, B):
    """
    Computes the length of the longest common subsequence (LCS).
    """
    a, b = len(A), len(B)
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    
    for i in range(a):
        for j in range(b):
            # If characters match, they are part of the LCS
            # Add 1 to the LCS of the prefixes
            if A[i] == B[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            # If they don't match, the LCS is the best of the two possibilities:
            # - LCS of A's prefix and B
            # - LCS of A and B's prefix
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                
    return dp[-1][-1]

def longest_common_subsequence_optimized(A, B):
    """
    Computes the length of the LCS using O(min(len(A), len(B))) space
    """
    # Ensure A is the shorter string to minimize space usage
    if len(A) > len(B):
        A, B = B, A
        
    # `dp` array stores the results for the previous row
    dp = [0] * (len(A) + 1)
    
    # Iterate through the rows (characters of the longer string B)
    for i in range(1, len(B) + 1):
        # `prev_diagonal` holds the value of dp[i-1][j-1]
        prev_diagonal = 0 
        
        # Iterate through the columns (characters of the shorter string A)
        for j in range(1, len(A) + 1):
            # `temp` stores the value from the row above (dp[i-1][j])
            # before we overwrite dp[j]
            temp = dp[j]
            
            # If characters match
            if A[j-1] == B[i-1]:
                # The new LCS length is 1 + the diagonal's value
                dp[j] = 1 + prev_diagonal
            else:
                # Otherwise, it's the max of the value from the left
                # (dp[j-1], which was just updated) and the value from above (temp)
                dp[j] = max(dp[j-1], temp)
                
            # The current `temp` value becomes the next iteration's diagonal
            prev_diagonal = temp
            
    # The final answer is the last element in the dp array
    return dp[-1]

