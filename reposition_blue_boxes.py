#!/usr/bin/env python3
"""Analyze and reposition blue boxes to align with diagonals"""

import math

# Diagonal line equations
top_slope = -0.476
top_intercept = -53.2

bottom_slope = -0.486
bottom_intercept = 52.6

# Current blue rectangles (from SVG)
upper_rect = {
    "x": 22.5,
    "y": -272,
    "width": 97,
    "height": 195
}

lower_rect = {
    "x": -116.5,
    "y": 74,
    "width": 98,
    "height": 206
}

# Outer circle radius
outer_radius = 260

print("=" * 70)
print("CURRENT BLUE RECTANGLES")
print("=" * 70)
print()

print("UPPER RECTANGLE:")
print(f"  Position: x={upper_rect['x']}, y={upper_rect['y']}")
print(f"  Size: width={upper_rect['width']}, height={upper_rect['height']}")
print(f"  Left edge: x = {upper_rect['x']}")
print(f"  Right edge: x = {upper_rect['x'] + upper_rect['width']}")
print(f"  Top edge: y = {upper_rect['y']}")
print(f"  Bottom edge: y = {upper_rect['y'] + upper_rect['height']}")
print(f"  Inner lower left corner: ({upper_rect['x']}, {upper_rect['y'] + upper_rect['height']})")
print()

print("LOWER RECTANGLE:")
print(f"  Position: x={lower_rect['x']}, y={lower_rect['y']}")
print(f"  Size: width={lower_rect['width']}, height={lower_rect['height']}")
print(f"  Left edge: x = {lower_rect['x']}")
print(f"  Right edge: x = {lower_rect['x'] + lower_rect['width']}")
print(f"  Top edge: y = {lower_rect['y']}")
print(f"  Bottom edge: y = {lower_rect['y'] + lower_rect['height']}")
print(f"  Top right corner: ({lower_rect['x'] + lower_rect['width']}, {lower_rect['y']})")
print()

print("=" * 70)
print("CALCULATING DIAGONAL INTERSECTIONS")
print("=" * 70)
print()

# For upper rect: inner lower left corner at x=22.5 should touch top diagonal
upper_left_x = upper_rect['x']
target_y_upper = top_slope * upper_left_x + top_intercept
print(f"UPPER BOX - Inner lower left corner should touch top diagonal:")
print(f"  At x = {upper_left_x}")
print(f"  Top diagonal y = {top_slope} * {upper_left_x} + {top_intercept} = {target_y_upper:.2f}")
print(f"  Current bottom edge: y = {upper_rect['y'] + upper_rect['height']}")
print(f"  Need to move: {target_y_upper - (upper_rect['y'] + upper_rect['height']):.2f} pixels")
print()

# For lower rect: top right corner at x=-18.5 should touch bottom diagonal
lower_right_x = lower_rect['x'] + lower_rect['width']
target_y_lower = bottom_slope * lower_right_x + bottom_intercept
print(f"LOWER BOX - Top right corner should touch bottom diagonal:")
print(f"  At x = {lower_right_x}")
print(f"  Bottom diagonal y = {bottom_slope} * {lower_right_x} + {bottom_intercept} = {target_y_lower:.2f}")
print(f"  Current top edge: y = {lower_rect['y']}")
print(f"  Need to move: {target_y_lower - lower_rect['y']:.2f} pixels")
print()

print("=" * 70)
print("NEW RECTANGLE POSITIONS")
print("=" * 70)
print()

# Calculate new positions
upper_vertical_shift = target_y_upper - (upper_rect['y'] + upper_rect['height'])
new_upper_y = upper_rect['y'] + upper_vertical_shift
new_upper_bottom = new_upper_y + upper_rect['height']

lower_vertical_shift = target_y_lower - lower_rect['y']
new_lower_y = lower_rect['y'] + lower_vertical_shift
new_lower_bottom = new_lower_y + lower_rect['height']

print("UPPER RECTANGLE (after vertical adjustment):")
print(f"  New y: {new_upper_y:.2f}")
print(f"  Top edge: y = {new_upper_y:.2f}")
print(f"  Bottom edge: y = {new_upper_bottom:.2f} (should be {target_y_upper:.2f})")
print(f"  Inner lower left: ({upper_left_x}, {new_upper_bottom:.2f})")
print()

print("LOWER RECTANGLE (after vertical adjustment):")
print(f"  New y: {new_lower_y:.2f}")
print(f"  Top edge: y = {new_lower_y:.2f} (should be {target_y_lower:.2f})")
print(f"  Bottom edge: y = {new_lower_bottom:.2f}")
print(f"  Top right: ({lower_right_x}, {new_lower_y:.2f})")
print()

