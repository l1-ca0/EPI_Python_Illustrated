# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node


def pivot_list(head: ListNode, pivot_value: int) -> Optional[ListNode]:
    """
    Partitions a linked list around a pivot value 'x'.
    
    Nodes with values less than x come first, then nodes with values equal to x,
    and finally nodes with values greater than x. The relative ordering within
    each partition is preserved.

    Args:
        head: The head node of the list.
        pivot_value: The integer value to partition around.

    Returns:
        The head of the reordered list.
    """
    # --- Step 1: Initialize three separate lists using dummy heads ---
    # Each list uses a tail pointer for efficient O(1) appends.
    less_head = less_tail = ListNode(0)
    equal_head = equal_tail = ListNode(0)
    greater_head = greater_tail = ListNode(0)

    # --- Step 2: Iterate through the original list and distribute nodes ---
    current_node = head
    while current_node:
        if current_node.data < pivot_value:
            # Append to the 'less than' list.
            less_tail.next = current_node
            less_tail = less_tail.next
        elif current_node.data == pivot_value:
            # Append to the 'equal to' list.
            equal_tail.next = current_node
            equal_tail = equal_tail.next
        else: # current_node.data > pivot_value
            # Append to the 'greater than' list.
            greater_tail.next = current_node
            greater_tail = greater_tail.next
        
        # Advance to the next node in the original list.
        current_node = current_node.next

    # --- Step 3: Combine the three lists ---
    
    # a) Terminate the 'greater than' list. This becomes the end of the final list.
    greater_tail.next = None
    
    # b) Link the 'equal to' list to the 'greater than' list.
    #    (The head of the 'greater' list is greater_head.next)
    equal_tail.next = greater_head.next
    
    # c) Link the 'less than' list to the 'equal to' list.
    less_tail.next = equal_head.next
    
    # The new head is the start of the 'less than' list.
    return less_head.next