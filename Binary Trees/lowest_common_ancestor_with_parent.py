class BinaryTreeNode:
    """A standard binary tree node for context."""
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
class BinaryTreeNodeWithParent(BinaryTreeNode):
    """A node that includes a pointer to its parent."""
    def __init__(self, data=0, left=None, right=None, parent=None):
        super().__init__(data, left, right)
        self.parent = parent

def lca_with_parent_pointer(node0: BinaryTreeNodeWithParent, 
                            node1: BinaryTreeNodeWithParent) -> BinaryTreeNodeWithParent:
    """
    Computes the LCA of two nodes in a tree where nodes have parent pointers.
    """
    def get_depth(node):
        """Helper to calculate a node's depth by traversing up to the root."""
        depth = 0
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    # 1. Find the depth of each node.
    depth0, depth1 = get_depth(node0), get_depth(node1)

    # Make node0 the deeper node for simplicity.
    if depth1 > depth0:
        node0, node1 = node1, node0

    # 2. Ascend from the deeper node to equalize depths.
    depth_diff = abs(depth0 - depth1)
    while depth_diff > 0:
        node0 = node0.parent
        depth_diff -= 1

    # 3. Ascend from both nodes together until they meet at the LCA.
    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent
        
    return node0