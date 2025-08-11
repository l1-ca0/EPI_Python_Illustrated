from typing import List

class BinaryTreeNode:
    """A standard binary tree node for context."""
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    """
    Performs a preorder traversal of a binary tree without using recursion.

    Args:
        tree: The root node of the binary tree.

    Returns:
        A list of node values in preorder sequence.
    """
    # Handle the edge case of an empty tree.
    if not tree:
        return []

    # Initialize the stack with the root node. The stack will hold nodes
    # that we need to visit in the future.
    s = [tree]
    result = []

    # Continue the loop as long as there are nodes to process on the stack.
    while s:
        # Get the next node to process by popping from the top of the stack.
        current_node = s.pop()

        # Visit the node by adding its data to the result list.
        result.append(current_node.data)

        # IMPORTANT: Push the right child first, then the left child.
        # Since the stack is LIFO (Last-In, First-Out), the left child
        # will be processed before the right child.

        # If the right child exists, push it onto the stack.
        if current_node.right:
            s.append(current_node.right)

        # If the left child exists, push it onto the stack. It will now
        # be at the top, ensuring it's the next node we process.
        if current_node.left:
            s.append(current_node.left)
            
    return result