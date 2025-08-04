# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def reverse_linked_list(head: ListNode) -> Optional[ListNode]:
    """
    Reverses a singly linked list in-place.

    Args:
        head: The head node of the list to be reversed.

    Returns:
        The new head of the reversed list.
    """
    previous_node = None
    current_node = head

    # Traverse the list, reversing the 'next' pointer of each node.
    while current_node:
        # Store the next node before we overwrite the pointer.
        next_node_temp = current_node.next
        
        # Reverse the pointer of the current node to point to the previous one.
        current_node.next = previous_node
        
        # Move the pointers one step forward for the next iteration.
        previous_node = current_node
        current_node = next_node_temp

    # When the loop ends, 'previous_node' is the new head of the reversed list.
    return previous_node