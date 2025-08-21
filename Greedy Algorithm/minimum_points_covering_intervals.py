import collections
import operator
import math

Interval = collections.namedtuple('Interval', ('left', 'right'))

def find_minimum_visits(intervals):
    """
    Finds the minimum number of visits to cover all given intervals

    The greedy strategy is to sort intervals by their right (end) points.
    We place a visit at the right endpoint of the first interval. This covers
    the first interval and potentially others. We then iterate and find the
    next interval that is NOT covered by our last visit, and repeat the process.

    Args:
        intervals: A list of Interval namedtuples

    Returns:
        The minimum number of visits required
    """
    if not intervals:
        return 0

    # Sort intervals based on their right endpoints in ascending order
    # This is the core of the greedy strategy
    intervals.sort(key=operator.attrgetter('right'))

    last_visit_time = float('-inf')
    num_visits = 0

    # Iterate through the intervals sorted by when they finish
    for interval in intervals:
        # If the interval starts after our last visit, it's not covered
        if interval.left > last_visit_time:
            # We must place a new visit to cover this interval
            # We choose its right endpoint, as this is the greedy choice that
            # maximizes our chance of covering future intervals
            last_visit_time = interval.right
            num_visits += 1
            
    return num_visits

# --- Example Usage ---
tasks = [Interval(0, 3), Interval(2, 6), Interval(3, 4), Interval(6, 9)]
min_visits = find_minimum_visits(tasks)

print(f"Minimum visits required: {min_visits}") # Expected: 2 (at times 3 and 9, or 4 and 9 etc)