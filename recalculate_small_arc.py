#!/usr/bin/env python3
"""Recalculate with focus on small arc sweep"""

import math

# Bottom blue box
bottom_box = {
    "top_left": (-116.5, 61.59),
    "top_right": (-18.5, 61.59),
    "width": 98
}

# Top diagonal
top_diagonal_slope = -0.476
top_diagonal_intercept = -53.2

arc_center = bottom_box["top_right"]
arc_radius = bottom_box["width"]

print("=" * 70)
print("RECONSIDERING THE ARC")
print("=" * 70)
print()

print("Given:")
print(f"  Arc center: {arc_center}")
print(f"  Arc radius: {arc_radius}")
print()

print("User constraint: Arc should be 45-90° and not extend left of x = -116.5")
print()

# Let's explore different starting points
print("Checking: What if the arc DOESN'T start at the actual top-left corner?")
print()

# Find ALL intersections with the top diagonal
def circle_line_intersection(cx, cy, r, m, b):
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

print("Intersection points with top diagonal:")
for i, (x, y) in enumerate(intersections, 1):
    angle = math.degrees(math.atan2(y - arc_center[1], x - arc_center[0]))
    print(f"  Point {i}: ({x:7.2f}, {y:7.2f}), angle: {angle:7.2f}°")

print()

# What if we need to find where a vertical line at x=-116.5 intersects the arc?
print("What if the arc should start where x = -116.5 intersects the circle?")
print()

# Circle: (x - cx)² + (y - cy)² = r²
# At x = -116.5: (-116.5 - (-18.5))² + (y - 61.59)² = 98²
# (-98)² + (y - 61.59)² = 98²
# (y - 61.59)² = 0
# y = 61.59

print(f"At x = -116.5:")
x_check = -116.5
y_squared = arc_radius**2 - (x_check - arc_center[0])**2
if y_squared >= 0:
    y1 = arc_center[1] + math.sqrt(y_squared)
    y2 = arc_center[1] - math.sqrt(y_squared)
    print(f"  y = {y1:.2f} or y = {y2:.2f}")
    angle1 = math.degrees(math.atan2(y1 - arc_center[1], x_check - arc_center[0]))
    angle2 = math.degrees(math.atan2(y2 - arc_center[1], x_check - arc_center[0]))
    print(f"  Upper point: ({x_check}, {y1:.2f}), angle: {angle1:.2f}°")
    print(f"  Lower point: ({x_check}, {y2:.2f}), angle: {angle2:.2f}°")
else:
    print(f"  No intersection! x = -116.5 is outside the circle.")

print()
print("WAIT - The current top-left corner IS on the circle!")
print("So if we start at (-116.5, 61.59) at 180°...")
print()

# Maybe I should consider counter-clockwise instead?
print("What if 'clockwise' means the other direction in SVG coordinates?")
print("In SVG, Y increases downward, so 'clockwise' might be different...")
print()

# Or maybe the diagonal intersection should be calculated differently?
print("Let me check: could the 'small arc' mean we should use the closer")
print("intersection point measured along the arc perimeter?")
print()

start_angle = 180.0
for i, (x, y) in enumerate(intersections, 1):
    end_angle = math.degrees(math.atan2(y - arc_center[1], x - arc_center[0]))

    # Calculate both clockwise and counter-clockwise sweeps
    cw_sweep = start_angle - end_angle
    if cw_sweep < 0:
        cw_sweep += 360

    ccw_sweep = end_angle - start_angle
    if ccw_sweep < 0:
        ccw_sweep += 360

    print(f"To Point {i} at ({x:.2f}, {y:.2f}):")
    print(f"  Clockwise sweep: {cw_sweep:.2f}°")
    print(f"  Counter-clockwise sweep: {ccw_sweep:.2f}°")
    print(f"  Minimum sweep: {min(cw_sweep, ccw_sweep):.2f}°")
    print()
