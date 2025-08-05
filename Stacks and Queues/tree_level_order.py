import collections
from typing import List, Optional

# A BinaryTreeNode class is assumed to be defined as follows:
# class BinaryTreeNode:
#     def __init__(self, data=0, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

def binary_tree_level_order(tree: Optional[BinaryTreeNode]) -> List[List[int]]:
    """
    Performs a level-order (BFS) traversal of a binary tree.

    Args:
        tree: The root node of the binary tree.

    Returns:
        A list of lists, where each inner list contains the node
        values at a particular level, from top to bottom.
    """
    if not tree:
        return []

    result: List[List[int]] = []
    # A deque from the collections module is an efficient implementation of a queue.
    nodes_to_visit = collections.deque([tree])

    while nodes_to_visit:
        # Get the number of nodes at the current level before processing.
        num_nodes_in_level = len(nodes_to_visit)
        current_level_values: List[int] = []

        # Process all nodes for just the current level.
        for _ in range(num_nodes_in_level):
            # Dequeue the next node from the front of the queue.
            current_node = nodes_to_visit.popleft()
            
            # Add its value to the list for this level.
            current_level_values.append(current_node.data)

            # Enqueue its children to be processed in the next level's iteration.
            if current_node.left:
                nodes_to_visit.append(current_node.left)
            if current_node.right:
                nodes_to_visit.append(current_node.right)
        
        # Add the completed level's values to the main result list.
        result.append(current_level_values)
        
    return result 