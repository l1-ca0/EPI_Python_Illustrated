def search_entry_equal_to_index(A):
    """
    In a sorted array `A` of distinct integers, finds an index i where A[i] == i.
    """
    left, right = 0, len(A) - 1

    while left <= right:
        mid = left + (right - left) // 2
        difference = A[mid] - mid

        if difference == 0:
            # Success A[mid] == mid.
            return mid
        elif difference > 0:  # A[mid] > mid
            # The target must be in the left half.
            right = mid - 1
        else:  # A[mid] < mid
            # The target must be in the right half.
            left = mid + 1
    
    # No such entry was found.
    return -1

