import collections
from typing import List, NamedTuple

# A namedtuple hold a min and max value.
MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))

def find_min_max(A: List[int]) -> MinMax:
    """
    Finds the minimum and maximum elements in an array using an efficient
    number of comparisons (approx. 1.5n).

    Args:
        A: A list of comparable numbers.

    Returns:
        A MinMax namedtuple containing the smallest and largest elements.
    """
    # If the list is empty or has one element, the min and max are the same.
    if len(A) <= 1:
        return MinMax(A[0], A[0]) if A else None

    # --- Step 1: Initialize global_min_max ---
    # Compare the first two elements to establish initial min and max.
    # This costs 1 comparison.
    global_min_max = MinMax(min(A[0], A[1]), max(A[0], A[1]))
    
    # --- Step 2: Process the rest of the array in pairs ---
    # We iterate with a step of 2 to grab pairs of elements.
    for i in range(2, len(A) - 1, 2):
        
        # 1. Find the local min and max of the pair (1 comparison).
        local_min_max = MinMax(min(A[i], A[i+1]), max(A[i], A[i+1]))
        
        # 2. Update the global min and max using the local min and max.
        # This requires 2 more comparisons. Total of 3 for the pair.
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest))

    # --- Step 3: Handle the final element if the array has an odd length ---
    if len(A) % 2:
        last_element = A[-1]
        global_min_max = MinMax(
            min(global_min_max.smallest, last_element),
            max(global_min_max.largest, last_element))

    return global_min_max