# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def even_odd_merge(head: ListNode) -> Optional[ListNode]:
    """
    Reorders a linked list so that all even-indexed nodes appear before all
    odd-indexed nodes, preserving relative order within each group.
    (Indices are 0-based).

    Args:
        head: The head node of the list.

    Returns:
        The head of the reordered list.
    """
    if not head:
        return None

    # --- Step 1: Initialize two sublists, one for even and one for odd nodes ---
    # We use dummy heads to make appending nodes easier.
    even_dummy_head = ListNode(0)
    odd_dummy_head = ListNode(0)

    # 'even_tail' and 'odd_tail' will track the last node of each sublist.
    even_tail = even_dummy_head
    odd_tail = odd_dummy_head

    # --- Step 2: Iterate through the original list, distributing nodes ---
    current_node = head
    index = 0
    while current_node:
        # Detach the current node and decide where it goes.
        next_node_in_original_list = current_node.next
        
        if index % 2 == 0: # Even-indexed node
            even_tail.next = current_node
            even_tail = even_tail.next
        else: # Odd-indexed node
            odd_tail.next = current_node
            odd_tail = odd_tail.next
        
        # Move to the next node in the original list.
        current_node = next_node_in_original_list
        index += 1

    # --- Step 3: Terminate the lists and merge them ---
    
    # The last node of the odd list must point to None to end the full list.
    odd_tail.next = None
    
    # Attach the head of the odd sublist to the tail of the even sublist.
    even_tail.next = odd_dummy_head.next

    # The head of the reordered list is the head of the even sublist.
    return even_dummy_head.next