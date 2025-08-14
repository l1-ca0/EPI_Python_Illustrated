def generate_gray_code_recursive(num_bits):
    # Base Case: The Gray code for 0 bits is just the number 0
    if num_bits == 0:
        return [0]

    # --- Recursive Step ---
    # 1- First, get the Gray code for one bit smaller
    gray_code_n_minus_1 = generate_gray_code_recursive(num_bits - 1)
    
    # 2- Create the "reflected" half
    # The new leading bit will be a '1' at the (n-1)th position
    # e.g., for 3 bits, this is 2^(3-1) = 4, or binary '100'
    leading_bit = 1 << (num_bits - 1)
    
    # Take the n-1 code, reverse it, and add the leading bit to each element
    reflected_half = [leading_bit | i for i in reversed(gray_code_n_minus_1)]
    
    # 3- Combine the original first half with the new reflected half
    return gray_code_n_minus_1 + reflected_half


def generate_gray_code_iterative(num_bits):
    # Start with the base case for 0 bits
    gray_code_sequence = [0]
    
    # Loop for each bit from 1 up to num_bits
    for i in range(num_bits):
        # The new leading bit to add for this iteration (1, 2, 4, 8, etc)
        leading_bit = 1 << i
        
        # Take the current sequence, reverse it, and add the new leading bit
        # Then, append this new half to the existing sequence
        reflected_half = [leading_bit | x for x in reversed(gray_code_sequence)]
        gray_code_sequence += reflected_half
        
    return gray_code_sequence