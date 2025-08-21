def max_visible_points(points, fov_degrees):
    """
    Finds the maximum number of points visible from the origin (0,0) within
    a fixed field-of-view angle

    1. Converts each point's (x, y) coordinate to an angle in degrees
    2. Sorts the angles
    3. Duplicates the angle list (angle + 360) to handle the circular "wrap-around"
    4. Uses a two-pointer sliding window to find the max points in any fov_degrees range

    Args:
        points: A list of (x, y) tuples for each point's location
        fov_degrees: The field-of-view of the observer in degrees

    Returns:
        The maximum number of points that can be seen at once
    """
    if not points:
        return 0
        
    angles = []
    for x, y in points:
        # Convert cartesian coordinates to a polar angle in degrees [0, 360)
        angle = math.degrees(math.atan2(y, x))
        angles.append(angle if angle >= 0 else angle + 360)

    angles.sort()
    
    # Duplicate the angles to handle wrapping around the circle
    # e.g., a window from 350 to 20 degrees
    extended_angles = angles + [angle + 360 for angle in angles]
    
    max_points = 0
    left = 0
    # Use a sliding window (represented by `left` and `right` pointers)
    for right in range(len(extended_angles)):
        # While the current window is wider than the field of view,
        # shrink the window from the left
        while extended_angles[right] - extended_angles[left] > fov_degrees:
            left += 1
        
        # The number of points in the current valid window
        current_points = right - left + 1
        max_points = max(max_points, current_points)
        
    return max_points

# --- Example Usage ---
# Points are placed roughly at 10, 20, 25, 90, 95, 100, and 270 degrees
visible_points = [(math.cos(math.radians(d)), math.sin(math.radians(d))) 
                  for d in [10, 20, 25, 90, 95, 100, 270]]
fov = 20.0 # Field of view is 20 degrees

max_p = max_visible_points(visible_points, fov)

print(f"Field of View: {fov} degrees")
print(f"Maximum visible points: {max_p}") # Expected: 3 (covers 10, 20, 25 or 90, 95, 100)