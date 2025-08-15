def min_palindrome_partitions(s):
    """
    Computes the minimum number of palindromic partitions for a string s
    """
    n = len(s)
    # is_palindrome[i][j] will be True if s[i..j] is a palindrome
    is_palindrome = [[False] * n for _ in range(n)]

    # --- Phase 1: Pre-compute all palindromic substrings ---
    # Initialize is_palindrome table (assuming it's a 2D boolean array of size n x n)
    # n is the length of the string s

    # Handle substrings of length 1
    for i in range(n):
        is_palindrome[i][i] = True

    # Handle substrings of length 2
    for i in range(n - 1):  # To avoid out-of-bounds for i+1
        is_palindrome[i][i+1] = (s[i] == s[i+1])

    # Check for substrings of length 3 and greater
    for length in range(3, n + 1):  # Start from length 3
        for i in range(n - length + 1):
            j = i + length - 1
            # For lengths >= 3, check outer characters and inner substring
            is_palindrome[i][j] = (s[i] == s[j] and is_palindrome[i+1][j-1])


    # --- Phase 2: Calculate minimum partitions ---
    # dp[i] = min number of partitions for prefix s[:i]
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # The worst case is cutting into `i` individual characters
        min_val = i 
        # Check every possible last cut `j`
        for j in range(i):
            # If the last substring s[j:i] is a palindrome
            if is_palindrome[j][i-1]:
                # We have a candidate solution: 1 + partitions for s[:j]
                min_val = min(min_val, 1 + dp[j])
        dp[i] = min_val

    # The result for the whole string is dp[n], but the number of
    # cuts is one less than the number of partitions
    return dp[n]

# Example from the book
# s = "0204451881"
# The minimum decomposition is ["020", "44", "5", "1881"], which has 4 partitions
