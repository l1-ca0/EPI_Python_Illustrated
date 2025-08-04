# This code make use of the two helper functions in is_list_cyclic.py and overlapping_no_cycle_lists.py:
# 1. has_cycle(list_head): Returns the cycle's start node or None.
# 2. overlapping_no_cycle_lists(list1, list2): Finds overlap in two acyclic lists.

def find_list_overlap(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
    """
    Determines if two linked lists overlap, regardless of whether they contain cycles.
    Returns the overlapping node, or None if they do not overlap.
    """

    # --- Step 1: Check for cycles in each list ---
    # The has_cycle function returns the starting node of a cycle if one exists.
    cycle_start1 = has_cycle(list1)
    cycle_start2 = has_cycle(list2)

    # --- Case 1: Both lists are acyclic (no cycles were found) ---
    if not cycle_start1 and not cycle_start2:
        # If both are straight lists, delegate to the function designed for that case.
        return overlapping_no_cycle_lists(list1, list2)

    # --- Case 2: One list is cyclic and the other is not ---
    # A finite, non-cyclic list cannot merge into an infinite, cyclic list.
    elif (cycle_start1 and not cycle_start2) or \
         (not cycle_start1 and cycle_start2):
        return None

    # --- Case 3: Both lists have cycles ---
    # In this case, both cycle_start1 and cycle_start2 point to a valid node.
    # If the lists overlap, they must share the same cycle.
    else:
        # To check if they share a cycle, traverse one cycle (list2's cycle)
        # and see if the starting node of the other cycle (cycle_start1) is part of it.
        temp_pointer = cycle_start2
        
        while True:
            # If the pointer traversing cycle 2 ever runs into the start of cycle 1,
            # it proves they share the same cycle. Therefore, they overlap.
            if temp_pointer is cycle_start1:
                # Any node in the shared cycle is a valid overlap point.
                # We can simply return one of the cycle start nodes.
                return cycle_start1 

            # Advance the pointer through the cycle.
            temp_pointer = temp_pointer.next

            # If the pointer has made a full lap and returned to its starting point
            # without ever finding cycle_start1, the cycles must be separate.
            if temp_pointer is cycle_start2:
                return None # No overlap.