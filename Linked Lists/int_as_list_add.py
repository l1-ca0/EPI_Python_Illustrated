# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def add_two_numbers(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
    """
    Adds two numbers represented by linked lists, where the least
    significant digit comes first.
    """
    # A dummy head simplifies the creation of the new result list.
    result_dummy_head = ListNode(0)
    # 'result_tail' will always point to the last node of our result list.
    result_tail = result_dummy_head

    carry = 0
    p1 = list1
    p2 = list2

    # The loop must continue as long as there are digits in either list
    # or there is a carry-over value from the last calculation.
    while p1 or p2 or carry:
        # Get the value from the current node, or 0 if the list is exhausted.
        val1 = p1.data if p1 else 0
        val2 = p2.data if p2 else 0

        # --- Perform the addition for the current place value ---
        current_sum = val1 + val2 + carry
        new_digit = current_sum % 10
        carry = current_sum // 10

        # --- Append the new digit to our result list ---
        result_tail.next = ListNode(new_digit)
        result_tail = result_tail.next

        # --- Advance pointers to the next nodes (if they exist) ---
        if p1: p1 = p1.next
        if p2: p2 = p2.next
    
    return result_dummy_head.next
