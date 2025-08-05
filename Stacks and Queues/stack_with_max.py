class MaxStack:
    """
    A stack that supports finding the max element in O(1) time, using
    optimized space for the max cache.
    """
    def __init__(self):
        self._element_stack: List[int] = []
        # A separate stack to track only the maximum values as they appear.
        self._max_stack: List[int] = []

    def is_empty(self) -> bool:
        return not self._element_stack

    def get_max(self) -> int:
        if not self._max_stack:
            raise IndexError("get_max() on an empty stack")
        return self._max_stack[-1]

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("pop() from an empty stack")
        
        popped_element = self._element_stack.pop()
        
        # If the element being popped is the current maximum, then the
        # maximum value must be updated by popping from the max_stack as well.
        if popped_element == self.get_max():
            self._max_stack.pop()
            
        return popped_element

    def push(self, x: int) -> None:
        self._element_stack.append(x)
        
        # Push to the max_stack only if the new element is a new maximum
        # or if the max_stack is empty. Using '>=' correctly handles
        # pushing duplicate values of the current maximum.
        if not self._max_stack or x >= self.get_max():
            self._max_stack.append(x)