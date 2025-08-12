# The total number of pegs is constant.
NUM_PEGS = 3

def compute_tower_hanoi(num_rings):
    """
    Sets up and solves the Tower of Hanoi problem for a given number of rings.
    
    Args:
        num_rings: The number of rings to move.
        
    Returns:
        A list of lists, where each inner list represents a move [from_peg, to_peg].
    """
    
    # pegs is a list of lists. Each inner list represents a peg.
    # Peg 0 starts with all the rings, from largest (bottom) to smallest (top).
    # e.g., for 3 rings, pegs = [[3, 2, 1], [], []]
    pegs = [list(range(num_rings, 0, -1))] + [[] for _ in range(NUM_PEGS - 1)]
    
    # This list will store the sequence of moves required to solve the puzzle.
    result = []

    # Initial call to the recursive helper function to start the process.
    # We want to move 'num_rings' from peg 0 to peg 2, using peg 1 as auxiliary.
    compute_tower_hanoi_steps(num_rings, 0, 2, 1, pegs, result)
    
    return result

def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg, pegs, result):
    """
    Recursively calculates the steps to move a tower of rings.
    
    Args:
        num_rings_to_move: The number of rings in the current sub-problem.
        from_peg: The starting peg for this sub-problem.
        to_peg: The destination peg for this sub-problem.
        use_peg: The auxiliary (temporary) peg.
        pegs: The current state of all pegs.
        result: The list to record moves.
    """
    # Base case for the recursion: if there are no rings to move, do nothing.
    if num_rings_to_move > 0:
        # Step 1: Recursively move the top n-1 rings from the 'from_peg'
        # to the 'use_peg'. The 'to_peg' now serves as the temporary peg.
        compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg, pegs, result)
        
        # Step 2: Move the single, largest remaining ring from 'from_peg' to 'to_peg'.
        # .pop() removes the top ring from the 'from_peg'.
        # .append() adds it to the top of the 'to_peg'.
        pegs[to_peg].append(pegs[from_peg].pop())
        
        # Record this move in the result list.
        result.append([from_peg, to_peg])
        
        # Step 3: Recursively move the n-1 rings that we placed on the 'use_peg'
        # onto the final 'to_peg'. The original 'from_peg' now serves as the temporary peg.
        compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg, from_peg, pegs, result)

# Example usage for 3 rings:
# print(compute_tower_hanoi(3))
# Expected output: [[0, 2], [0, 1], [2, 1], [0, 2], [1, 0], [1, 2], [0, 2]]
