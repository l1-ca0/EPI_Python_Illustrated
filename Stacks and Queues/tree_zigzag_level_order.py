def zigzag_level_order(tree: Optional[BinaryTreeNode]) -> List[List[int]]:
    if not tree:
        return []

    result: List[List[int]] = []
    nodes_to_visit = collections.deque([tree])
    is_left_to_right = True # A flag to track the direction for each level.

    while nodes_to_visit:
        num_nodes_in_level = len(nodes_to_visit)
        current_level_values: List[int] = []

        for _ in range(num_nodes_in_level):
            current_node = nodes_to_visit.popleft()
            current_level_values.append(current_node.data)
            if current_node.left:
                nodes_to_visit.append(current_node.left)
            if current_node.right:
                nodes_to_visit.append(current_node.right)
        
        # If the direction for this level is right-to-left, reverse the values.
        if not is_left_to_right:
            current_level_values.reverse()

        result.append(current_level_values)
        # Flip the direction for the next level.
        is_left_to_right = not is_left_to_right
        
    return result