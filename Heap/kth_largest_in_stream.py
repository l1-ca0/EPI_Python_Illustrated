def print_kth_largest_in_stream(stream: Iterator[int], k: int):
    """
    For each element in a stream (starting from the k-th), prints the
    k-th largest element seen up to that point.
    """
    min_heap = []
    
    for i, x in enumerate(stream):
        # For the first k-1 elements, just build the heap.
        if i < k - 1:
            heapq.heappush(min_heap, x)
        # At the k-th element, the heap is full. The top is the k-th largest.
        elif i == k - 1:
            heapq.heappush(min_heap, x)
            print(f"After {i+1} elements, k-th largest is: {min_heap[0]}")
        # For all subsequent elements...
        else:
            # If the new element is larger than the smallest element in our heap
            # (the current k-th largest), then it belongs in the top k.
            if x > min_heap[0]:
                heapq.heappushpop(min_heap, x)
            
            # The top of the heap is the new k-th largest element.
            print(f"After {i+1} elements, k-th largest is: {min_heap[0]}")

