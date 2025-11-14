#!/usr/bin/env python3
"""Calculate upper box pie shape using same perpendicular logic"""

import math

# Upper blue box bottom-left corner (center for pie)
point = (22.5, -63.91)

# Diagonal line equations
top_diagonal_slope = -0.476
top_diagonal_intercept = -53.2

bottom_diagonal_slope = -0.486
bottom_diagonal_intercept = 52.6

print("=" * 70)
print("UPPER BOX PIE CALCULATION (mirrored from bottom)")
print("=" * 70)
print()

print(f"Starting point (bottom-left of upper box): {point}")
print(f"This should be where top diagonal crosses")
print()

# Verify the point is on top diagonal
y_check = top_diagonal_slope * point[0] + top_diagonal_intercept
print(f"Verification: At x = {point[0]}")
print(f"  Top diagonal y = {y_check:.2f}")
print(f"  Actual point y = {point[1]}")
print(f"  Match: {abs(y_check - point[1]) < 11}")
print()

print("=" * 70)
print("PERPENDICULAR LINE TO BOTTOM DIAGONAL")
print("=" * 70)
print()

# Perpendicular slope to BOTTOM diagonal (mirrored from bottom box)
perp_slope = -1 / bottom_diagonal_slope
print(f"Bottom diagonal slope: {bottom_diagonal_slope}")
print(f"Perpendicular slope: {perp_slope:.6f}")
print()

# Perpendicular line through point
perp_intercept = point[1] - perp_slope * point[0]
print(f"Perpendicular line equation:")
print(f"  y = {perp_slope:.6f}x + {perp_intercept:.6f}")
print()

print("=" * 70)
print("INTERSECTION WITH BOTTOM DIAGONAL")
print("=" * 70)
print()

# Find intersection with bottom diagonal
x_intersect = (bottom_diagonal_intercept - perp_intercept) / (perp_slope - bottom_diagonal_slope)
y_intersect = bottom_diagonal_slope * x_intersect + bottom_diagonal_intercept

print(f"Intersection of perpendicular with BOTTOM diagonal:")
print(f"  Point: ({x_intersect:.2f}, {y_intersect:.2f})")
print()

# Calculate distance
distance = math.sqrt((x_intersect - point[0])**2 + (y_intersect - point[1])**2)
print(f"Distance from start point to intersection: {distance:.2f} pixels")
print()

# Calculate angle from arc center
angle = math.degrees(math.atan2(y_intersect - point[1], x_intersect - point[0]))
print(f"Angle from arc center ({point}) to intersection:")
print(f"  {angle:.2f}°")
print()

arc_radius = 97  # width of upper box
print(f"Arc radius (upper box width): {arc_radius} pixels")
print(f"Perpendicular distance: {distance:.2f} pixels")
print(f"Difference: {abs(distance - arc_radius):.2f} pixels")
print()

print("=" * 70)
print("UPPER BOX PIE SHAPE")
print("=" * 70)
print()

arc_center = point
arc_start = (119.5, -63.91)  # bottom-right corner
arc_end = (x_intersect, y_intersect)

print(f"Arc center (bottom-left): {arc_center}")
print(f"Arc start (bottom-right): {arc_start}")
print(f"Arc end (perpendicular intersection): ({arc_end[0]:.2f}, {arc_end[1]:.2f})")
print(f"Arc radius: {arc_radius} pixels")
print()

# Calculate arc sweep
start_angle = math.degrees(math.atan2(arc_start[1] - arc_center[1], arc_start[0] - arc_center[0]))
end_angle = math.degrees(math.atan2(arc_end[1] - arc_center[1], arc_end[0] - arc_center[0]))

print(f"Start angle: {start_angle:.2f}°")
print(f"End angle: {end_angle:.2f}°")
print()

# For symmetry with bottom box, we want an outward bulging arc
# Bottom box goes from 180° with sweep flag 1 (clockwise)
# Upper box should go from 0° with sweep flag 1 (clockwise)

sweep_cw = start_angle - end_angle
if sweep_cw < 0:
    sweep_cw += 360

sweep_ccw = end_angle - start_angle
if sweep_ccw < 0:
    sweep_ccw += 360

print(f"Clockwise sweep: {sweep_cw:.2f}°")
print(f"Counter-clockwise sweep: {sweep_ccw:.2f}°")
print()

# For outward bulging pizza slice, use the larger sweep with flag 1
large_arc_flag = 0  # Since we expect small angle
sweep_flag = 1  # Outward bulging (clockwise in SVG)

print("SVG PATH:")
print(f'  <path class="pie-preview" d="')
print(f'    M {arc_center[0]} {arc_center[1]}')
print(f'    L {arc_start[0]} {arc_start[1]}')
print(f'    A {arc_radius} {arc_radius} 0 {large_arc_flag} {sweep_flag} {arc_end[0]:.2f} {arc_end[1]:.2f}')
print(f'    Z')
print(f'  "/>')
print()

print("=" * 70)
print("SYMMETRY CHECK")
print("=" * 70)
print()

print("Bottom box pie:")
print(f"  Center: (-18.5, 61.59)")
print(f"  Start: (-116.5, 61.59)")
print(f"  End: (-60.33, -24.48)")
print(f"  Radius: 98")
print()

print("Upper box pie:")
print(f"  Center: {arc_center}")
print(f"  Start: {arc_start}")
print(f"  End: ({arc_end[0]:.2f}, {arc_end[1]:.2f})")
print(f"  Radius: {arc_radius}")
print()

# Check symmetry about y=0
print("Symmetry about y=0:")
print(f"  Bottom center y: 61.59, Upper center y: {arc_center[1]:.2f}")
print(f"    Mirror match: {abs(61.59 + arc_center[1]) < 5}")
