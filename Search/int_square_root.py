def integer_square_root(k: int) -> int:
    """
    Computes the largest integer whose square is less than or equal to k.

    Args:
        k: A non-negative integer.

    Returns:
        The largest integer x such that x*x <= k.
    """
    if k < 0:
        raise ValueError("Cannot compute square root of a negative number")

    low, high = 0, k
    # 'result' will store the largest valid candidate found so far.
    result = 0 

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            # This 'mid' is a valid answer. We store it as our best-so-far.
            result = mid
            
            # Now, we try to find an even larger valid answer by searching
            # in the upper half of the range.
            low = mid + 1
        else: # mid_squared > k
            # 'mid' is too large. The answer must be in the lower half.
            high = mid - 1
            
    # After the loop, 'result' holds the last (and largest) 'mid'
    # that satisfied the condition.
    return result