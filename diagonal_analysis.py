#!/usr/bin/env python3
"""Analyze diagonal lines in the logo"""

import math

# Diagonal guide points
top_points = [(-18.5, -44.5), (0, -53), (22.5, -64)]
bottom_points = [(-18.5, 62), (0, 52), (22.5, 42)]

def fit_line(points):
    """Fit a line y = mx + b through points using least squares"""
    n = len(points)
    x_mean = sum(p[0] for p in points) / n
    y_mean = sum(p[1] for p in points) / n

    numerator = sum((p[0] - x_mean) * (p[1] - y_mean) for p in points)
    denominator = sum((p[0] - x_mean) ** 2 for p in points)

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    return slope, intercept

def line_circle_intersection(slope, intercept, radius):
    """Find where line y = mx + b intersects circle x^2 + y^2 = r^2"""
    # Substituting y = mx + b into x^2 + y^2 = r^2:
    # x^2 + (mx + b)^2 = r^2
    # (1 + m^2)x^2 + 2mbx + (b^2 - r^2) = 0

    a = 1 + slope**2
    b_coef = 2 * slope * intercept
    c = intercept**2 - radius**2

    discriminant = b_coef**2 - 4*a*c

    if discriminant < 0:
        return []

    x1 = (-b_coef + math.sqrt(discriminant)) / (2*a)
    x2 = (-b_coef - math.sqrt(discriminant)) / (2*a)

    y1 = slope * x1 + intercept
    y2 = slope * x2 + intercept

    return [(x1, y1), (x2, y2)]

def perpendicular_distance(slope1, intercept1, slope2, intercept2):
    """Calculate perpendicular distance between two parallel lines y = mx + b"""
    # Convert to Ax + By + C = 0 form: -mx + y - b = 0
    # Distance = |C1 - C2| / sqrt(A^2 + B^2)
    # For y = mx + b: -mx + y - b = 0, so A = -m, B = 1, C = -b

    if abs(slope1 - slope2) > 0.001:
        print("Warning: Lines are not parallel!")

    # Lines: -mx + y - b1 = 0 and -mx + y - b2 = 0
    # Distance = |(-b1) - (-b2)| / sqrt(m^2 + 1) = |b2 - b1| / sqrt(m^2 + 1)

    distance = abs(intercept2 - intercept1) / math.sqrt(slope1**2 + 1)
    return distance

# Fit lines
top_slope, top_intercept = fit_line(top_points)
bottom_slope, bottom_intercept = fit_line(bottom_points)

print("=" * 60)
print("DIAGONAL LINE ANALYSIS")
print("=" * 60)
print()

print("TOP DIAGONAL LINE:")
print(f"  Points: {top_points}")
print(f"  Slope: {top_slope:.6f}")
print(f"  Intercept: {top_intercept:.6f}")
print(f"  Equation: y = {top_slope:.6f}x + {top_intercept:.6f}")
print()

# Check fit quality
print("  Fit quality:")
for x, y_actual in top_points:
    y_predicted = top_slope * x + top_intercept
    error = abs(y_actual - y_predicted)
    print(f"    Point ({x:6.1f}, {y_actual:6.1f}): predicted y = {y_predicted:6.2f}, error = {error:.2f}")
print()

print("BOTTOM DIAGONAL LINE:")
print(f"  Points: {bottom_points}")
print(f"  Slope: {bottom_slope:.6f}")
print(f"  Intercept: {bottom_intercept:.6f}")
print(f"  Equation: y = {bottom_slope:.6f}x + {bottom_intercept:.6f}")
print()

# Check fit quality
print("  Fit quality:")
for x, y_actual in bottom_points:
    y_predicted = bottom_slope * x + bottom_intercept
    error = abs(y_actual - y_predicted)
    print(f"    Point ({x:6.1f}, {y_actual:6.1f}): predicted y = {y_predicted:6.2f}, error = {error:.2f}")
print()

