class BinaryTreeNode:
    """A standard binary tree node for context."""
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def has_path_sum(tree: BinaryTreeNode, target_sum: int) -> bool:
    """
    Checks if there exists a root-to-leaf path that sums to target_sum.
    """
    # Base case: an empty tree cannot have a path sum.
    if not tree:
        return False

    # Check if the current node is a leaf.
    is_leaf = not tree.left and not tree.right
    
    # If it's a leaf, the path is valid only if the node's data
    # equals the remaining sum needed.
    if is_leaf:
        return target_sum == tree.data

    # If it's not a leaf, subtract the current node's data from the target
    # and check if a valid path exists in either the left OR right subtree.
    remaining_sum = target_sum - tree.data
    return (has_path_sum(tree.left, remaining_sum) or
            has_path_sum(tree.right, remaining_sum))
            