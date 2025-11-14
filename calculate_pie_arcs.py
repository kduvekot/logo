#!/usr/bin/env python3
"""Calculate pie-shaped arc elements for blue boxes"""

import math

# Diagonal line equations
top_diagonal_slope = -0.476
top_diagonal_intercept = -53.2

bottom_diagonal_slope = -0.486
bottom_diagonal_intercept = 52.6

# Current blue box positions (after repositioning)
lower_box = {
    "top_left": (-116.5, 61.59),
    "top_right": (-18.5, 61.59),
    "width": 98
}

upper_box = {
    "bottom_left": (22.5, -63.91),
    "bottom_right": (119.5, -63.91),
    "width": 97
}

def circle_line_intersection(center_x, center_y, radius, slope, intercept):
    """Find intersection of circle and line y = mx + b"""
    # Circle: (x - cx)² + (y - cy)² = r²
    # Line: y = mx + b
    # Substitute: (x - cx)² + (mx + b - cy)² = r²

    a = 1 + slope**2
    b_coef = 2 * (slope * (intercept - center_y) - center_x)
    c = center_x**2 + (intercept - center_y)**2 - radius**2

    discriminant = b_coef**2 - 4*a*c

    if discriminant < 0:
        return []

    x1 = (-b_coef + math.sqrt(discriminant)) / (2*a)
    x2 = (-b_coef - math.sqrt(discriminant)) / (2*a)

    y1 = slope * x1 + intercept
    y2 = slope * x2 + intercept

    return [(x1, y1), (x2, y2)]

def angle_from_center(center_x, center_y, point_x, point_y):
    """Calculate angle in degrees from center to point"""
    dx = point_x - center_x
    dy = point_y - center_y
    angle = math.degrees(math.atan2(dy, dx))
    return angle

print("=" * 70)
print("BOTTOM BLUE BOX - PIE SHAPED ELEMENT")
print("=" * 70)
print()

# Arc centered at top-right corner
arc_center = lower_box["top_right"]
arc_radius = lower_box["width"]
arc_start = lower_box["top_left"]

print(f"Arc center (top-right corner): {arc_center}")
print(f"Arc radius (box width): {arc_radius}")
print(f"Arc start point (top-left corner): {arc_start}")
print()

# Find intersection with TOP diagonal
intersections = circle_line_intersection(
    arc_center[0], arc_center[1], arc_radius,
    top_diagonal_slope, top_diagonal_intercept
)

print(f"Arc intersections with TOP diagonal (y = {top_diagonal_slope}x + {top_diagonal_intercept}):")
for i, (x, y) in enumerate(intersections, 1):
    angle = angle_from_center(arc_center[0], arc_center[1], x, y)
    dist = math.sqrt((x - arc_center[0])**2 + (y - arc_center[1])**2)
    print(f"  Point {i}: ({x:7.2f}, {y:7.2f}), angle: {angle:6.2f}°, distance: {dist:.2f}")
print()

# Determine which intersection to use
# We start at top-left (-116.5, 61.59) and sweep clockwise
start_angle = angle_from_center(arc_center[0], arc_center[1], arc_start[0], arc_start[1])
print(f"Start angle (from top-left corner): {start_angle:.2f}°")
print()

# Choose the intersection that makes sense geometrically
# Clockwise from 180° goes through 90° (upward), 0° (right), -90° (downward)
valid_intersections = []
for x, y in intersections:
    angle = angle_from_center(arc_center[0], arc_center[1], x, y)
    # Check if this point is in the clockwise sweep from start
    # From 180° clockwise, we go through 90° (up), 0° (right), -90° (down)
    # We want the first intersection going clockwise
    if x < arc_center[0]:  # Left of center
        valid_intersections.append((x, y, angle))
        print(f"Valid intersection for clockwise sweep: ({x:.2f}, {y:.2f}), angle: {angle:.2f}°")

