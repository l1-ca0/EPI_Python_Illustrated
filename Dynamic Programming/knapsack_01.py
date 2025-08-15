def knapsack_01(items, capacity):
    """
    Solves the 0/1 knapsack problem using bottom-up dynamic programming
    
    Args:
        items: A list of tuples, where each tuple is (value, weight)
        capacity: The maximum weight the knapsack can hold
    
    Returns:
        The maximum value that can be achieved
    """
    # dp[i][w] will store the max value using the first `i` items with capacity `w`
    # We add +1 to dimensions for the base cases (0 items or 0 capacity)
    num_items = len(items)
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]

    # Iterate through each item
    for i in range(1, num_items + 1):
        # Get the value and weight of the current item
        # i-1 because items are 0-indexed
        value, weight = items[i-1]
        
        # Iterate through each possible knapsack capacity
        for w in range(1, capacity + 1):
            # Option 1: Don't take the current item (`i`)
            # The value is the same as the solution with `i-1` items
            dp[i][w] = dp[i-1][w]
            
            # Option 2: Take the current item (`i`), if it fits
            if weight <= w:
                # The value is the current item's value plus the best value
                # for the remaining capacity (w - weight) using previous items
                value_if_taken = value + dp[i-1][w - weight]
                
                # Choose the option that yields the maximum value
                dp[i][w] = max(dp[i][w], value_if_taken)

    
    return dp[-1][-1]


def knapsack_01_optimized(items, capacity):
    """Solves the 0/1 knapsack problem using O(W) space"""
    # dp[w] stores the max value for a knapsack of capacity `w`
    dp = [0] * (capacity + 1)
    
    for value, weight in items:
        # Iterate backwards to use results from the *previous* item calculations
        # If we went forwards, we'd be using the current item multiple times
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], value + dp[w - weight])
            
    return dp[capacity]

