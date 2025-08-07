def search_smallest(A):
    """
    Finds the index of the minimum element in a sorted array
    of distinct elements using binary search.

    Args:
        A (list[int]): A cyclically sorted list of distinct integers.

    Returns:
        int: The index of the smallest element in the array.
    """
    left, right = 0, len(A) - 1

    # The loop continues as long as our search space has more than one element.
    # It will terminate when left == right, pinpointing the minimum element.
    while left < right:
        mid = left + (right - left) // 2

        # We compare the middle element to the rightmost element to identify
        # which part of the array contains the "inflection point" or minimum.
        if A[mid] > A[right]:
            # If A[mid] is greater than A[right], it means the subarray from
            # mid to right is not sorted in ascending order.
            left = mid + 1
        else:  # A[mid] <= A[right]
            # If A[mid] is less than or equal to A[right], the subarray from
            # mid to right IS sorted.
            # Example: [5, 1, 2, 3, 4]. If mid points to 2, 2 <= 4.
            # This means the minimum is either A[mid] itself or to its left.
            # We set right = mid because mid is a potential candidate.
            right = mid
            
    # When the loop ends, left and right converge on the index of the minimum element.
    return left