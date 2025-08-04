# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def merge_two_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists into one sorted linked list.
    
    :param l1: The head of the first sorted linked list.
    :param l2: The head of the second sorted linked list.
    :return: The head of the merged sorted linked list.
    """
    dummy_head = ListNode(0)  # Create a dummy node to simplify the merge process
    current = dummy_head      # Pointer to build the new list

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach the remaining elements, if any
    current.next = l1 or l2

    return dummy_head.next  # Return the merged list, skipping the dummy node