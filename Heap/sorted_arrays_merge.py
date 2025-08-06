import heapq
from typing import List

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    """
    Merges k sorted arrays into a single sorted array using a min-heap.
    """
    min_heap = []
    result = []

    # Create an iterator for each input array. Iterators are memory-efficient
    # as they don't require loading all data at once.
    sorted_arrays_iters = [iter(arr) for arr in sorted_arrays]

    # --- Step 1: Initialize the heap ---
    # Push the first element from each array's iterator onto the heap.
    for i, it in enumerate(sorted_arrays_iters):
        # Get the first element from the iterator.
        first_element = next(it, None) # 'None' is a default if the iterator is empty.
        
        if first_element is not None:
            # Push a tuple of (value, original_array_index) onto the heap.
            # The heap will be ordered by 'value'.
            heapq.heappush(min_heap, (first_element, i))

    # --- Step 2: Main merging loop ---
    # Continue as long as there are elements in the heap to process.
    while min_heap:
        # Pop the smallest element. This is the next element for our sorted list.
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        
        # Add the value to our result.
        result.append(smallest_entry)
        
        # Get the iterator for the array where the smallest element came from.
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        
        # Get the *next* element from that same iterator to replenish the heap.
        next_element = next(smallest_array_iter, None)
        
        # If that array is not yet exhausted, push its next element onto the heap.
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result



def merge_sorted_arrays_pythonic(sorted_arrays: List[List[int]]) -> List[int]:
    """
    Merges k sorted arrays using the built-in heapq.merge function.
    """
    # The '*' (unpack operator) passes each array in sorted_arrays as a separate argument to heapq.merge.
    # heapq.merge returns an iterator, so we wrap it in list() to get the result.
    return list(heapq.merge(*sorted_arrays))