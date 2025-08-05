import collections
from typing import Deque

class QueueWithMax:
    """
    A queue that supports adding to the back, removing from the front,
    and finding the maximum element, all in O(1) amortized time.
    """

    def __init__(self):
        """Initializes the queue."""
        # The main queue to store all elements.
        self._element_queue: Deque[int] = collections.deque()
        
        # A helper deque to efficiently track the maximum element.
        # This deque is always kept in monotonically decreasing order.
        self._max_candidates_deque: Deque[int] = collections.deque()

    def enqueue(self, item: int) -> None:
        """Adds an item to the back of the queue."""
        # 1. Add the item to the main queue.
        self._element_queue.append(item)
        
        # 2. Maintain the max candidates deque.
        #    Before adding the new item, remove any elements from the *back* of
        #    the candidates deque that are smaller than the new item.
        while self._max_candidates_deque and self._max_candidates_deque[-1] < item:
            self._max_candidates_deque.pop()
        
        # 3. Add the new item to the back of the candidates deque.
        self._max_candidates_deque.append(item)

    def dequeue(self) -> int:
        """Removes and returns the item from the front of the queue."""
        if not self._element_queue:
            raise IndexError("dequeue from an empty queue")

        # 1. Remove the item from the front of the main queue.
        item_to_return = self._element_queue.popleft()
        
        # 2. Update the max candidates deque if necessary.
        #    If the element being dequeued is the current maximum, it must
        #    also be removed from the front of the candidates deque.
        if item_to_return == self._max_candidates_deque[0]:
            self._max_candidates_deque.popleft()
            
        return item_to_return

    def max(self) -> int:
        """
        Returns the maximum element currently in the queue in O(1) time.
        """
        if not self._max_candidates_deque:
            raise IndexError("max() on an empty queue")
            
        # The maximum element is always at the front of the candidates deque.
        return self._max_candidates_deque[0]

    def size(self) -> int:
        """Returns the number of elements in the queue."""
        return len(self._element_queue)