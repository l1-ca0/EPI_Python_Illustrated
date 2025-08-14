from typing import List

def combinations(n: int, k: int) -> List[List[int]]:
    """
    Generates all combinations (subsets of size k) from the set {1, 2, ..., n}

    Args:
        n: The number of elements in the total set
        k: The desired size of each combination (subset)

    Returns:
        A list of all combinations
    """
    combinations = []
    
    def find_combinations_helper(start_num: int, current_combo: List[int]):
        # --- Base Case 1: Success ---
        # If the current combination has reached the desired size k, we're done
        if len(current_combo) == k:
            # Add a copy of the valid combination to our results and stop this path
            combinations.append(list(current_combo))
            return

        # --- Base Case 2: Pruning ---
        # If the number of elements we still need is more than the number
        # of elements available, then it's impossible to form a valid combination
        # This check prevents a lot of unnecessary work
        needed = k - len(current_combo)
        available = n - start_num + 1
        if needed > available:
            return

        # --- Recursive Step ---
        # Iterate from the current starting number up to n
        for i in range(start_num, n + 1):
            # 1- CHOOSE: Add the number 'i' to our current combination
            current_combo.append(i)
            
            # 2- EXPLORE: Recurse to find the rest of the combination
            # We start the next search from 'i + 1' to avoid duplicates and re-using elements
            find_combinations_helper(i + 1, current_combo)
            
            # 3- UN-CHOOSE (Backtrack): Remove 'i' so we can try the next number in the loop
            current_combo.pop()

    # Start the process by trying to pick the first number (1) with an empty combo
    find_combinations_helper(1, [])
    return combinations

