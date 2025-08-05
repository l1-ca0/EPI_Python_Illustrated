from typing import List, Iterator, Tuple

def examine_buildings_with_sunset(building_heights: Iterator[int]) -> List[int]:
    """
    Given a sequence of building heights from east to west, this function
    identifies which buildings have an unobstructed view of the sunset to the west.

    Args:
        building_heights: An iterator of integers representing building heights.

    Returns:
        A list of the indices of the buildings that have a sunset view.
    """
    # The stack will store tuples of (index, height) for candidate buildings.
    view_candidates_stack: List[Tuple[int, int]] = []

    for index, height in enumerate(building_heights):
        
        # Check if the current building blocks any previous candidates.
        # We access the height from the tuple using index [1].
        while view_candidates_stack and height >= view_candidates_stack[-1][1]:
            # Pop shorter buildings to the east that are now blocked.
            view_candidates_stack.pop()

        # Add the current building's (index, height) tuple as a new candidate.
        view_candidates_stack.append((index, height))

    # The stack now contains all buildings with a view.
    # We extract their original indices (stored at index [0] of the tuple).
    result_indices = [building[0] for building in view_candidates_stack]
    
    return result_indices