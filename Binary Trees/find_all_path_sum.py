from typing import List

class BinaryTreeNode:
    """A standard binary tree node for context."""
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def find_all_paths_with_sum(tree: BinaryTreeNode, target_sum: int) -> List[List[int]]:
    """
    Finds all root-to-leaf paths that sum to a specific target value.
    Returns a list of paths, where each path is a list of node values.
    """
    all_paths = []

    def find_paths_helper(node: BinaryTreeNode, remaining_sum: int, current_path: List[int]):
        if not node:
            return

        # Add the current node to the path we are exploring.
        current_path.append(node.data)
        
        # Check if the current node is a leaf.
        is_leaf = not node.left and not node.right

        # If it's a leaf and the sum is correct, we've found a valid path.
        if is_leaf and node.data == remaining_sum:
            # Add a copy of the current path to our list of results.
            all_paths.append(list(current_path))
        else:
            # If not a leaf, continue exploring the children.
            new_remaining_sum = remaining_sum - node.data
            find_paths_helper(node.left, new_remaining_sum, current_path)
            find_paths_helper(node.right, new_remaining_sum, current_path)

        # Backtrack: Remove the current node from the path before returning.
        # This is essential for exploring other branches correctly.
        current_path.pop()
        
    find_paths_helper(tree, target_sum, [])
    return all_paths