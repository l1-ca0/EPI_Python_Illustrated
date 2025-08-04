# class ListNode:
#     def __init__(self, data=0, next_node=None):
#         self.data = data
#         self.next = next_node

def find_overlap(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
    """
    Finds the first overlapping node of two linked lists that do not contain cycles.
    Returns the overlapping node, or None if they do not overlap.
    """

    # --- Step 1: Calculate the length of both lists ---
    def get_length(node: ListNode) -> int:
        """Helper function to calculate the length of a list."""
        count = 0
        current = node
        while current:
            count += 1
            current = current.next
        return count

    len1 = get_length(list1)
    len2 = get_length(list2)

    # Initialize pointers to the start of each list.
    pointer1, pointer2 = list1, list2

    # --- Step 2: Align the starting pointers ---
    # Advance the pointer of the longer list by the difference in lengths.
    # This ensures both pointers are equidistant from the end of their lists.
    if len1 > len2:
        for _ in range(len1 - len2):
            pointer1 = pointer1.next
    else: # len2 >= len1
        for _ in range(len2 - len1):
            pointer2 = pointer2.next

    # --- Step 3: Traverse in tandem to find the merge point ---
    # Advance both pointers one node at a time.
    # If the lists overlap, the pointers will eventually be the same object.
    while pointer1 and pointer2:
        if pointer1 is pointer2:
            return pointer1  # Found the overlap!

        pointer1 = pointer1.next
        pointer2 = pointer2.next

    # If the loop finishes, one of the pointers reached the end,
    # meaning there is no overlap.
    return None