def generate_power_set_recursive(input_set):
    """
    Generates the power set using a recursive 'in or out' approach
    """
    power_set = []
    # We convert the set to a list to work with indices
    input_list = list(input_set)

    def find_subsets(index, current_subset):
        # Base Case: If we've considered every element, we're done
        # The current_subset is complete, so add it to our final list
        if index == len(input_list):
            power_set.append(list(current_subset))
            return

        # --- The Two Choices ---
        
        # Choice 1: EXCLUDE the current element
        # We simply move on to the next element without adding the current one
        find_subsets(index + 1, current_subset)

        # Choice 2: INCLUDE the current element
        # We add the current element to the subset and then move on
        current_subset.append(input_list[index])
        find_subsets(index + 1, current_subset)
        
        # Backtrack: We remove the element we just added so that the state is clean
        # for the previous recursive calls
        current_subset.pop()

    # Start the process from the first element (index 0) with an empty subset
    find_subsets(0, [])
    return power_set

