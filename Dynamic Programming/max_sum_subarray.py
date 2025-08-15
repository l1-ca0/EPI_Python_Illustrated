def find_maximum_subarray(A):
    # min_sum stores the minimum prefix sum seen so far
    # max_sum stores the overall maximum subarray sum found
    min_sum = max_sum = 0
    
    # itertools.accumulate(A) generates the prefix sums one by one
    for running_sum in itertools.accumulate(A):
        
        # Update min_sum with the smallest prefix sum encountered
        min_sum = min(min_sum, running_sum)
        
        # The current best sum is the current prefix sum minus the
        # smallest prefix sum we've seen
        max_sum = max(max_sum, running_sum - min_sum)
        
    return max_sum