print("=" * 70)
print("CHECKING OUTER CIRCLE BOUNDARIES")
print("=" * 70)
print()

def check_circle_boundary(x, y, radius):
    """Check if point is inside circle"""
    distance = math.sqrt(x**2 + y**2)
    return distance <= radius, distance

def circle_y_at_x(x, radius):
    """Get y values where vertical line intersects circle"""
    if abs(x) > radius:
        return None, None
    y = math.sqrt(radius**2 - x**2)
    return y, -y

print("UPPER RECTANGLE - Checking if it extends outside outer circle:")
print()

# Check corners
corners = [
    ("Top left", upper_rect['x'], new_upper_y),
    ("Top right", upper_rect['x'] + upper_rect['width'], new_upper_y),
    ("Bottom left", upper_rect['x'], new_upper_bottom),
    ("Bottom right", upper_rect['x'] + upper_rect['width'], new_upper_bottom)
]

for name, x, y in corners:
    inside, dist = check_circle_boundary(x, y, outer_radius)
    status = "INSIDE" if inside else "OUTSIDE"
    print(f"  {name:15s} ({x:7.2f}, {y:7.2f}): distance={dist:6.2f}, {status}")

# Check if top edge needs to be an arc
print()
print("  Checking top edge:")
for x in [upper_rect['x'], upper_rect['x'] + upper_rect['width']]:
    y_top, y_bottom = circle_y_at_x(x, outer_radius)
    print(f"    At x={x:6.1f}: circle boundary at y={y_bottom:.2f} (top), box top at y={new_upper_y:.2f}")
    if new_upper_y < y_bottom:
        print(f"      ✗ Box extends {y_bottom - new_upper_y:.2f} pixels OUTSIDE circle")

print()
print("LOWER RECTANGLE - Checking if it extends outside outer circle:")
print()

corners = [
    ("Top left", lower_rect['x'], new_lower_y),
    ("Top right", lower_rect['x'] + lower_rect['width'], new_lower_y),
    ("Bottom left", lower_rect['x'], new_lower_bottom),
    ("Bottom right", lower_rect['x'] + lower_rect['width'], new_lower_bottom)
]

for name, x, y in corners:
    inside, dist = check_circle_boundary(x, y, outer_radius)
    status = "INSIDE" if inside else "OUTSIDE"
    print(f"  {name:15s} ({x:7.2f}, {y:7.2f}): distance={dist:6.2f}, {status}")

# Check if bottom edge needs to be an arc
print()
print("  Checking bottom edge:")
for x in [lower_rect['x'], lower_rect['x'] + lower_rect['width']]:
    y_top, y_bottom = circle_y_at_x(x, outer_radius)
    print(f"    At x={x:6.1f}: circle boundary at y={y_top:.2f} (bottom), box bottom at y={new_lower_bottom:.2f}")
    if new_lower_bottom > y_top:
        print(f"      ✗ Box extends {new_lower_bottom - y_top:.2f} pixels OUTSIDE circle")

print()
print("=" * 70)
print("RECOMMENDATION")
print("=" * 70)
print()
print("Both rectangles extend outside the outer circle.")
print("Need to convert to paths with:")
print("  - UPPER box: Arc along outer circle for TOP edge")
print("  - LOWER box: Arc along outer circle for BOTTOM edge")
print()

# Calculate arc endpoints
print("ARC CALCULATIONS:")
print()
print("Upper box top arc:")
y_pos, y_neg = circle_y_at_x(upper_rect['x'], outer_radius)
print(f"  Start: ({upper_rect['x']}, {y_neg:.2f}) - left edge at outer circle")
y_pos, y_neg = circle_y_at_x(upper_rect['x'] + upper_rect['width'], outer_radius)
print(f"  End: ({upper_rect['x'] + upper_rect['width']}, {y_neg:.2f}) - right edge at outer circle")
print()

print("Lower box bottom arc:")
y_pos, y_neg = circle_y_at_x(lower_rect['x'], outer_radius)
print(f"  Start: ({lower_rect['x']}, {y_pos:.2f}) - left edge at outer circle")
y_pos, y_neg = circle_y_at_x(lower_rect['x'] + lower_rect['width'], outer_radius)
print(f"  End: ({lower_rect['x'] + lower_rect['width']}, {y_pos:.2f}) - right edge at outer circle")
