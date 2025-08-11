import collections

# A standard class for a binary tree node.
class BinaryTreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    """
    Checks if a binary tree is height-balanced using a nested helper function.
    """

    # Define a simple data structure to return two values from the helper function:
    # 1. 'balanced': A boolean indicating if the subtree is balanced.
    # 2. 'height': The height of the subtree.
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    # It checks for balance and computes height in a single post-order traversal.
    def check_balanced(tree: BinaryTreeNode) -> BalancedStatusWithHeight:
        # Base Case: An empty tree is balanced and has a height of -1.
        # We use -1 so that a leaf node (with two empty children)
        # correctly gets a height of max(-1, -1) + 1 = 0.
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)

        # Recursive Step (Left): Process the left subtree first.
        left_result = check_balanced(tree.left)
        # If the left subtree is not balanced, we can stop early.
        # The entire tree is unbalanced, so propagate this result up.
        if not left_result.balanced:
            return left_result # Return the unbalanced status immediately

        # Recursive Step (Right): Process the right subtree.
        right_result = check_balanced(tree.right)
        # If the right subtree is not balanced, propagate this result up.
        if not right_result.balanced:
            return right_result # Return the unbalanced status immediately

        # Process Step (Root): Check the current node after its children are processed.
        # We know both subtrees are balanced, so we just check the height difference here.
        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        
        # Return the status and calculated height for the tree rooted at this node.
        return BalancedStatusWithHeight(is_balanced, height)

    # The main function's logic is to start the recursion on the root
    # of the tree and return the final boolean 'balanced' status.
    return check_balanced(tree).balanced