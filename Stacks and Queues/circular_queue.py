class CircularQueue:
    """
    A queue implementation using a resizing circular array for efficient
    O(1) enqueue and dequeue operations (amortized for enqueue).
    """
    
    _SCALE_FACTOR = 2  # The factor by which to grow the array when resizing.

    def __init__(self, initial_capacity: int):
        """Initializes the queue with a given capacity."""
        if initial_capacity < 1:
            raise ValueError("Initial capacity must be at least 1.")
            
        self._entries = [None] * initial_capacity
        self._head = 0      # Index of the front element.
        self._tail = 0      # Index of the next available slot at the back.
        self._size = 0      # Current number of elements in the queue.

    def enqueue(self, item: int) -> None:
        """Adds an item to the back of the queue."""
        
        # --- Step 1: Resize the array if it's full ---
        if self._size == len(self._entries):
            # The resizing logic is handled in a helper method.
            self._resize()
        
        # --- Step 2: Add the new item at the tail position ---
        self._entries[self._tail] = item
        
        # --- Step 3: Advance the tail pointer, wrapping around if necessary ---
        self._tail = (self._tail + 1) % len(self._entries)
        self._size += 1

    def dequeue(self) -> int:
        """Removes and returns the item from the front of the queue."""
        
        if self.size() == 0:
            raise IndexError("dequeue from an empty queue")

        # Get the item from the front of the queue.
        item_to_return = self._entries[self._head]
        self._size -= 1
        
        # Advance the head pointer, wrapping around if necessary.
        self._head = (self._head + 1) % len(self._entries)
        
        return item_to_return

    def size(self) -> int:
        """Returns the number of items currently in the queue."""
        return self._size

    def _resize(self) -> None:
        """
        Private helper method to resize the internal array when it becomes full.
        """
        # Unwraps the circular elements into a new linear order using slicing.
        # e.g., if array is [d, e, _, _, a, b, c] with head at index 4,
        # the slices are [a, b, c] + [d, e].
        unwrapped_elements = (self._entries[self._head:] + self._entries[:self._head])
        
        # Reset the internal array with the unwrapped elements, then extend it.
        new_size = len(self._entries) * self._SCALE_FACTOR
        self._entries = unwrapped_elements + ([None] * (new_size - self._size))
        
        # After unwrapping, the head is at index 0 and the tail is after the last element.
        self._head = 0
        self._tail = self._size