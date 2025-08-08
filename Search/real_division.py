def real_divide(x: float, y: float, tolerance: float = 1e-9) -> float:
    """
    Computes x / y without using the division operator,
    to within a specified tolerance.

    Args:
        x: The dividend (positive float).
        y: The divisor (positive float).
        tolerance: The desired precision of the result.

    Returns:
        The result of x / y.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")

    # --- Step 1: Establish the search range [low, high] ---
    low = 0.0
    high = 0.0

    if y >= 1.0:
        # If y >= 1, the result is at most x.
        high = x
    else: # y < 1.0
        # If y < 1, the result is > x. Find an upper bound.
        high = 1.0
        while high * y < x:
            high *= 2.0
    
    # --- Step 2: Perform binary search ---
    # Continue until the search range is smaller than the tolerance.
    while (high - low) > tolerance:
        mid = low + (high - low) * 0.5
        guess = mid * y
        
        if guess > x:
            # The guess 'mid' is too high.
            high = mid
        else:
            # The guess 'mid' is too low or just right.
            low = mid
            
    # low and high are now extremely close to the true answer.
    return low