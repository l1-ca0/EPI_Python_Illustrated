class BinaryTreeNode:
    """A standard binary tree node for context."""
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    """
    Computes the sum of all numbers represented by root-to-leaf paths.
    """
    def sum_helper(node: BinaryTreeNode, partial_path_sum: int) -> int:
        # Base case: an empty node contributes nothing to the sum.
        if not node:
            return 0

        # Update the path sum. A left shift ( * 2) and add is how we
        # append a new binary digit to the end of a number.
        partial_path_sum = partial_path_sum * 2 + node.data

        # Leaf node case: this is the end of a path, so return its full value.
        if not node.left and not node.right:
            return partial_path_sum

        # Non-leaf node case: return the sum of paths from the left and right subtrees.
        return sum_helper(node.left, partial_path_sum) + sum_helper(node.right, partial_path_sum)

    return sum_helper(tree, 0)