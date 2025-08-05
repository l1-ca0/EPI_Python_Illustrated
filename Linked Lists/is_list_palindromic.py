# Assume a helper function 'reverse_linked_list' exists:
# def reverse_linked_list(head: ListNode) -> ListNode: ...

def is_linked_list_a_palindrome(head: ListNode) -> bool:
    """
    Checks if a singly linked list is a palindrome in O(n) time and O(1) space.
    """
    if not head or not head.next:
        return True # An empty or single-node list is a palindrome.

    # --- Step 1: Find the middle of the linked list ---
    slow = fast = head
    # This loop positions 'slow' at the node right before the midpoint.
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # --- Step 2: Reverse the second half of the list ---
    # The second half starts at the node after 'slow'.
    second_half_head = reverse_linked_list(slow.next)

    # --- Step 3: Compare the first half with the reversed second half ---
    first_half_pointer = head
    second_half_pointer = second_half_head
    is_a_match = True
    while second_half_pointer:
        if first_half_pointer.data != second_half_pointer.data:
            is_a_match = False
            break
        first_half_pointer = first_half_pointer.next
        second_half_pointer = second_half_pointer.next

    # --- Step 4: Restore the original list ---
    # Re-reverse the second half and link it back to the first half.
    slow.next = reverse_linked_list(second_half_head)

    return is_a_match