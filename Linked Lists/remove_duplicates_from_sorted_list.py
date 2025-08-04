# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def remove_duplicates_from_sorted_list(head: ListNode) -> Optional[ListNode]:
    """
    Removes duplicate values from a sorted singly linked list, keeping one of each value.
    
    Args:
        head: The head node of the sorted list.
        
    Returns:
        The head of the list with duplicates removed.
    """
    current_node = head

    while current_node:
        # 'lookahead' will find the first node with a value different from current_node.
        lookahead = current_node.next

        # Keep advancing the lookahead pointer as long as it points to a duplicate.
        while lookahead and lookahead.data == current_node.data:
            lookahead = lookahead.next

        # At this point, 'lookahead' is either:
        # 1. The first node with a new value.
        # 2. None, if the rest of the list were all duplicates.
        
        # Bypass the duplicates by linking the current_node directly to the lookahead node.
        current_node.next = lookahead
        
        # Move on to the next distinct element to continue the process.
        current_node = lookahead

    return head