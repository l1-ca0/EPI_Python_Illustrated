import heapq

def merge_sorted_arrays(sorted_arrays: list) -> list:
    return list(heapq.merge(*sorted_arrays))

def sort_k_increasing_decreasing_array(A: list) -> list:
    """
    Sorts an array that consists of alternating increasing and decreasing sections.
    """
    # Edge case for a very short array.
    if len(A) <= 1:
        return A
        
    sorted_subarrays = []
    # Define states to keep track of the current trend.
    INCREASING, DECREASING = 0, 1
    # The first subarray is assumed to be increasing.
    subtype = INCREASING
    start_idx = 0

    # Iterate through the array to find turning points.
    for i in range(1, len(A) + 1):
        # A turning point is found if we are at the end of the array OR
        # the trend changes from increasing to decreasing OR
        # the trend changes from decreasing to increasing.
        if (i == len(A) or \
           (A[i - 1] < A[i] and subtype == DECREASING) or \
           (A[i - 1] > A[i] and subtype == INCREASING)):

            # Slice the completed subarray from the main array.
            subarray = A[start_idx:i]
            
            # If the subarray was decreasing, reverse it to make it increasing.
            if subtype == DECREASING:
                sorted_subarrays.append(subarray[::-1])
            else:
                sorted_subarrays.append(subarray)

            # Start a new subarray and flip the trend type.
            start_idx = i
            subtype = DECREASING if subtype == INCREASING else INCREASING

    # Step 3: Merge all the sorted subarrays into a single sorted list.
    return merge_sorted_arrays(sorted_subarrays)