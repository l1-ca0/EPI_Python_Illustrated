import heapq
import itertools
from typing import List, Iterator

def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:
    """
    Sorts a k-sorted sequence (iterator) using a min-heap.

    Args:
        sequence: An iterator of numbers, where each element is at most
                  k positions away from its sorted position.
        k: The maximum distance an element can be from its sorted position.

    Returns:
        A list containing the fully sorted numbers.
    """
    min_heap = []
    result = []

    # --- Step 1: Initialize the heap ---
    # Populate the min-heap with the first k elements from the sequence.
    # This creates our initial "window" of candidates.
    # islice consumes from the iterator, so the next loop won't see these again.
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    # --- Step 2: Main processing loop ---
    # For every remaining element in the input sequence...
    for x in sequence:
        # Push the new element onto the heap and immediately pop the smallest.
        # The popped element is guaranteed to be the next smallest in the
        # overall sorted sequence.
        # This keeps the heap size fixed at k.
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # --- Step 3: Drain the remaining elements from the heap ---
    # After the input sequence is exhausted, the heap contains the k largest
    # elements. We extract them in sorted order by repeatedly popping.
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result