def decompose_into_dictionary_words(domain, dictionary):
    """
    Decomposes a string into a sequence of dictionary words
    Returns one valid decomposition if it exists
    """
    word_set = set(dictionary)
    
    # predecessor_idx[i] stores the start index of the last word
    # in a valid decomposition of the prefix `domain[:i]`
    predecessor_idx = [-1] * (len(domain) + 1)
    
    # Base Case: The start of the string has a predecessor of 0
    predecessor_idx[0] = 0
    
    # --- Phase 1: Fill the predecessor array ---
    for i in range(1, len(domain) + 1):
        for j in range(i):
            # If the prefix `domain[:j]` is reachable and `domain[j:i]` is a word
            if predecessor_idx[j] != -1 and domain[j:i] in word_set:
                # We can reach `i` from `j`, so store `j` as the predecessor
                predecessor_idx[i] = j
                break

    # --- Phase 2: Reconstruct the path from the predecessors ---
    decompositions = []
    # Check if a full decomposition was found for the entire domain
    if predecessor_idx[-1] != -1:
        curr_idx = len(domain)
        while curr_idx > 0:
            # Get the start index of the current word
            start_idx = predecessor_idx[curr_idx]
            # Slice the word from the domain
            decompositions.append(domain[start_idx:curr_idx])
            # Jump back to the start of that word for the next iteration
            curr_idx = start_idx
            
    # The words were found backwards, so reverse for the correct order
    return decompositions[::-1]

