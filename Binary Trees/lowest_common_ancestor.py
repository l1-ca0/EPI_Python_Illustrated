import collections

class BinaryTreeNode:
    """A standard binary tree node for context."""
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
'''
The most efficient approach uses a single, recursive traversal. The core idea is that for any given node n, we can determine its relationship to the LCA by looking at its subtrees. 
We can perform a post-order traversal (Left, Right, Root) and have our recursive function return two key pieces of information from each subtree:
    1. The number of target nodes (the two nodes we're looking for) found in the subtree.
    2. A pointer to the LCA if it has been found within that subtree.

The LCA is identified when:
    1. A node's left subtree contains one of the target nodes and its right subtree contains the other. In this case, the current node is the LCA
    2. The current node is one of the target nodes, and the other target node is found in one of its subtrees. In this case, the current node is also the LCA.
If a recursive call reports that it has found both target nodes, the LCA has already been identified below it, and we simply pass that result up the call stack.
'''
def lca_without_parent_pointer(tree: BinaryTreeNode, node0: BinaryTreeNode, 
                               node1: BinaryTreeNode) -> BinaryTreeNode:
    """
    Computes the LCA of two nodes in a binary tree.
    """
    # Status tuple to hold the number of target nodes found in a subtree
    # and a pointer to the LCA if found.
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(node: BinaryTreeNode) -> Status:
        # Base case: An empty node contains no targets.
        if not node:
            return Status(num_target_nodes=0, ancestor=None)

        # Post-order traversal: recurse on children first.
        left_result = lca_helper(node.left)
        # If LCA is already found in the left subtree, propagate the result up.
        if left_result.num_target_nodes == 2:
            return left_result

        right_result = lca_helper(node.right)
        # If LCA is already found in the right subtree, propagate the result up.
        if right_result.num_target_nodes == 2:
            return right_result

        # Check if the current node is one of the targets.
        num_nodes_here = (left_result.num_target_nodes +
                          right_result.num_target_nodes +
                          (1 if node is node0 or node is node1 else 0))

        # If we have found both nodes in the subtree rooted at 'node',
        # then 'node' is the LCA. Otherwise, no LCA has been found yet.
        ancestor = node if num_nodes_here == 2 else None
        
        return Status(num_nodes_here, ancestor)

    return lca_helper(tree).ancestor