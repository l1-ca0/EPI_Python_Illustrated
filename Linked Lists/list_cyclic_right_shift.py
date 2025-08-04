# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node


def rotate_list_right(head: ListNode, k: int) -> Optional[ListNode]:
    """
    Performs a cyclic right shift on a singly linked list by k positions.

    Args:
        head: The head node of the list.
        k: The number of positions to shift right (non-negative).

    Returns:
        The new head of the cyclically shifted list.
    """
    # Handle edge cases: empty list, single-node list, or no shift.
    if not head or not head.next or k == 0:
        return head

    # --- Step 1: Find the length and the original tail of the list ---
    list_length = 1
    tail = head
    while tail.next:
        list_length += 1
        tail = tail.next
    
    # At this point, 'tail' is the last node and 'list_length' is known.

    # --- Step 2: Normalize k and handle the no-op case ---
    # A shift by 'k' is the same as a shift by 'k % list_length'.
    k %= list_length
    if k == 0:
        return head # No effective shift needed.

    # --- Step 3: Form a cycle, find the new endpoints, and break the cycle ---
    
    # a) Connect the original tail to the original head to form a cycle.
    tail.next = head

    # b) Find the new tail. The new tail is the (n-k)-th node from the beginning
    #    of the original list. We need to take (n-k-1) steps from the head to reach it.
    steps_to_new_tail = list_length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
        
    # 'new_tail' now points to the node that will become the end of the new list.

    # c) The new head is the node right after the new tail.
    new_head = new_tail.next

    # d) Break the cycle by setting the new tail's 'next' pointer to None.
    new_tail.next = None

    return new_head