def min_cameras_for_perimeter(arcs, perimeter_length=360):
    """
    Solves the interval covering problem on a circular perimeter

    It works by converting the circular problem into a linear one. Arcs that
    "wrap around" the 0 point are split into two separate linear intervals.
    Then, the standard `find_minimum_visits` function is used.

    Args:
        arcs: A list of (start, end) tuples for each arc
        perimeter_length: The total length of the perimeter (e.g., 360 for degrees)

    Returns:
        The minimum number of cameras (visits) needed
    """
    linear_intervals = []
    for start, end in arcs:
        if start <= end:
            # This is a simple, non-wrapping arc
            linear_intervals.append(Interval(start, end))
        else:
            # This arc wraps around; split it into two
            # e.g., (350, 10) becomes Interval(350, 360) and Interval(0, 10)
            linear_intervals.append(Interval(start, perimeter_length))
            linear_intervals.append(Interval(0, end))
    
    # Use the already solved linear algorithm on the unrolled intervals
    return find_minimum_visits(linear_intervals)

# --- Example Usage ---
# An arc from 350 to 20, an arc from 10 to 30, and an arc from 340 to 15
robot_arcs = [(350, 20), (10, 30), (340, 15)]
num_cameras = min_cameras_for_perimeter(robot_arcs)
print(f"Minimum cameras required: {num_cameras}") # Expected: 2