def generate_power_set_bitwise(input_set):
    """
    Generates the power set by mapping subsets to binary numbers (bit masks)
    """
    power_set = []
    # We use a list to have a fixed order
    input_list = list(input_set)
    num_elements = len(input_list)
    
    # We will loop from 0 to 2^n - 1
    # Each number 'i' represents a unique subset
    for i in range(1 << num_elements): # 1 << n is a fast way to calculate 2^n
        current_subset = []
        
        # Now, we check the bits of 'i' to see which "switches" are on
        for j in range(num_elements):
            # Use the bitwise AND operator to check if the j-th bit is set to 1
            # (1 << j) creates a mask with a 1 only at the j-th position (e.g., 001, 010, 100)
            if (i & (1 << j)):
                # If the j-th bit is on, add the j-th element to the subset
                current_subset.append(input_list[j])
                
        power_set.append(current_subset)
        
    return power_set

# Example
print("\nBitwise Solution for {0, 1, 2}:")
print(generate_power_set_bitwise({0, 1, 2}))