class BinaryTreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_left, subtree_right):
        # both left subtree and right subtree is empty
        if not subtree_left and not subtree_right:
            return True
        # recursively check for symmetric subtree
        elif subtree_left and subtree_right:
            return (subtree_left.data == subtree_right.data
            and check_symmetric(subtree_left.left, subtree_right.right)
            and check_symmetric(subtree_left.right, subtree_right.left))
        # one subtree is empty, and the other is not
        return False

    return not tree or check_symmetric(tree.left, tree.right)