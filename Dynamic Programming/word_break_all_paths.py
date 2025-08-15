def decompose_into_all_paths(domain, dictionary):
    """
    Finds all possible decompositions of a string into dictionary words
    """
    word_set = set(dictionary)
    
    # --- Phase 1: Build a graph of predecessors ---
    # predecessors[i] will store a list of all valid start indices
    # for words that end at position `i`
    predecessors = [[] for _ in range(len(domain) + 1)]
    predecessors[0] = [0] # Base case for the start of the string

    for i in range(1, len(domain) + 1):
        for j in range(i):
            # If the prefix `domain[:j]` is reachable and `domain[j:i]` is a word
            if predecessors[j] and domain[j:i] in word_set:
                # Add `j` as a valid predecessor for `i`
                predecessors[i].append(j)
                # We do NOT break here, to find all possible splits

    # --- Phase 2: Reconstruct all paths using backtracking ---
    all_decompositions = []
    
    def build_paths(end_index, current_path):
        """
        Recursively builds paths by backtracking from the end_index
        """
        # Base Case: If we've reached the start, a valid path is complete
        if end_index == 0:
            # Add a reversed copy of the found path to our results
            all_decompositions.append(current_path[::-1])
            return

        # Recursive Step: Explore all predecessors for the current end_index
        for start_index in predecessors[end_index]:
            # Get the word for the current segment
            word = domain[start_index:end_index]
            # Add the word to the path and recurse
            current_path.append(word)
            build_paths(start_index, current_path)
            # Backtrack: remove the word to explore other branches
            current_path.pop()

    # Start the path-building process from the end of the domain
    build_paths(len(domain), [])
    
    return all_decompositions

# Example Usage
s = "catsanddog"
dictionary = {"cat", "cats", "and", "sand", "dog"}
all_paths = decompose_into_all_paths(s, dictionary)

print(f"All decompositions for '{s}':")
for path in all_paths:
    print(path)
# Expected Output:
# ['cat', 'sand', 'dog']
# ['cats', 'and', 'dog']