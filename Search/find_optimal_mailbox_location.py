import collections
import random
from typing import List

# Use a namedtuple to store building data.
Building = collections.namedtuple('Building', ('position', 'residents'))

def find_optimal_mailbox_location(buildings: List[Building]) -> float:
    """
    Finds the optimal mailbox location to minimize total resident travel distance.
    This is the weighted median of the building positions.

    The algorithm uses a modified Quickselect to find the weighted median in
    O(n) average time and O(n) space for the recursive partitioning.

    Args:
        buildings: A list of Building objects, each with a position and residents.

    Returns:
        The optimal position (a float) for the mailbox.
    """
    if not buildings:
        raise ValueError("Building list cannot be empty.")
    
    # Calculate the total number of residents.
    total_residents = sum(b.residents for b in buildings)
    # The median is the resident at the halfway point of the total population.
    median_weight_target = total_residents / 2.0

    # We will recursively (or iteratively) narrow down the list of buildings
    # until we find the one containing the median resident.
    while True:
        # Step 1: Choose a random building as the pivot.
        pivot = random.choice(buildings)
        
        # Step 2: Partition the buildings and sum their weights.
        less, equal, greater = [], [], []
        weight_less = 0
        weight_equal = 0
        
        for b in buildings:
            if b.position < pivot.position:
                less.append(b)
                weight_less += b.residents
            elif b.position > pivot.position:
                greater.append(b)
            else: # b.position == pivot.position
                equal.append(b)
                weight_equal += b.residents
                
        # Step 3: Check where the median resident falls.
        if weight_less < median_weight_target and \
           (weight_less + weight_equal) >= median_weight_target:
            # The median resident lives in one of the buildings at the pivot's
            # location. We've found the optimal spot.
            return pivot.position
        elif weight_less >= median_weight_target:
            # The median must be in the 'less' group. Discard the other groups
            # and repeat the process on this smaller list.
            buildings = less
        else: # The median is in the 'greater' group.
            # Discard the 'less' and 'equal' groups and repeat.
            # We must also adjust our target weight to reflect the residents
            # we've discarded.
            median_weight_target -= (weight_less + weight_equal)
            buildings = greater

# --- Example Usage ---
if __name__ == '__main__':
    # Buildings are at positions 10, 20, 30, 40
    # with 1, 5, 2, and 4 residents respectively.
    building_list = [
        Building(position=10, residents=1),
        Building(position=20, residents=5),
        Building(position=30, residents=2),
        Building.fromkeys(['position', 'residents'], 40, 4)
    ]

    # Total residents = 1 + 5 + 2 + 4 = 12
    # Median resident target = 12 / 2 = 6
    # - Building at pos 10: cumulative residents = 1
    # - Building at pos 20: cumulative residents = 1 + 5 = 6
    # The median resident is in the building at position 20.
    
    optimal_location = find_optimal_mailbox_location(building_list)
    print(f"The optimal mailbox location is at position: {optimal_location}")
    # Expected Output: The optimal mailbox location is at position: 20