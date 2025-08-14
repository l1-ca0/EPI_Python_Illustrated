from typing import List

def decompose_into_palindromes(text: str) -> List[List[str]]:
    """
    Finds all possible ways to partition a string into a sequence of palindromes

    Args:
        text: The input string to decompose

    Returns:
        A list of all possible decompositions, where each decomposition is a list of strings
    """
    decompositions = []

    def find_decompositions_helper(start_index: int, current_decomposition: List[str]):
        """
        A recursive helper that finds partitions starting from a given index
        """
        
        # Base Case: If our starting index is past the end of the string,
        # it means we have successfully partitioned the entire string
        if start_index == len(text):
            decompositions.append(list(current_decomposition))
            return

        # --- Recursive Step ---
        # Try every possible "cut" by creating prefixes of increasing length
        # starting from the 'start_index'
        for i in range(start_index, len(text)):
            # The potential next piece of our partition
            prefix = text[start_index : i + 1]
            
            # Check if this piece is a palindrome
            if prefix == prefix[::-1]:
                # 1- CHOOSE: If it's a palindrome, add it to our current path
                current_decomposition.append(prefix)
                
                # 2- EXPLORE: Recurse on the rest of the string
                # The next search will start right after the end of our chosen prefix
                find_decompositions_helper(i + 1, current_decomposition)
                
                # 3- UN-CHOOSE (Backtrack): Remove the prefix so we can try the next
                # longer prefix in the loop
                current_decomposition.pop()

    # Start the process from the beginning of the string (index 0) with an empty list
    find_decompositions_helper(0, [])
    return decompositions

