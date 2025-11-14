#!/usr/bin/env python3
"""
Detailed analysis of gaps to find if x-positions can be derived.
"""

import math

# Primary input parameters
R_outer = 260
R_inner = 163
width = 97

# Current x-positions (to be analyzed)
x_blue_inner = 22.5
x_blue_outer = 119.5
x_orange_green = 141.5

# Diagonal parameters (derived from width)
intercept = 53.75
m = -math.sqrt((2 * intercept / width)**2 - 1)

print("=" * 80)
print("COMPREHENSIVE GAP POSITION ANALYSIS")
print("=" * 80)

print("\n📊 GIVEN PARAMETERS:")
print(f"   R_outer = {R_outer} px")
print(f"   R_inner = {R_inner} px")
print(f"   Width = {width} px")

print("\n🎯 CURRENT GAP BOUNDARIES (what we want to derive):")
print(f"   x_blue_inner = ±{x_blue_inner}")
print(f"   x_blue_outer = ±{x_blue_outer}")
print(f"   x_orange_green = ±{x_orange_green}")

print("\n" + "=" * 80)
print("FINDING #1: x_blue_outer is FULLY DERIVABLE")
print("=" * 80)

# The diagonal line y = mx - intercept intersects the inner circle
# at x_blue_outer. We can derive this from first principles.

print("\nThe top diagonal y = {:.4f}x - {:.2f} intersects the inner circle.".format(m, intercept))
print("Solving: x² + ({:.4f}x - {:.2f})² = {}²".format(m, intercept, R_inner))

a = 1 + m**2
b = -2 * m * intercept
c = intercept**2 - R_inner**2

disc = b**2 - 4*a*c
x1 = (-b + math.sqrt(disc)) / (2*a)
x2 = (-b - math.sqrt(disc)) / (2*a)

print(f"\nQuadratic: {a:.4f}x² + ({b:.4f})x + ({c:.4f}) = 0")
print(f"Solutions: x = {x1:.2f} or x = {x2:.2f}")

# One solution is positive (right side), one is negative (left side)
x_derived_right = max(x1, x2)
x_derived_left = min(x1, x2)

print(f"\n✅ RIGHT intersection: x = {x_derived_right:.2f}")
print(f"   Actual x_blue_outer = {x_blue_outer}")
print(f"   Match: {abs(x_derived_right - x_blue_outer) < 0.1}")

print(f"\n   LEFT intersection: x = {x_derived_left:.2f}")
print(f"   (This is the other point where diagonal crosses inner circle)")

# Verify these are on the circle
y_right = m * x_derived_right - intercept
y_left = m * x_derived_left - intercept
dist_right = math.sqrt(x_derived_right**2 + y_right**2)
dist_left = math.sqrt(x_derived_left**2 + y_left**2)
print(f"\n   Verification:")
print(f"   Right point: ({x_derived_right:.2f}, {y_right:.2f}), distance = {dist_right:.2f}")
print(f"   Left point: ({x_derived_left:.2f}, {y_left:.2f}), distance = {dist_left:.2f}")
print(f"   Inner radius: {R_inner}")

print("\n" + "=" * 80)
print("FINDING #2: x_blue_inner follows from x_blue_outer")
print("=" * 80)

print(f"\nThe blue shape has constant width = {width} px")
print(f"Therefore: x_blue_inner = x_blue_outer - width")
print(f"         = {x_derived_right:.2f} - {width}")
print(f"         = {x_derived_right - width:.2f}")
print(f"\n✅ Derived x_blue_inner = {x_derived_right - width:.2f}")
print(f"   Actual x_blue_inner = {x_blue_inner}")
print(f"   Match: {abs((x_derived_right - width) - x_blue_inner) < 0.1}")

print("\n" + "=" * 80)
print("FINDING #3: Analyzing x_orange_green = ±{:.1f}".format(x_orange_green))
print("=" * 80)

# The orange/green boundary is where these shapes end
# Gap from blue outer to orange/green edge
outer_gap = x_orange_green - x_blue_outer

print(f"\nOuter gap width: {x_orange_green} - {x_blue_outer} = {outer_gap} px")
print(f"Inner gap width: {x_blue_inner} - 0 = {x_blue_inner} px")
print(f"\nThese gaps are almost equal (difference: {abs(outer_gap - x_blue_inner):.1f} px)")

print("\n🔍 Testing if gaps are related to other parameters:")

# Test various ratios
test_ratios = [
    ("Width / 4", width / 4),
    ("Width / 4.3", width / 4.3),
    ("Width / 4.31", width / 4.31),
    ("Intercept / 2", intercept / 2),
    ("Intercept / 2.4", intercept / 2.4),
    ("Intercept / 2.39", intercept / 2.39),
    ("R_inner / 7", R_inner / 7),
    ("R_inner / 7.24", R_inner / 7.24),
    ("Width × 0.232", width * 0.232),
]

print(f"\n   Searching for derivation of inner gap ({x_blue_inner}):")
for name, value in test_ratios:
    if abs(value - x_blue_inner) < 0.6:
        print(f"   • {name:20s} = {value:6.2f} (error: {abs(value - x_blue_inner):.2f})")

print(f"\n   Searching for derivation of outer gap ({outer_gap}):")
for name, value in test_ratios:
    if abs(value - outer_gap) < 0.6:
        print(f"   • {name:20s} = {value:6.2f} (error: {abs(value - outer_gap):.2f})")

