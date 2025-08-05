# Assume a DoublyListNode class with 'data', 'next', and 'prev' attributes.
def is_doubly_linked_palindrome(head: DoublyListNode, tail: DoublyListNode) -> bool:
    """
    Checks if a doubly linked list is a palindrome, given pointers to the head and tail.
    """
    if not head:
        return True

    # Initialize pointers at both ends of the list.
    forward_pointer = head
    backward_pointer = tail
    
    # Traverse inwards from both ends, comparing nodes.
    # The loop continues until the pointers meet (for odd-length lists)
    # or cross (for even-length lists).
    while forward_pointer != backward_pointer and forward_pointer.prev != backward_pointer:
        
        # If data at corresponding positions doesn't match, it's not a palindrome.
        if forward_pointer.data != backward_pointer.data:
            return False
            
        # Move pointers one step closer to the middle.
        forward_pointer = forward_pointer.next
        backward_pointer = backward_pointer.prev
        
    # If the loop completes, all mirrored pairs matched.
    return True