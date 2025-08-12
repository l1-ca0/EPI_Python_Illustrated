def generate_permutations_recursive(A):
    permutations = []

    def find_permutations(start_index):
        # Base case: if our starting index is at the end of the array,
        # we have a complete permutation
        if start_index == len(A) - 1:
            # Add a copy of the current state of A to our results
            permutations.append(list(A))
            return

        # For the subarray starting at 'start_index',
        # try placing each of its elements in the first position
        for i in range(start_index, len(A)):
            # 1- CHOOSE: Swap the current element with the one at start_index
            A[start_index], A[i] = A[i], A[start_index]
            
            # 2- EXPLORE: Recurse to generate all permutations for the rest of the array
            find_permutations(start_index + 1)
            
            # 3- UN-CHOOSE (Backtrack): Swap them back to restore the original order
            # This is crucial so we can try the next element in the loop correctly
            A[start_index], A[i] = A[i], A[start_index]

    # Start the process from the beginning of the array (index 0)
    find_permutations(0)
    return permutations
