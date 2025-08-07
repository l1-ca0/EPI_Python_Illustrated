def find_key_interval(A, k):
    """
    Finds the start and end index of a key k in a sorted array A.

    Args:
        A (list[int]): A sorted list of integers.
        k (int): The key to search for.

    Returns:
        list[int]: A list [L, U] where L is the first index of k and
                   U is the last. Returns [-1, -1] if k is not found.
    """

    def find_first(A, k):
        """Helper to find the first occurrence of k."""
        left, right = 0, len(A) - 1
        first_pos = -1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == k:
                first_pos = mid
                right = mid - 1  # Keep searching left
            elif A[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return first_pos

    def find_last(A, k):
        """Helper to find the last occurrence of k."""
        left, right = 0, len(A) - 1
        last_pos = -1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == k:
                last_pos = mid
                left = mid + 1  # Keep searching right
            elif A[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return last_pos

    first = find_first(A, k)
    if first == -1:
        # If the key doesn't exist at all, we're done.
        return [-1, -1]
    
    last = find_last(A, k)
    return [first, last]

# Example:
# A = [1, 2, 2, 4, 4, 4, 7, 11, 11, 13], k = 4
# find_interval(A, 4) will return [3, 5].
#
# If k = 5, it will return [-1, -1].