if valid_intersections:
    # Pick the one closest to start angle in clockwise direction
    end_point = valid_intersections[0][:2]
    end_angle = valid_intersections[0][2]

    print()
    print("PIE SHAPE PATH:")
    print(f"  Start: {arc_start} at angle {start_angle:.2f}°")
    print(f"  Arc center: {arc_center}")
    print(f"  Arc end: {end_point} at angle {end_angle:.2f}°")
    print()

    # Calculate arc sweep
    # From 180° to ~60° is about 120° clockwise
    angle_sweep = start_angle - end_angle
    if angle_sweep < 0:
        angle_sweep += 360

    print(f"  Arc sweep: {angle_sweep:.2f}° (clockwise)")
    print(f"  Large arc flag: {1 if angle_sweep > 180 else 0}")
    print(f"  Sweep flag: 1 (clockwise)")
    print()

    # SVG path
    print("SVG PATH for bottom box pie element:")
    print(f'  <path class="blue" d="')
    print(f'    M {arc_center[0]} {arc_center[1]}')
    print(f'    L {arc_start[0]} {arc_start[1]}')
    laf = 1 if angle_sweep > 180 else 0
    print(f'    A {arc_radius} {arc_radius} 0 {laf} 1 {end_point[0]:.2f} {end_point[1]:.2f}')
    print(f'    Z')
    print(f'  "/>')

print()
print("=" * 70)
print("UPPER BLUE BOX - PIE SHAPED ELEMENT")
print("=" * 70)
print()

# Arc centered at bottom-left corner
arc_center = upper_box["bottom_left"]
arc_radius = upper_box["width"]
arc_start = upper_box["bottom_right"]

print(f"Arc center (bottom-left corner): {arc_center}")
print(f"Arc radius (box width): {arc_radius}")
print(f"Arc start point (bottom-right corner): {arc_start}")
print()

# Find intersection with BOTTOM diagonal
intersections = circle_line_intersection(
    arc_center[0], arc_center[1], arc_radius,
    bottom_diagonal_slope, bottom_diagonal_intercept
)

print(f"Arc intersections with BOTTOM diagonal (y = {bottom_diagonal_slope}x + {bottom_diagonal_intercept}):")
for i, (x, y) in enumerate(intersections, 1):
    angle = angle_from_center(arc_center[0], arc_center[1], x, y)
    dist = math.sqrt((x - arc_center[0])**2 + (y - arc_center[1])**2)
    print(f"  Point {i}: ({x:7.2f}, {y:7.2f}), angle: {angle:6.2f}°, distance: {dist:.2f}")
print()

# Determine which intersection to use
start_angle = angle_from_center(arc_center[0], arc_center[1], arc_start[0], arc_start[1])
print(f"Start angle (from bottom-right corner): {start_angle:.2f}°")
print()

# For upper box: start at bottom-right, sweep counter-clockwise (for symmetry)
# Actually, the user said to apply the same logic, so let's think about it
# For lower box: center at top-right, start at top-left, go clockwise
# For upper box by symmetry: center at bottom-left, start at bottom-right, go counter-clockwise
valid_intersections = []
for x, y in intersections:
    angle = angle_from_center(arc_center[0], arc_center[1], x, y)
    # Check if this point is in the counter-clockwise sweep from start
    # From 0° counter-clockwise, we go through 90° (up), 180° (left), -90° (down)
    if x > arc_center[0]:  # Right of center
        valid_intersections.append((x, y, angle))
        print(f"Valid intersection for counter-clockwise sweep: ({x:.2f}, {y:.2f}), angle: {angle:.2f}°")

if valid_intersections:
    # Pick the appropriate one
    end_point = valid_intersections[0][:2]
    end_angle = valid_intersections[0][2]

    print()
    print("PIE SHAPE PATH:")
    print(f"  Start: {arc_start} at angle {start_angle:.2f}°")
    print(f"  Arc center: {arc_center}")
    print(f"  Arc end: {end_point} at angle {end_angle:.2f}°")
    print()

    # Calculate arc sweep
    angle_sweep = end_angle - start_angle
    if angle_sweep < 0:
        angle_sweep += 360

    print(f"  Arc sweep: {angle_sweep:.2f}° (counter-clockwise)")
    print(f"  Large arc flag: {1 if angle_sweep > 180 else 0}")
    print(f"  Sweep flag: 0 (counter-clockwise)")
    print()

    # SVG path
    print("SVG PATH for upper box pie element:")
    print(f'  <path class="blue" d="')
    print(f'    M {arc_center[0]} {arc_center[1]}')
    print(f'    L {arc_start[0]} {arc_start[1]}')
    laf = 1 if angle_sweep > 180 else 0
    print(f'    A {arc_radius} {arc_radius} 0 {laf} 0 {end_point[0]:.2f} {end_point[1]:.2f}')
    print(f'    Z')
    print(f'  "/>')