print("\n📐 Geometric analysis of the gaps:")

# The diagonal crosses at x_blue_inner
y_cross_inner = m * x_blue_inner - intercept
print(f"\n   At x = {x_blue_inner}, diagonal crosses at y = {y_cross_inner:.2f}")
print(f"   This creates the horizontal 'step' at y = ±{abs(y_cross_inner):.2f}")

# Check if x_blue_inner relates to this y-coordinate
print(f"\n   Checking if x_blue_inner relates to the step height:")
print(f"   y_cross / x_inner = {abs(y_cross_inner) / x_blue_inner:.3f}")
print(f"   x_inner / y_cross = {x_blue_inner / abs(y_cross_inner):.3f}")

# Check arc length at mid-radius
mid_radius = (R_outer + R_inner) / 2
angle_inner = math.atan2(abs(y_cross_inner), x_blue_inner)
arc_to_inner = mid_radius * angle_inner
print(f"\n   Arc length from center to inner gap (at mid-radius {mid_radius:.1f}):")
print(f"   Angle: {math.degrees(angle_inner):.2f}°")
print(f"   Arc length: {arc_to_inner:.2f} px")

print("\n" + "=" * 80)
print("EXPLORING ALTERNATIVE APPROACHES")
print("=" * 80)

print("\n🔬 What if we parameterize by the gap ratio?")
print(f"\n   Define: gap_ratio = inner_gap / width")
print(f"   Current: gap_ratio = {x_blue_inner / width:.4f}")

print(f"\n   Then:")
print(f"   • x_blue_inner = width × gap_ratio")
print(f"   • x_blue_outer = x_blue_inner + width")
print(f"   • x_orange_green = x_blue_outer + (width × gap_ratio)")
print(f"     (if we assume outer gap ≈ inner gap)")

gap_ratio = x_blue_inner / width
x_test_inner = width * gap_ratio
x_test_outer = x_test_inner + width
x_test_boundary = x_test_outer + width * gap_ratio

print(f"\n   With gap_ratio = {gap_ratio:.4f}:")
print(f"   • x_blue_inner = {x_test_inner:.2f} ✓")
print(f"   • x_blue_outer = {x_test_outer:.2f} ✓")
print(f"   • x_orange_green = {x_test_boundary:.2f} (actual: {x_orange_green})")
print(f"     Error: {abs(x_test_boundary - x_orange_green):.2f} px")

print("\n🔬 What if the gap is chosen for visual balance?")

# The orange/green shapes span from x=0 to x=±141.5
# Calculate the arc length they cover
angles_at_mid = []
for x_val in [0, x_orange_green]:
    y_val = math.sqrt(mid_radius**2 - x_val**2)
    angle = math.atan2(y_val, x_val)
    angles_at_mid.append(angle)

arc_span_orange = mid_radius * (angles_at_mid[0] - angles_at_mid[1])
total_arc = math.pi * mid_radius  # Half circle

print(f"\n   Orange/green shapes span from x=0 to x=±{x_orange_green}")
print(f"   At mid-radius {mid_radius:.1f}:")
print(f"   • Arc from 0° to {math.degrees(angles_at_mid[1]):.1f}° = {arc_span_orange:.1f} px")
print(f"   • Total half-circle arc = {total_arc:.1f} px")
print(f"   • Coverage: {100 * arc_span_orange / total_arc:.1f}%")

print("\n" + "=" * 80)
print("SUMMARY & RECOMMENDATIONS")
print("=" * 80)

print("\n✅ FULLY DERIVABLE:")
print(f"   1. x_blue_outer = {x_derived_right:.2f}")
print(f"      → Intersection of diagonal with inner circle")
print(f"      → Formula: solve x² + (mx - b)² = R_inner²")
print(f"                 where m = {m:.4f}, b = {intercept}")

print(f"\n   2. x_blue_inner = {x_derived_right - width:.2f}")
print(f"      → Formula: x_blue_outer - width")

print("\n⚠️  NEEDS SPECIFICATION:")
print(f"   3. x_orange_green = ±{x_orange_green}")
print(f"      → Currently appears to be a design choice")
print(f"      → Defines outer gap width: {outer_gap} px")
print(f"      → Close to inner gap width: {x_blue_inner} px")

print("\n💡 PROPOSED PARAMETERIZATION:")
print("\n   Option A: Specify 'gap_width' as input parameter")
print(f"            gap_width ≈ {x_blue_inner:.1f} px (or {x_blue_inner/width:.3f} × width)")
print(f"            Then: x_blue_inner = gap_width")
print(f"                  x_orange_green = x_blue_outer + gap_width")

print("\n   Option B: Derive from geometric proportion")
print(f"            Use intercept/2.39 ≈ {intercept/2.39:.2f} as gap width")
print(f"            This is close to both gaps ({x_blue_inner} and {outer_gap})")

print("\n   Option C: Keep gaps symmetric (outer = inner)")
print(f"            Set both gaps = {x_blue_inner:.1f}")
print(f"            Then x_orange_green = x_blue_outer + {x_blue_inner:.1f}")
print(f"                                = {x_blue_outer + x_blue_inner:.1f}")
print(f"            Current actual: {x_orange_green} (diff: {abs(x_orange_green - (x_blue_outer + x_blue_inner)):.1f} px)")

print("\n" + "=" * 80)
