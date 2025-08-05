from typing import List

def is_well_formed(s: str) -> bool:
    """
    Checks if a string of brackets '()[]{}' is well-formed.
    A string is well-formed if:
    1. All opening brackets are closed by the same type of bracket.
    2. Brackets are closed in the correct order (last opened is first closed).

    Args:
        s: The input string of brackets.

    Returns:
        True if the string is well-formed, False otherwise.
    """
    # The stack will store the opening brackets as they are encountered.
    opening_brackets_stack: List[str] = []

    # A map to hold the relationship between opening and closing brackets.
    # This is used to quickly find the matching bracket for any opener.
    lookup_map = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        # If the character is an opening bracket, push it onto the stack.
        if char in lookup_map:
            opening_brackets_stack.append(char)
        
        else: # The character must be a closing bracket.
            # Check for two invalid conditions for a closing bracket:
            
            # 1. If the stack is empty, there is no opening bracket to match this
            #    closing bracket, so the string is invalid.
            if not opening_brackets_stack:
                return False

            # 2. If the stack is not empty, pop the last opening bracket and
            #    check if it matches the current closing bracket.
            last_opened_bracket = opening_brackets_stack.pop()
            if lookup_map[last_opened_bracket] != char:
                return False # Invalid due to mismatched brackets.

    # After iterating through the entire string, if it is well-formed,
    # the stack must be empty. If it's not empty, it means there
    # are unclosed opening brackets.
    return not opening_brackets_stack