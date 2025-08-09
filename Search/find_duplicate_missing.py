import collections
from functools import reduce
from typing import List


DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))

def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    """
    Finds the single duplicate and single missing number in an array that
    should contain the numbers from 0 to n-1.

    This is achieved in O(n) time and O(1) space using bitwise XOR.
    """
    
    # --- Step 1: Calculate the XOR sum of the missing and duplicate numbers ---
    # m_xor_d = (XOR of all elements in A) ^ (XOR of all nums from 0 to n-1)
    # This cancels out all numbers that appear once in A and once in the range,
    # leaving just (duplicate ^ missing).
    m_xor_d = reduce(lambda v, i: v ^ i, A, 0)
    for i in range(len(A)):
        m_xor_d ^= i
        
    # --- Step 2: Find a bit that is different between the missing and duplicate ---
    # We need any bit that is 1 in m_xor_d. The least significant bit (LSB)
    # is the easiest to find using this bitwise trick.
    # `differ_bit` will be a number like 000100, with only one bit set.
    differ_bit = m_xor_d & (~(m_xor_d - 1))
    
    # This will hold one of the results (either the missing or duplicate).
    miss_or_dup = 0
    
    # --- Step 3: Partition numbers with the differ_bit and find one number ---
    # Iterate through the input array and the full range of numbers again.
    # This time, we only XOR numbers that have the 'differ_bit' set.
    for i in range(len(A)):
        # Check numbers from the input array.
        if A[i] & differ_bit:
            miss_or_dup ^= A[i]
        # Check numbers from the full range 0..n-1.
        if i & differ_bit:
            miss_or_dup ^= i
            
    # The result 'miss_or_dup' is now either the missing or the duplicate number.
    # We can identify which one it is by checking if it's present in the input array.
    if miss_or_dup in A:
        duplicate_num = miss_or_dup
        # --- Step 4: Find the other number using the result from Step 1 ---
        missing_num = m_xor_d ^ duplicate_num
    else:
        missing_num = miss_or_dup
        duplicate_num = m_xor_d ^ missing_num
        
    return DuplicateAndMissing(duplicate_num, missing_num)