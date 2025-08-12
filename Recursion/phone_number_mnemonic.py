from typing import List

# A mapping from digit to corresponding characters on a phone keypad.
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonic(phone_number: str) -> List[str]:
    """
    The main function that initializes the process of finding all mnemonics for a phone number

    Args:
        phone_number: A string of digits

    Returns:
        A list of all possible character sequences (mnemonics)
    """
    # This list will store the final results
    mnemonics: List[str] = []
    
    # A list of characters to build each mnemonic. We use a list because strings are immutable
    partial_mnemonic = [''] * len(phone_number)

    # Start the recursive process from the first digit (index 0)
    phone_mnemonic_helper(0, phone_number, partial_mnemonic, mnemonics)
    
    return mnemonics

def phone_mnemonic_helper(digit_idx: int, phone_number: str, partial_mnemonic: List[str], mnemonics: List[str]):
    """
    A recursive helper function that generates mnemonics

    Args:
        digit_idx: The current index in the phone_number we are processing
        phone_number: The original phone number string
        partial_mnemonic: The current mnemonic being built
        mnemonics: The list to store completed mnemonics
    """
    
    # Base Case: If we have processed all digits (the index matches the length of the number),
    # it means we have a complete mnemonic
    if digit_idx == len(phone_number):
        # Join the characters in our working list to form the final string
        # and add it to our list of results.
        mnemonics.append(''.join(partial_mnemonic))
    else:
        # Recursive Step: If there are still digits left to process...
        
        # Get the current digit from the phone number string
        current_digit = int(phone_number[digit_idx])
        
        # Loop through all possible letters for the current digit (e.g., 'A', 'B', 'C' for 2)
        for char in MAPPING[current_digit]:
            # 1. Place the character at the current position in our partial mnemonic
            partial_mnemonic[digit_idx] = char
            
            # 2. Recurse to handle the next digit in the number
            phone_mnemonic_helper(digit_idx + 1, phone_number, partial_mnemonic, mnemonics)
            
            # 3. "Backtrack": When the recursive call returns, the loop continues to the
            #    next character, automatically overwriting the previous one. No explicit
            #    cleanup is needed here because of the loop's nature.

# Example usage:
# print(phone_mnemonic("23"))
# Expected output: ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']