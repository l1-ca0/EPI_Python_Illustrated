def search_first_of_k(A, k):
    """
    Searches for the first occurrence of a key `k` in a sorted array `A`.

    Args:
        A (list[int]): A sorted list of integers.
        k (int): The key to search for.

    Returns:
        int: The index of the first occurrence of k, or -1 if not found.
    """
    # Initialize the search space to the entire array.
    left, right = 0, len(A) - 1
    # `result` stores the most recent (leftmost) index where `k` was found.
    result = -1

    # Standard binary search loop.
    while left <= right:
        # Use this formula for mid to prevent potential integer overflow.
        mid = left + (right - left) // 2

        if A[mid] > k:
            # The element at mid is too large, so the target must be to the left.
            right = mid - 1
        elif A[mid] == k:
            # Found an occurrence of k
            # Record this index as our current best answer.
            result = mid
            # Now, we must check if an earlier occurrence exists.
            # We continue the search in the left subarray.
            right = mid - 1
        else:  # A[mid] < k
            # The element at mid is too small, so the target must be to the right.
            left = mid + 1
    
    return result