from typing import List

def phone_mnemonic_iterative(phone_number: str) -> List[str]:
    """
    Generates all mnemonics for a phone number using an iterative approach

    Args:
        phone_number: A string of digits 

    Returns:
        A list of all possible character sequences (mnemonics)
    """
    # Same mapping as the recursive version
    MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

    # Handle empty input
    if not phone_number:
        return []
        
    # Initialize the list of mnemonics with an empty string. This is the starting
    # point from which all mnemonics will be built
    mnemonics = ['']

    # Iterate through each digit in the input phone number
    for digit_char in phone_number:
        digit = int(digit_char)
        letters = MAPPING[digit]
        
        # Create a new list of mnemonics by expanding the existing ones
        mnemonics = [
            partial_mnemonic + letter
            for partial_mnemonic in mnemonics
            for letter in letters
        ]
        
    return mnemonics

# Example usage and walkthrough for "23":
# 1. Start with mnemonics = ['']
#
# 2. Process first digit '2' (letters "ABC"):
#    - new_mnemonics = ['' + 'A', '' + 'B', '' + 'C']
#    - mnemonics becomes ['A', 'B', 'C']
#
# 3. Process second digit '3' (letters "DEF"):
#    - new_mnemonics = ['A'+'D', 'A'+'E', 'A'+'F', 'B'+'D', 'B'+'E', 'B'+'F', ...]
#    - mnemonics becomes ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
#
# 4. Return the final list.

print(phone_mnemonic_iterative("23"))
# Expected output: ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']