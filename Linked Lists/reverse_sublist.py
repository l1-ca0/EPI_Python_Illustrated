# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def reverse_sublist(head: ListNode, start: int, finish: int) -> Optional[ListNode]:
    """
    Reverses the nodes of a linked list from position 'start' to 'finish'.
    The list positions are 1-indexed.
    """
    # A dummy node simplifies handling edge cases, like reversing from the beginning of the list.
    dummy_head = ListNode(0, head)

    # 1. Find the node just *before* the sublist to be reversed.
    # We will need to change this node's 'next' pointer later.
    node_before_sublist = dummy_head
    for _ in range(start - 1):
        node_before_sublist = node_before_sublist.next

    # 'sublist_head' is the first node in the part we are reversing.
    # It will be moved during the process and end up as the tail of the reversed part.
    sublist_head = node_before_sublist.next

    # 2. Perform the reversal.
    # This loop runs (finish - start) times. In each iteration, it takes the node
    # immediately after 'sublist_head' and moves it to the front of the sublist.
    for _ in range(finish - start):
        # Identify the node we need to move to the front.
        node_to_move = sublist_head.next

        # A) Detach 'node_to_move' from its current position.
        #    'sublist_head' now skips over 'node_to_move' and points to the node after it.
        sublist_head.next = node_to_move.next

        # B) Re-link 'node_to_move' to the beginning of the reversed section.
        #    The current beginning of the reversed section is what 'node_before_sublist' points to.
        node_to_move.next = node_before_sublist.next

        # C) Update the head of the reversed section.
        #    'node_before_sublist' now points to 'node_to_move', making it the new front.
        node_before_sublist.next = node_to_move

    # Return the head of the fully modified list, which is the node after our dummy head.
    return dummy_head.next