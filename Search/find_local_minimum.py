def find_local_minimum(A):
    """
    Finds an index of a local minimum in an array A.
    A local minimum A[i] is defined as A[i-1] >= A[i] <= A[i+1].
    Assumes A[0] >= A[1] and A[n-2] <= A[n-1].

    Args:
        A (list[int]): The input array.

    Returns:
        int: An index corresponding to a local minimum.
    """
    left, right = 0, len(A) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if A[mid] is a local minimum by comparing to its neighbors
        # Use infinity for boundary conditions to simplify logic
        left_neighbor = A[mid - 1] if mid > 0 else float('inf')
        right_neighbor = A[mid + 1] if mid < len(A) - 1 else float('inf')

        if A[mid] <= left_neighbor and A[mid] <= right_neighbor:
            # Found it! A[mid] is a valley.
            return mid
        elif left_neighbor < A[mid]:
            # There's a downward slope to the left, so a minimum must be there.
            right = mid - 1
        else:  # right_neighbor < A[mid]
            # There's a downward slope to the right.
            left = mid + 1
            
    return -1 # Should not be reached given the problem's constraints

