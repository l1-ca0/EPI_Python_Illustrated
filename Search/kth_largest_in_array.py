import random
from typing import List

def find_kth_largest(A: List[int], k: int) -> int:
    """
    Finds the k-th largest element in an array using the Quickselect algorithm.

    Args:
        A: A list of numbers.
        k: The desired rank (e.g., k=1 for largest, k=2 for 2nd largest).

    Returns:
        The k-th largest element.
    """
    left, right = 0, len(A) - 1
    # The k-th largest element is at index (n-k) in a zero-indexed, sorted array.
    target_index = len(A) - k

    while left <= right:
        # Choose a random pivot to avoid worst-case O(n^2) behavior.
        pivot_idx = random.randint(left, right)
        
        # Partition the array around the pivot and get its final sorted position.
        new_pivot_idx = partition(A, left, right, pivot_idx)

        if new_pivot_idx == target_index:
            # The pivot is the element we were looking for.
            return A[new_pivot_idx]
        elif new_pivot_idx > target_index:
            # The target is in the left subarray.
            right = new_pivot_idx - 1
        else: # new_pivot_idx < target_index
            # The target is in the right subarray.
            left = new_pivot_idx + 1

    # This line should not be reachable if k is valid (1 <= k <= len(A))
    raise ValueError("k is out of the valid range")

def partition(A: List[int], left: int, right: int, pivot_idx: int) -> int:
    """
    Rearranges the subarray A[left:right+1] around the pivot.
    
    All elements less than the pivot are moved to its left, and all elements
    greater than or equal to it are moved to its right.

    Returns:
        The final index where the pivot element is placed.
    """
    pivot_value = A[pivot_idx]
    # Move pivot to the end to get it out of the way.
    A[pivot_idx], A[right] = A[right], A[pivot_idx]
    
    # store_idx is the boundary of the "smaller than pivot" section.
    store_idx = left
    for i in range(left, right):
        if A[i] < pivot_value:
            # If the current element is smaller, swap it into the smaller section.
            A[store_idx], A[i] = A[i], A[store_idx]
            store_idx += 1
            
    # Move the pivot from the end to its final sorted position.
    A[right], A[store_idx] = A[store_idx], A[right]
    return store_idx