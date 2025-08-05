from typing import List

class QueueWithStacks:
    """
    An implementation of a FIFO (First-In, First-Out) queue using two
    LIFO (Last-In, First-Out) stacks.
    """

    def __init__(self):
        """Initializes the two stacks used to simulate a queue."""
        # This stack is for incoming elements (enqueue operations).
        self._enqueue_stack: List[int] = []
        # This stack is for outgoing elements (dequeue operations).
        self._dequeue_stack: List[int] = []

    def enqueue(self, item: int) -> None:
        """
        Adds an item to the back of the queue. This is an O(1) operation.
        """
        self._enqueue_stack.append(item)

    def dequeue(self) -> int:
        """
        Removes and returns the item from the front of the queue.
        This operation is O(1) on average (amortized).
        """
        # --- Check if the dequeue stack is empty ---
        # If it is, transfer elements from the enqueue stack to reverse their
        # order and get the oldest element on top.
        if not self._dequeue_stack:
            
            # Before transferring, check if there's anything to transfer.
            # If both stacks are empty, the queue is empty.
            if not self._enqueue_stack:
                raise IndexError("dequeue from an empty queue")

            # --- Transfer elements from enqueue to dequeue stack ---
            while self._enqueue_stack:
                self._dequeue_stack.append(self._enqueue_stack.pop())
        
        # Now, the oldest element is guaranteed to be at the top of the
        # dequeue stack. Pop and return it.
        return self._dequeue_stack.pop()

    def size(self) -> int:
        """Returns the total number of items in the queue."""
        return len(self._enqueue_stack) + len(self._dequeue_stack)