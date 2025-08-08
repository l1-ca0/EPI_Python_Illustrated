import math

def real_square_root(x: float) -> float:
    """
    Computes the square root of a non-negative floating-point number.

    Args:
        x: A non-negative floating-point number.

    Returns:
        The square root of x with high precision.
    """
    if x < 0.0:
        raise ValueError("Cannot compute square root of a negative number")

    # --- Step 1: Set the initial search range ---
    # If x < 1.0, its root is between x and 1.0.
    # If x >= 1.0, its root is between 1.0 and x.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    # --- Step 2: Binary search until the range is sufficiently small ---
    # We continue until 'left' and 'right' are almost equal.
    # math.isclose() is a safe way to compare floating-point numbers.
    while not math.isclose(left, right):
        mid = left + 0.5 * (right - left)  # Avoids potential overflow vs. (left+right)/2
        mid_squared = mid * mid
        
        if mid_squared > x:
            # mid is too large. The root must be in the lower half [left, mid].
            right = mid
        else: # mid_squared <= x
            # mid is a candidate. The root might be mid or larger, so search in [mid, right].
            left = mid
    
    # When the loop terminates, 'left' is a very close approximation of the root.
    return left