print("=" * 60)
print("SYMMETRY ANALYSIS")
print("=" * 60)
print()

print(f"Top line slope:    {top_slope:.6f}")
print(f"Bottom line slope: {bottom_slope:.6f}")
print(f"Slope difference:  {abs(top_slope - bottom_slope):.6f}")
print()

if abs(top_slope - bottom_slope) < 0.01:
    print("✓ Lines are PARALLEL (slopes match within tolerance)")
else:
    print("✗ Lines are NOT parallel")
print()

# Check if lines are symmetric about x-axis
print(f"Top line intercept:    {top_intercept:.2f}")
print(f"Bottom line intercept: {bottom_intercept:.2f}")
print(f"Sum of intercepts:     {top_intercept + bottom_intercept:.2f}")
print()

if abs(top_intercept + bottom_intercept + 1) < 2:  # Should be close to -1 for perfect x-axis symmetry
    print("✓ Lines are approximately symmetric about horizontal centerline (y=0)")
else:
    print(f"  Distance from y=0 to top line:    {abs(top_intercept):.2f}")
    print(f"  Distance from y=0 to bottom line: {abs(bottom_intercept):.2f}")
    print(f"  Midpoint: y = {(top_intercept + bottom_intercept)/2:.2f}")
print()

print("=" * 60)
print("PERPENDICULAR DISTANCE")
print("=" * 60)
print()

perp_dist = perpendicular_distance(top_slope, top_intercept, bottom_slope, bottom_intercept)
print(f"Perpendicular distance between the two lines: {perp_dist:.2f} pixels")
print()

# Compare to other dimensions
print("For reference:")
print(f"  Outer radius: 260 px")
print(f"  Inner radius: 163 px")
print(f"  Ring width: 97 px")
print(f"  Distance between lines: {perp_dist:.2f} px")
print(f"  Ratio to ring width: {perp_dist/97:.3f}")
print()

print("=" * 60)
print("INTERSECTION WITH OUTER CIRCLE (r=260)")
print("=" * 60)
print()

top_intersections = line_circle_intersection(top_slope, top_intercept, 260)
print(f"Top diagonal intersections with outer circle:")
for i, (x, y) in enumerate(top_intersections, 1):
    print(f"  Point {i}: ({x:7.2f}, {y:7.2f})")
print()

bottom_intersections = line_circle_intersection(bottom_slope, bottom_intercept, 260)
print(f"Bottom diagonal intersections with outer circle:")
for i, (x, y) in enumerate(bottom_intersections, 1):
    print(f"  Point {i}: ({x:7.2f}, {y:7.2f})")
print()

print("=" * 60)
print("INTERSECTION WITH INNER CIRCLE (r=163)")
print("=" * 60)
print()

top_inner = line_circle_intersection(top_slope, top_intercept, 163)
print(f"Top diagonal intersections with inner circle:")
for i, (x, y) in enumerate(top_inner, 1):
    print(f"  Point {i}: ({x:7.2f}, {y:7.2f})")
print()

bottom_inner = line_circle_intersection(bottom_slope, bottom_intercept, 163)
print(f"Bottom diagonal intersections with inner circle:")
for i, (x, y) in enumerate(bottom_inner, 1):
    print(f"  Point {i}: ({x:7.2f}, {y:7.2f})")
print()

print("=" * 60)
print("INTERSECTION WITH VERTICAL LINES")
print("=" * 60)
print()

vertical_lines = [-141.5, -116.5, -18.5, 0, 2.5, 22.5, 119.5, 141.5]

print("Top diagonal intersections:")
for x in vertical_lines:
    y = top_slope * x + top_intercept
    print(f"  x = {x:7.1f}: y = {y:7.2f}")
print()

print("Bottom diagonal intersections:")
for x in vertical_lines:
    y = bottom_slope * x + bottom_intercept
    print(f"  x = {x:7.1f}: y = {y:7.2f}")
print()
