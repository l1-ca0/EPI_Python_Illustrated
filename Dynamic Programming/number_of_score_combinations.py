from functools import lru_cache

def count_score_combinations_recursive(final_score, play_scores):
    """
    Calculates score combinations using top-down recursion with memoization
    """
    
    # Sort the plays to potentially improve cache performance, though not required
    # It ensures that subproblems are always approached with plays in the same order
    plays = tuple(sorted(play_scores))

    @lru_cache(maxsize=None) # Automatically caches the results of the function calls
    def solve(current_score, play_index):
        # Base Case 1: A score of 0 has been successfully reached
        if current_score == 0:
            return 1 # This represents one valid combination

        # Base Case 2: The score is negative or we've run out of plays to use
        if current_score < 0 or play_index >= len(plays):
            return 0 

        # Recursive Step 1: Use the play at `play_index`
        # We stay at the same play_index to allow for using this play multiple times
        use_current_play = solve(current_score - plays[play_index], play_index)

        # Recursive Step 2: Skip the play at `play_index` and move to the next
        skip_current_play = solve(current_score, play_index + 1)
        
        # The total is the sum of both choices
        return use_current_play + skip_current_play

    return solve(final_score, 0)


def count_score_combinations(final_score, play_scores):
    """
    Calculates the number of ways to reach a final score using given play scores
    This version uses O(S * n) space complexity
    """
    
    # Create a 2D DP table: num_plays x (final_score + 1)
    # dp[i][j] will store the number of ways to make score j using the first i plays
    num_plays = len(play_scores)
    dp = [[0] * (final_score + 1) for _ in range(num_plays)]
    
    # Iterate through each type of play
    for i in range(num_plays):
        # The current play's point value
        current_play = play_scores[i]
        
        # Base case: there is one way to make a score of 0 (by choosing no plays)
        dp[i][0] = 1
        
        # Iterate through each possible score from 1 to final_score
        for j in range(1, final_score + 1):
            
            # Combinations WITHOUT using the current_play
            # This is the result from the previous row (using the previous set of plays)
            # If i is 0, there is no previous row, so this is 0
            without_this_play = dp[i-1][j] if i > 0 else 0
            
            # Combinations WITH at least one of the current_play
            # This requires finding combinations for the remaining score (j - current_play)
            with_this_play = 0
            if j >= current_play:
                # We can only use this play if the score is high enough
                # The value comes from the same row because we can use the current_play multiple times
                with_this_play = dp[i][j - current_play]

            # The total is the sum of the two possibilities
            dp[i][j] = without_this_play + with_this_play
            
    return dp[-1][-1]


def count_score_combinations_optimized(final_score, play_scores):
    """
    Calculates the number of ways to reach a final score using given play scores
    This version uses O(S) space complexity
    """
    
    # Create a 1D DP array of size final_score + 1
    # dp[j] will store the number of ways to make score j
    dp = [0] * (final_score + 1)
    
    # Base case: there's one way to make a score of 0 (by choosing no plays)
    dp[0] = 1
    
    # Iterate through each type of play
    for play in play_scores:
        # For each play, update the dp table for all scores it can contribute to
        # We start j from `play` because scores less than `play` cannot be formed by it
        for j in range(play, final_score + 1):
            # The number of ways to make score j is updated by adding the
            # number of ways we could make the score (j - play)
            # This works because dp[j - play] already contains the combinations
            # to reach that smaller score, and we are now just adding one more `play`
            # to each of those combinations
            dp[j] += dp[j - play]
            
    return dp[final_score]


