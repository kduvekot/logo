#!/usr/bin/env python3
"""Verify by calculating perpendicular line from bottom to top diagonal"""

import math

# Bottom blue box top-right corner (where bottom diagonal crosses)
point = (-18.5, 61.59)

# Diagonal line equations
top_diagonal_slope = -0.476
top_diagonal_intercept = -53.2

bottom_diagonal_slope = -0.486
bottom_diagonal_intercept = 52.6

print("=" * 70)
print("PERPENDICULAR LINE VERIFICATION")
print("=" * 70)
print()

print(f"Starting point (top-right of bottom box): {point}")
print(f"This should be where bottom diagonal crosses: y = {bottom_diagonal_slope}x + {bottom_diagonal_intercept}")
print()

# Verify the point is on bottom diagonal
y_check = bottom_diagonal_slope * point[0] + bottom_diagonal_intercept
print(f"Verification: At x = {point[0]}")
print(f"  Bottom diagonal y = {y_check:.2f}")
print(f"  Actual point y = {point[1]}")
print(f"  Match: {abs(y_check - point[1]) < 0.1}")
print()

print("=" * 70)
print("PERPENDICULAR LINE CALCULATION")
print("=" * 70)
print()

# Perpendicular slope to bottom diagonal
perp_slope = -1 / bottom_diagonal_slope
print(f"Bottom diagonal slope: {bottom_diagonal_slope}")
print(f"Perpendicular slope: {perp_slope:.6f}")
print()

# Perpendicular line through point: y - y0 = m(x - x0)
# y = mx - mx0 + y0
perp_intercept = point[1] - perp_slope * point[0]
print(f"Perpendicular line equation:")
print(f"  y = {perp_slope:.6f}x + {perp_intercept:.6f}")
print()

print("=" * 70)
print("INTERSECTION WITH TOP DIAGONAL")
print("=" * 70)
print()

# Find intersection with top diagonal
# perp_slope * x + perp_intercept = top_diagonal_slope * x + top_diagonal_intercept
# (perp_slope - top_diagonal_slope) * x = top_diagonal_intercept - perp_intercept

x_intersect = (top_diagonal_intercept - perp_intercept) / (perp_slope - top_diagonal_slope)
y_intersect = top_diagonal_slope * x_intersect + top_diagonal_intercept

print(f"Intersection of perpendicular with TOP diagonal:")
print(f"  Point: ({x_intersect:.2f}, {y_intersect:.2f})")
print()

# Calculate distance
distance = math.sqrt((x_intersect - point[0])**2 + (y_intersect - point[1])**2)
print(f"Distance from start point to intersection: {distance:.2f} pixels")
print()

# Calculate angle from arc center
arc_center = point
angle = math.degrees(math.atan2(y_intersect - point[1], x_intersect - point[0]))
print(f"Angle from arc center ({point}) to intersection:")
print(f"  {angle:.2f}°")
print()

print("=" * 70)
print("COMPARE WITH ARC RADIUS")
print("=" * 70)
print()

arc_radius = 98  # width of bottom box
print(f"Arc radius (box width): {arc_radius} pixels")
print(f"Perpendicular distance: {distance:.2f} pixels")
print(f"Match: {abs(distance - arc_radius) < 1}")
print()

if abs(distance - arc_radius) < 1:
    print("✓✓✓ PERFECT MATCH!")
    print()
    print("The perpendicular line distance equals the arc radius!")
    print("This means the arc endpoint SHOULD be at the perpendicular intersection!")
    print()
    print(f"Expected arc endpoint: ({x_intersect:.2f}, {y_intersect:.2f})")
else:
    print(f"Distance differs by {abs(distance - arc_radius):.2f} pixels")
    print("The arc intersection might not be at the perpendicular point.")

print()
print("=" * 70)
print("COMPARING WITH CALCULATED ARC INTERSECTIONS")
print("=" * 70)
print()

# Previously calculated intersections
arc_intersections = [
    (-40.55, -33.90, 76.99),  # Point 1, 77° arc
    (-78.70, -15.74, 52.10)   # Point 2, 52° arc
]

print("Previously calculated arc/diagonal intersections:")
for i, (x, y, arc_deg) in enumerate(arc_intersections, 1):
    dist_to_perp = math.sqrt((x - x_intersect)**2 + (y - y_intersect)**2)
    print(f"  Point {i}: ({x:.2f}, {y:.2f}), {arc_deg:.0f}° arc")
    print(f"    Distance to perpendicular point: {dist_to_perp:.2f} pixels")
    if dist_to_perp < 5:
        print(f"    ✓ VERY CLOSE MATCH!")
    print()

print("=" * 70)
print("RECOMMENDATION")
print("=" * 70)
print()

# Find which arc intersection is closest to perpendicular intersection
min_dist = float('inf')
best_point = None
for x, y, arc_deg in arc_intersections:
    dist = math.sqrt((x - x_intersect)**2 + (y - y_intersect)**2)
    if dist < min_dist:
        min_dist = dist
        best_point = (x, y, arc_deg)

if best_point and min_dist < 5:
    print(f"Use arc intersection at ({best_point[0]:.2f}, {best_point[1]:.2f})")
    print(f"Arc sweep: {best_point[2]:.0f}° counter-clockwise")
    print(f"This is closest to the perpendicular intersection point.")
else:
    print(f"Neither arc intersection is close to perpendicular point.")
    print(f"Perpendicular intersection: ({x_intersect:.2f}, {y_intersect:.2f})")
