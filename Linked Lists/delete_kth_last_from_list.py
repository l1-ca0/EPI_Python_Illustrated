# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def remove_kth_from_end(head: ListNode, k: int) -> Optional[ListNode]:
    """
    Removes the k-th node from the end of a linked list in a single pass.

    Args:
        head: The head node of the list.
        k: The position from the end (1-indexed, so k=1 is the last node).

    Returns:
        The head of the modified linked list.
    """
    # A dummy node simplifies edge cases, such as removing the head of the list.
    dummy_head = ListNode(0, head)

    # Initialize two pointers. The 'follower' will eventually point to the
    # node just before the one we want to delete.
    ahead_pointer = dummy_head
    follower_pointer = dummy_head

    # --- Step 1: Create a gap of k nodes between the two pointers ---
    # Advance the 'ahead_pointer' k steps into the list.
    for _ in range(k):
        # This check handles cases where k is larger than the list length.
        if not ahead_pointer.next:
            return head # k is invalid, return original list.
        ahead_pointer = ahead_pointer.next

    # --- Step 2: Move both pointers in tandem until ahead_pointer reaches the end ---
    # Because of the initial gap, when 'ahead_pointer' is at the last node,
    # 'follower_pointer' will be at the node right before our target.
    while ahead_pointer.next:
        ahead_pointer = ahead_pointer.next
        follower_pointer = follower_pointer.next

    # --- Step 3: Delete the target node ---
    # 'follower_pointer' is now at the (k+1)-th node from the end.
    # Its 'next' is the k-th node from the end, which is our target.
    # We bypass it to remove it from the list.
    follower_pointer.next = follower_pointer.next.next

    # The actual head of the modified list is the node after our dummy head.
    return dummy_head.next