# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def add_two_numbers_msd_first(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
    """
    Adds two numbers represented by linked lists, where the most
    significant digit comes first.
    """
    # --- Step 1: Push list values onto stacks to access them in reverse order ---
    stack1 = []
    stack2 = []
    
    p1 = list1
    while p1:
        stack1.append(p1.data)
        p1 = p1.next
        
    p2 = list2
    while p2:
        stack2.append(p2.data)
        p2 = p2.next
        
    # --- Step 2: Add digits from right-to-left using the stacks ---
    carry = 0
    result_head = None # The head of our result list, built backwards.

    while stack1 or stack2 or carry:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0

        current_sum = val1 + val2 + carry
        new_digit = current_sum % 10
        carry = current_sum // 10
        
        # --- Step 3: Prepend the new digit to the front of the result list ---
        # This builds the final list in the correct MSD-first order.
        new_node = ListNode(new_digit)
        new_node.next = result_head
        result_head = new_node
        
    return result_head