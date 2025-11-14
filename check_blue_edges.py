#!/usr/bin/env python3
"""Check if diagonal-inner circle intersections match blue rect edges"""

import math

# Inner circle radius
inner_radius = 163

# Blue rectangle edges (from the SVG)
# Upper rect: x="22.5" width="97" → left: 22.5, right: 119.5
# Lower rect: x="-116.5" width="98" → left: -116.5, right: -18.5

blue_rect_edges = {
    "Upper rect left": 22.5,
    "Upper rect right": 119.5,
    "Lower rect left": -116.5,
    "Lower rect right": -18.5
}

# Diagonal intersections with inner circle (from our analysis)
diagonal_inner_intersections = [
    ("Top diagonal, left", -161.28, 23.59),
    ("Top diagonal, right", 119.99, -110.32),
    ("Bottom diagonal, left", -119.56, 110.79),
    ("Bottom diagonal, right", 160.97, -25.63)
]

print("=" * 70)
print("CHECKING BLUE RECTANGLE EDGES vs INNER CIRCLE")
print("=" * 70)
print()

for name, x in blue_rect_edges.items():
    if abs(x) < inner_radius:
        y = math.sqrt(inner_radius**2 - x**2)
        print(f"{name:20s} (x={x:7.1f}):")
        print(f"  Inner circle intersections: ({x:7.1f}, {y:7.2f}) and ({x:7.1f}, {-y:7.2f})")
    else:
        print(f"{name:20s} (x={x:7.1f}): Outside inner circle!")
    print()

print("=" * 70)
print("DIAGONAL INTERSECTIONS WITH INNER CIRCLE")
print("=" * 70)
print()

for name, x, y in diagonal_inner_intersections:
    print(f"{name:25s}: ({x:8.2f}, {y:8.2f})")
print()

print("=" * 70)
print("COMPARISON - Finding Matches")
print("=" * 70)
print()

# Check each diagonal intersection against blue rect edges
for diag_name, diag_x, diag_y in diagonal_inner_intersections:
    print(f"\n{diag_name}: ({diag_x:.2f}, {diag_y:.2f})")

    best_match = None
    min_distance = float('inf')

    for rect_name, rect_x in blue_rect_edges.items():
        if abs(rect_x) < inner_radius:
            rect_y_pos = math.sqrt(inner_radius**2 - rect_x**2)
            rect_y_neg = -rect_y_pos

            # Check distance to both intersection points
            dist_pos = math.sqrt((diag_x - rect_x)**2 + (diag_y - rect_y_pos)**2)
            dist_neg = math.sqrt((diag_x - rect_x)**2 + (diag_y - rect_y_neg)**2)

            dist = min(dist_pos, dist_neg)
            y_match = rect_y_pos if dist_pos < dist_neg else rect_y_neg

            if dist < min_distance:
                min_distance = dist
                best_match = (rect_name, rect_x, y_match, dist)

    if best_match:
        rect_name, rect_x, rect_y, dist = best_match
        print(f"  Closest match: {rect_name} at ({rect_x:.1f}, {rect_y:.2f})")
        print(f"  Distance: {dist:.2f} pixels")
        print(f"  X difference: {abs(diag_x - rect_x):.2f}")
        print(f"  Y difference: {abs(diag_y - rect_y):.2f}")

        if dist < 5:
            print(f"  ✓ VERY CLOSE MATCH!")
        elif dist < 10:
            print(f"  ✓ Close match")

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

matches = []

# Upper rect right edge (119.5)
upper_right_y = math.sqrt(163**2 - 119.5**2)
print(f"Upper blue rect RIGHT edge at x=119.5:")
print(f"  Inner circle: (119.5, ±{upper_right_y:.2f})")
print(f"  Top diagonal: (119.99, -110.32)")
print(f"  Match? X diff = {abs(119.99-119.5):.2f}, Y diff = {abs(-110.32-(-upper_right_y)):.2f}")
if abs(119.99-119.5) < 1 and abs(-110.32-(-upper_right_y)) < 1:
    print(f"  ✓✓✓ EXCELLENT MATCH!")
    matches.append("Upper rect right edge ≈ Top diagonal intersection")
print()

# Lower rect left edge (-116.5)
lower_left_y_pos = math.sqrt(163**2 - 116.5**2)
print(f"Lower blue rect LEFT edge at x=-116.5:")
print(f"  Inner circle: (-116.5, ±{lower_left_y_pos:.2f})")
print(f"  Bottom diagonal: (-119.56, 110.79)")
print(f"  Match? X diff = {abs(-119.56-(-116.5)):.2f}, Y diff = {abs(110.79-lower_left_y_pos):.2f}")
if abs(-119.56-(-116.5)) < 5 and abs(110.79-lower_left_y_pos) < 5:
    print(f"  ✓✓ CLOSE MATCH!")
    matches.append("Lower rect left edge ≈ Bottom diagonal intersection")
print()

if matches:
    print("CONFIRMED MATCHES:")
    for i, match in enumerate(matches, 1):
        print(f"  {i}. {match}")
