import collections

class BinaryTreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def find_first_unbalanced_node(tree: BinaryTreeNode, k: int) -> BinaryTreeNode:
    """
    Finds the lowest node that is not k-balanced, but whose descendants all are.
    """

    # Named tuple to hold the size and the potential result from a subtree.
    BalanceInfo = collections.namedtuple('BalanceInfo', ('size', 'result_node'))

    def check_k_balance(node: BinaryTreeNode, k: int) -> BalanceInfo:
        # Base case: An empty tree has size 0 and is balanced.
        if not node:
            return BalanceInfo(size=0, result_node=None)

        # Post-order traversal: Get info from left and right children first.
        left_info = check_k_balance(node.left, k)
        # If a result was found in the left subtree, propagate it up immediately.
        if left_info.result_node:
            return left_info

        right_info = check_k_balance(node.right, k)
        # If a result was found in the right subtree, propagate it up.
        if right_info.result_node:
            return right_info

        # At this point, we know all descendants are k-balanced.
        # Now, check the current node.
        node_size = 1 + left_info.size + right_info.size
        
        if abs(left_info.size - right_info.size) > k:
            # This is the first node from the bottom that is not k-balanced.
            return BalanceInfo(node_size, node)
        
        # This node is k-balanced, so continue the search upwards.
        return BalanceInfo(node_size, None)

    # The final result is the 'result_node' from the top-level call.
    return check_k_balance(tree, k).result_node