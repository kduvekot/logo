#!/usr/bin/env python3
"""Verify pie arc calculation for bottom blue box"""

import math

# Bottom blue box coordinates (after repositioning)
bottom_box = {
    "top_left": (-116.5, 61.59),
    "top_right": (-18.5, 61.59),
    "width": 98
}

# Top diagonal line
top_diagonal_slope = -0.476
top_diagonal_intercept = -53.2

print("=" * 70)
print("BOTTOM BLUE BOX - PIE ARC VERIFICATION")
print("=" * 70)
print()

print("Your description:")
print("1. Arc center: top-right corner of bottom box")
print("2. Arc radius: width of the box")
print("3. Start: top-left corner of bottom box")
print("4. Direction: clockwise")
print("5. End: where arc meets TOP diagonal")
print()

print("=" * 70)
print("CALCULATION")
print("=" * 70)
print()

arc_center = bottom_box["top_right"]
arc_radius = bottom_box["width"]
arc_start = bottom_box["top_left"]

print(f"Arc center (top-right): {arc_center}")
print(f"Arc radius (box width): {arc_radius} pixels")
print(f"Arc start (top-left): {arc_start}")
print()

# Verify that start point is indeed at the radius distance
start_dist = math.sqrt((arc_start[0] - arc_center[0])**2 + (arc_start[1] - arc_center[1])**2)
print(f"Distance from center to start: {start_dist:.2f} pixels")
print(f"  ✓ Matches radius: {abs(start_dist - arc_radius) < 0.01}")
print()

# Find intersection with top diagonal
# Circle: (x - cx)² + (y - cy)² = r²
# Line: y = mx + b
def circle_line_intersection(cx, cy, r, m, b):
    """Find where circle intersects line y = mx + b"""
    # (x - cx)² + (mx + b - cy)² = r²
    # Expand: x² - 2cx*x + cx² + m²x² + 2m(b-cy)x + (b-cy)² = r²
    # (1 + m²)x² + (2m(b-cy) - 2cx)x + (cx² + (b-cy)² - r²) = 0

    a = 1 + m**2
    b_coef = 2 * (m * (b - cy) - cx)
    c = cx**2 + (b - cy)**2 - r**2

    discriminant = b_coef**2 - 4*a*c

    if discriminant < 0:
        return []

    x1 = (-b_coef + math.sqrt(discriminant)) / (2*a)
    x2 = (-b_coef - math.sqrt(discriminant)) / (2*a)

    y1 = m * x1 + b
    y2 = m * x2 + b

    return [(x1, y1), (x2, y2)]

intersections = circle_line_intersection(
    arc_center[0], arc_center[1], arc_radius,
    top_diagonal_slope, top_diagonal_intercept
)

print(f"Intersection with TOP diagonal (y = {top_diagonal_slope}x + {top_diagonal_intercept}):")
for i, (x, y) in enumerate(intersections, 1):
    angle_rad = math.atan2(y - arc_center[1], x - arc_center[0])
    angle_deg = math.degrees(angle_rad)
    dist = math.sqrt((x - arc_center[0])**2 + (y - arc_center[1])**2)
    print(f"  Point {i}: ({x:8.2f}, {y:8.2f})")
    print(f"           Angle from center: {angle_deg:7.2f}°")
    print(f"           Distance: {dist:.2f} pixels")
    print()

# Determine which intersection point when going clockwise from start
start_angle = math.degrees(math.atan2(arc_start[1] - arc_center[1], arc_start[0] - arc_center[0]))
print(f"Start angle (from top-left): {start_angle:.2f}°")
print()

print("Clockwise direction from 180°:")
print("  180° → 90° (upward) → 0° (right) → -90° (downward) → -180°")
print()

# Choose the correct intersection
print("Evaluating which intersection point to use:")
for i, (x, y) in enumerate(intersections, 1):
    angle = math.degrees(math.atan2(y - arc_center[1], x - arc_center[0]))

    # Clockwise from 180° goes: 180 -> 90 -> 0 -> -90 -> -180
    # We want the first intersection encountered going clockwise

    if x < arc_center[0]:  # Left of center (in the left half)
        print(f"  Point {i} at ({x:.2f}, {y:.2f}), angle {angle:.2f}°")
        print(f"    This point is LEFT of center (x < {arc_center[0]})")

        # Going clockwise from 180°, we'd encounter this
        # Calculate the clockwise angle from start
        angle_diff = start_angle - angle
        if angle_diff < 0:
            angle_diff += 360
        print(f"    Clockwise sweep from start: {angle_diff:.2f}°")

print()
print("=" * 70)
print("RECOMMENDED PIE SHAPE")
print("=" * 70)
print()

# Use the first intersection (more negative angle = further clockwise from 180°)
end_point = intersections[0]  # This should be (-40.55, -33.90)
end_angle = math.degrees(math.atan2(end_point[1] - arc_center[1], end_point[0] - arc_center[0]))

sweep_angle = start_angle - end_angle
if sweep_angle < 0:
    sweep_angle += 360

print(f"Start: {arc_start} (angle: {start_angle:.2f}°)")
print(f"End: ({end_point[0]:.2f}, {end_point[1]:.2f}) (angle: {end_angle:.2f}°)")
print(f"Sweep: {sweep_angle:.2f}° clockwise")
print()

large_arc_flag = 1 if sweep_angle > 180 else 0
sweep_flag = 1  # Clockwise

print("SVG Path for pie shape:")
print(f"  M {arc_center[0]} {arc_center[1]}        (move to center)")
print(f"  L {arc_start[0]} {arc_start[1]}        (line to start)")
print(f"  A {arc_radius} {arc_radius} 0 {large_arc_flag} {sweep_flag} {end_point[0]:.2f} {end_point[1]:.2f}  (arc)")
print(f"  Z                                 (close path)")
print()

print("Complete SVG element:")
print(f'<path class="pie-preview" d="')
print(f'  M {arc_center[0]} {arc_center[1]}')
print(f'  L {arc_start[0]} {arc_start[1]}')
print(f'  A {arc_radius} {arc_radius} 0 {large_arc_flag} {sweep_flag} {end_point[0]:.2f} {end_point[1]:.2f}')
print(f'  Z')
print(f'"/>')
