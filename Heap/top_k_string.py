import heapq
import itertools
from typing import List, Iterator

def find_k_longest_strings(k: int, stream: Iterator[str]) -> List[str]:
    """
    Finds the k longest strings from a stream of strings using a min-heap.

    Args:
        k: The number of longest strings to find.
        stream: An iterator or sequence of strings.

    Returns:
        A list containing the k longest strings.
    """
    # 1. Initialize the min-heap with the first k strings.
    # We store tuples of (length, string) so the heap automatically
    # orders elements by length.
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    
    # Turn the list into a valid min-heap in O(k) time.
    heapq.heapify(min_heap)

    # 2. Iterate through the rest of the strings in the stream.
    for next_string in stream:
        # Compare the new string's length with the shortest in our heap.
        # min_heap[0] is always the smallest element.
        if len(next_string) > min_heap[0][0]:
            # This new string is longer than at least one of our candidates.
            # Use heappushpop to efficiently replace the smallest element
            # (the root) with the new element.
            heapq.heappushpop(min_heap, (len(next_string), next_string))
            
    # 3. The heap now contains the k longest strings. Extract just the
    # strings from the (length, string) tuples.
    return [s for length, s in min_heap]