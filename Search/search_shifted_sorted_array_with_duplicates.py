def search_smallest_with_duplicates(A):
    """
    Finds the index of the minimum element in a cyclically sorted array
    that may contain duplicates.
    """
    left, right = 0, len(A) - 1

    while left < right:
        mid = left + (right - left) // 2

        if A[mid] > A[right]:
            # The minimum must be to the right of mid.
            left = mid + 1
        elif A[mid] < A[right]:
            # The minimum is at mid or to its left.
            right = mid
        else:  # A[mid] == A[right]
            # We can't decide, so we safely shrink the search space.
            right -= 1
            
    return left

# Example: A = [2, 2, 2, 0, 2] -> Returns 3 (index of 0)