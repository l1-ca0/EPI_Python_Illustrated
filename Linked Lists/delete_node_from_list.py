# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def delete_node_from_list(node_to_delete: ListNode) -> None:
    """
    Deletes a node from a singly linked list, given only a reference to that node.

    This function has a critical assumption: the node to be deleted is NOT the tail
    of the linked list, as it relies on copying data from the next node.
    
    Args:
        node_to_delete: A direct reference to the node that needs to be removed.
    """
    if not node_to_delete or not node_to_delete.next:
        raise ValueError("This method cannot be used to delete the tail node.")

    # Get a reference to the node that comes immediately after our target node.
    next_node = node_to_delete.next

    # Step 1: Copy the data from the next node into the current node.
    # This effectively makes the current node a duplicate of the next one.
    node_to_delete.data = next_node.data

    # Step 2: Bypass the next node.
    # Change the current node's 'next' pointer to point to the node *after* the next one.
    # This unlinks the original 'next_node' from the list.
    node_to_delete.next = next_node.next

    # The original 'next_node' is now orphaned and will be reclaimed by the garbage collector.
    