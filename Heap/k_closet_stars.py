import heapq
import math
from typing import List, Iterator

class Star:
    """Represents a star with 3D coordinates."""
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        """
        Calculates the squared Euclidean distance from the origin (0,0,0).
        Note: We use squared distance to avoid costly square root operations.
        The comparison still holds: if d1^2 < d2^2, then d1 < d2.
        """
        return self.x**2 + self.y**2 + self.z**2

    # Define how to represent a Star object as a string for printing.
    def __repr__(self) -> str:
        return f"Star(x={self.x}, y={self.y}, z={self.z})"

def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    """
    Finds the k closest stars to Earth from a stream of stars.

    Args:
        stars: An iterator that yields Star objects.
        k: The number of closest stars to find.

    Returns:
        A list containing the k closest Star objects.
    """
    # max_heap stores tuples of (-distance, star). The negated distance
    # allows our min-heap to function as a max-heap based on distance.
    max_heap = []

    # --- Main processing loop ---
    for star in stars:
        # Calculate the negated distance.
        neg_distance = -star.distance
        
        # If the heap isn't full yet, just add the star.
        if len(max_heap) < k:
            heapq.heappush(max_heap, (neg_distance, star))
        # If the heap is full, check if this star is closer than the
        # farthest star currently in the heap.
        # max_heap[0] is the smallest element, which corresponds to the
        # largest distance because of the negation.
        elif neg_distance > max_heap[0][0]:
            # This star is closer. Use heappushpop to efficiently replace
            # the farthest star with this new one.
            heapq.heappushpop(max_heap, (neg_distance, star))
            
    # The heap now contains the k closest stars. Extract just the Star
    # objects from the tuples to return them.
    return [s[1] for s in max_heap]