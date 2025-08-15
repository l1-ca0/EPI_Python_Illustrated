
#dp[i][w] = max(dp[i-1][w], value_i + dp[i][w - weight_i])
#The only difference from the 0/1 knapsack formula is that the second term looks at dp[i] (the current row) instead of dp[i-1] (the previous row), which is what allows an item to be used multiple times.
def unbounded_knapsack(items, capacity):
    """
    Solves the unbounded knapsack problem using dynamic programming
    
    Args:
        items: A list of tuples, where each tuple is (value, weight)
        capacity: The maximum weight the knapsack can hold
    
    Returns:
        The maximum value that can be achieved
    """
    num_items = len(items)
    # dp[i][w] stores the max value using the first `i` items with capacity `w`
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]

    # Iterate through each item
    for i in range(1, num_items + 1):
        value, weight = items[i-1] 
        
        # Iterate through each possible capacity
        for w in range(1, capacity + 1):
            # Option 1: Don't take the current item `i`
            # The value is the same as the solution with `i-1` items
            dp[i][w] = dp[i-1][w]
            
            # Option 2: Take the current item `i`, if it fits
            if weight <= w:
                # The value is the item's value plus the best solution for
                # the remaining capacity, still able to use item `i`
                value_with_item = value + dp[i][w - weight]
                
                # Choose the option that yields the maximum value
                dp[i][w] = max(dp[i][w], value_with_item)

    # The bottom-right cell contains the final answer
    return dp[num_items][capacity]

def unbounded_knapsack_optimized(items, capacity):
    """
    Solves the unbounded knapsack problem using O(W) space
    """
    # dp[w] stores the max value for a knapsack of capacity `w`
    dp = [0] * (capacity + 1)
    
    # Iterate through each type of item
    for value, weight in items:
        # Iterate forwards from the item's weight up to the capacity
        for w in range(weight, capacity + 1):
            # The key is the forward loop
            # When we calculate dp[w], we use dp[w - weight], which may
            # have already been updated in this same pass
            # This correctly simulates taking another copy of the current item
            dp[w] = max(dp[w], value + dp[w - weight])
            
    return dp[capacity]

