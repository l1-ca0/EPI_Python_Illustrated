def search_in_cyclically_sorted_array(A, k):
    """
    Searches for a key k in a cyclically sorted array of distinct elements.
    Returns the index of k if found, otherwise -1.
    """
    left, right = 0, len(A) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if A[mid] == k:
            return mid

        # Determine which half is normally sorted
        if A[left] <= A[mid]:
            # The left half [left...mid] is sorted.
            # Check if k falls within this sorted range.
            if A[left] <= k and k < A[mid]:
                right = mid - 1
            else:
                # k must be in the other (unsorted) half.
                left = mid + 1
        else:
            # The right half [mid...right] must be sorted.
            # Check if k falls within this sorted range.
            if A[mid] < k and k <= A[right]:
                left = mid + 1
            else:
                # k must be in the other (unsorted) half.
                right = mid - 1

    return -1 # Key not found

# Example: A = [378, 478, 550, 631, 103, 203, 220], k = 103
# search_in_cyclically_sorted_array(A, k) -> Returns 4