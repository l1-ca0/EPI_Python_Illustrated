from typing import List

class BinaryTreeNode:
    """A standard binary tree node for context."""
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    """
    Performs an inorder traversal of a binary tree without using recursion.

    Args:
        tree: The root node of the binary tree.

    Returns:
        A list of node values in inorder sequence.
    """
    # s: The stack used to simulate recursive function calls.
    # result: The list to store the inorder traversal result.
    s, result = [], []
    
    # The loop continues as long as there are nodes to process (tree is not None)
    # or there are nodes on the stack we need to return to.
    while s or tree:
        # This 'if' block handles the "go left" part of the inorder traversal.
        if tree:
            # We have a node to process. Push it onto the stack to save it for later.
            s.append(tree)
            # Then, descend to its left child to go as far left as possible.
            tree = tree.left
        # This 'else' block handles the "visit root" and "go right" parts.
        else:
            # We have hit a dead end on a left path (tree is None).
            # It's time to process a node by popping it from the stack.
            # This will be the leftmost node not yet visited.
            tree = s.pop()
            
            # Visit the node by adding its data to the result list.
            result.append(tree.data)
            
            # Now, attempt to traverse the right subtree of the node we just visited.
            # The loop will then handle this right child, starting a new
            # "go as far left as possible" sequence from there.
            tree = tree.right
            
    return result