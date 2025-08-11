import collections

class BinaryTreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def largest_complete_subtree_size(tree: BinaryTreeNode) -> int:
    """
    Finds the size of the largest complete subtree within a given binary tree.
    """

    # Named tuple to store the information returned from each recursive call.
    SubtreeInfo = collections.namedtuple('SubtreeInfo', 
                                         ('is_complete', 'size', 'height'))
    
    # Use a list to hold the max size so it can be modified by the nested function.
    max_size_tracker = [0]

    def get_subtree_info(node: BinaryTreeNode) -> SubtreeInfo:
        # Base case: An empty tree is a complete tree of size 0 and height -1.
        if not node:
            return SubtreeInfo(is_complete=True, size=0, height=-1)

        # Recursively get info from left and right children (post-order traversal).
        left_info = get_subtree_info(node.left)
        right_info = get_subtree_info(node.right)

        size = 1 + left_info.size + right_info.size
        height = 1 + max(left_info.height, right_info.height)
        is_complete = False

        # Check if the subtree at the current node is complete.
        # This requires that both its children's subtrees are complete.
        if left_info.is_complete and right_info.is_complete:
            # Condition 1: Heights are equal, left subtree must be perfect.
            # A perfect tree of height h has (2**(h+1) - 1) nodes.
            if left_info.height == right_info.height:
                if left_info.size == (1 << (left_info.height + 1)) - 1:
                    is_complete = True
            
            # Condition 2: Left is taller by 1, right subtree must be perfect.
            elif left_info.height == right_info.height + 1:
                if right_info.size == (1 << (right_info.height + 1)) - 1:
                    is_complete = True

        if is_complete:
            max_size_tracker[0] = max(max_size_tracker[0], size)
        
        return SubtreeInfo(is_complete, size, height)

    get_subtree_info(tree)
    return max_size_tracker[0]