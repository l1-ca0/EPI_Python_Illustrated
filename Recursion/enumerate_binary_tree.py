class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

def generate_all_binary_trees(num_nodes):
    """
    Generates a list of all structurally unique binary trees with a given number of nodes
    """
    
    # Base Case: A request for a tree with 0 nodes results in an empty tree (None)
    # We return it in a list because the loops below expect to iterate over a list
    if num_nodes == 0:
        return [None]

    all_trees = []
    # Iterate through all possible sizes for the LEFT subtree
    # It can range from 0 nodes up to num_nodes - 1
    for num_nodes_left in range(num_nodes):
        # The remaining nodes must go into the RIGHT subtree
        # We subtract 1 for the current root node
        num_nodes_right = num_nodes - 1 - num_nodes_left
        
        # --- Recursive Calls ---
        # Get all possible unique subtrees for the left and right sides
        all_left_subtrees = generate_all_binary_trees(num_nodes_left)
        all_right_subtrees = generate_all_binary_trees(num_nodes_right)
        
        # --- Combination Step ---
        # Now, combine every possible left subtree with every possible right subtree
        # to form all new trees for this specific split of nodes
        for left_subtree in all_left_subtrees:
            for right_subtree in all_right_subtrees:
                # Create a new root and attach the left and right subtrees
                new_tree = TreeNode(0, left_subtree, right_subtree)
                all_trees.append(new_tree)
                
    return all_trees

# --- Example for n=3 ---
num_nodes = 3
result = generate_all_binary_trees(num_nodes)
print(f"Found {len(result)} unique binary trees with {num_nodes} nodes")
# This should print 5, which matches Figure 15.6 in your image