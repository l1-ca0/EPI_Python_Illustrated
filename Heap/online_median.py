import heapq
from typing import List, Iterator

def online_median(sequence: Iterator[int]) -> List[float]:
    """
    Computes the running median of a stream of numbers.

    Args:
        sequence: An iterator that yields numbers.

    Returns:
        A list of the medians calculated after each number is read.
    """
    # min_heap stores the larger half of the numbers.
    min_heap = []
    # max_heap stores the smaller half of the numbers. We use negation
    # to simulate a max-heap with Python's min-heap implementation.
    max_heap = []
    result = []

    for x in sequence:
        # --- The Rebalancing Act ---
        # 1. Add the new number to the max_heap (smaller half).
        # We push its negation to maintain the max-heap property.
        heapq.heappush(max_heap, -x)
        
        # 2. Move the largest element from max_heap to min_heap.
        # This ensures every element in max_heap is <= every element in min_heap.
        largest_in_small_half = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, largest_in_small_half)

        # 3. Enforce the size invariant. If min_heap is now larger,
        # move its smallest element back to the max_heap.
        if len(min_heap) > len(max_heap):
            smallest_in_large_half = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -smallest_in_large_half)

        # --- Calculate the Median ---
        # If the total number of elements is even, the heaps are the same size.
        # The median is the average of the two middle elements.
        if len(min_heap) == len(max_heap):
            # max_heap's top is -median_part1, min_heap's top is median_part2
            median = (min_heap[0] - max_heap[0]) / 2.0
        # If the total number of elements is odd, max_heap has the extra element,
        # which is the median.
        else: # len(max_heap) == len(min_heap) + 1
            median = -max_heap[0]
            
        result.append(median)
        
    return result