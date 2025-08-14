from typing import List

def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    """
    Generates all valid combinations of balanced parentheses for a given number of pairs

    Args:
        num_pairs: The number of pairs of parentheses to use (e.g., 3 means '((()))', etc)

    Returns:
        A list of all valid parenthesis strings
    """
    solutions = []

    def find_all_combinations(left_needed: int, right_needed: int, current_string: str):
        # Base Case: When we've used up all parentheses, we have a valid solution
        if left_needed == 0 and right_needed == 0:
            solutions.append(current_string)
            return

        # --- Recursive Choices ---

        # Choice 1: Can we add a left parenthesis
        # We can as long as we still have some left parentheses to place
        if left_needed > 0:
            find_all_combinations(
                left_needed - 1, 
                right_needed, 
                current_string + '('
            )

        # Choice 2: Can we add a right parenthesis
        # This is only valid if the number of right parentheses we need
        # is greater than the number of left ones we still need
        # This ensures we always have a matching '(' for every ')' we place
        if right_needed > left_needed:
            find_all_combinations(
                left_needed, 
                right_needed - 1, 
                current_string + ')'
            )

    # Start the recursion with the full number of pairs to add and an empty string
    find_all_combinations(num_pairs, num_pairs, "")
    return solutions
