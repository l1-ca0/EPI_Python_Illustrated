def remove_excessive_duplicates(head: ListNode, m: int) -> Optional[ListNode]:
    """
    From a sorted list, remove all occurrences of any integer 'k'
    that appears more than 'm' times.

    Args:
        head: The head of the sorted linked list.
        m: The maximum allowed frequency for any integer.

    Returns:
        The head of the modified list.
    """
    # A dummy head simplifies removing nodes from the beginning of the list.
    dummy_head = ListNode(0, head)
    
    # 'previous' points to the last node of the list confirmed to be kept.
    previous = dummy_head
    current = head

    while current:
        # Start a runner to find the end of the current group of identical nodes.
        runner = current
        count = 0
        while runner and runner.data == current.data:
            count += 1
            runner = runner.next
        
        # Now, 'runner' points to the start of the next distinct group (or None).
        
        if count > m:
            # This group must be removed. Link the previous confirmed node
            # to the node after this group, bypassing it completely.
            previous.next = runner
        else:
            # This group is kept. Advance 'previous' to the last node of this group.
            previous = current
            # Note: We need to advance 'previous' past all nodes in the kept group.
            for _ in range(count - 1):
                previous = previous.next
        
        # Move to the start of the next group to continue processing.
        current = runner

    return dummy_head.next