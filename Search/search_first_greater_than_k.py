def search_first_greater_than_k(A, k):
    """
    Finds the index of the first element in a sorted array `A` that is greater than k.
    """
    left, right = 0, len(A) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] > k:
            # This is a potential answer. Store it and look for an even earlier one in the left half.
            result = mid
            right = mid - 1
        else:  # A[mid] <= k
            # This element is not greater than k, so we must search to the right.
            left = mid + 1
    return result

