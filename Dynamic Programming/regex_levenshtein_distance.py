def regex_levenshtein_distance(A, r):
    """
    Computes Levenshtein distance between a string A and a regex r.
    NOTE: This is a complex variant. This implementation handles '.', normal chars, and '*'.
    """
    a, b = len(A), len(r)
    dp = [[float('inf')] * (b + 1) for _ in range(a + 1)]

    # Base case: empty string vs empty regex is 0 distance
    dp[0][0] = 0
    
    # Initialize first row (empty string vs regex prefixes)
    for j in range(1, b + 1):
        if r[j-1] == '*':
            # A '*' can match zero times, so it can have the same cost as r[:j-2]
            dp[0][j] = dp[0][j-2]
        else:
            # A non-'*' char costs 1 edit (deletion from pattern)
            dp[0][j] = dp[0][j-1] + 1
            
    # Initialize first column (string prefixes vs empty regex)
    for i in range(1, a + 1):
        dp[i][0] = i # Cost is i deletions from A

    # Fill the DP table
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            char_A = A[i-1]
            char_r = r[j-1]

            if char_r != '*':
                # Standard Levenshtein logic for normal chars and '.'
                match_cost = 0 if char_r == '.' or char_A == char_r else 1
                dp[i][j] = min(dp[i-1][j-1] + match_cost, # Substitute
                               dp[i-1][j] + 1,             # Delete from A
                               dp[i][j-1] + 1)             # Insert into A
            else: # char_r is '*'
                # Case 1: The '*' and its preceding char match zero characters.
                # Cost is the same as skipping them in the regex pattern.
                zero_match_cost = dp[i][j-2]
                
                # Case 2: The '*' matches one or more characters.
                # This is only possible if the current char in A matches the char before '*'
                one_or_more_cost = float('inf')
                prev_char_r = r[j-2]
                if prev_char_r == '.' or prev_char_r == char_A:
                    # We match A's char, so we look at the cost from the previous A char
                    # against the SAME regex pattern (since '*' can be reused).
                    # This corresponds to a "match" (cost 0) on top of the previous state.
                    one_or_more_cost = dp[i-1][j]

                dp[i][j] = min(zero_match_cost, one_or_more_cost)

    return dp[-1][-1]
