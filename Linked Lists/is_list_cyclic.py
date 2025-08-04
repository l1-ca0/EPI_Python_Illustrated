# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def has_cycle(head: ListNode) -> Optional[ListNode]:
    """
    Finds the start of a cycle using the Floyd's algorithm.
    """
    slow = head
    fast = head

    # Phase 1: Find the meeting point inside the cycle.
    # The fast pointer will lap the slow pointer if a cycle exists.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # A collision has been found.
        if slow is fast:
            # Phase 2: Find the cycle's start node.
            # One pointer is reset to the head of the list. The other
            # remains at the meeting point.
            slow = head

            # Both pointers are now advanced one step at a time.
            # Their next meeting point is the start of the cycle.
            while slow is not fast:
                slow = slow.next
                fast = fast.next

            # Return the start node of the cycle.
            return slow

    # If the loop finishes, no meeting occurred, so no cycle exists.
    return None