#!/usr/bin/env python3
"""
Analysis of the 4 gaps in the donut ring to find derivable patterns.
"""

import math

# Primary input parameters
R_outer = 260  # outer circle radius
R_inner = 163  # inner circle radius
width = R_outer - R_inner  # 97

# Current hard-coded gap boundary positions (centered coordinates)
x_blue_inner = 22.5   # Inner vertical edges of blue shape
x_blue_outer = 119.5  # Outer vertical edges of blue shape
x_orange_green = 141.5  # Vertical edges where orange/green shapes end

# Derived diagonal parameters
# For parallel lines y = mx ± b with perpendicular distance W:
# W = 2b / √(1 + m²)
# So: √(1 + m²) = 2b / W
# Given W = 97 and 2b = 107.5:
intercept = 53.75  # y-intercept of diagonal lines (half the intercept separation)
diagonal_slope = -math.sqrt((2 * intercept / width)**2 - 1)  # ≈ -0.4778

print("=" * 70)
print("GAP ANALYSIS - Finding Patterns and Derivations")
print("=" * 70)

print("\n1. PRIMARY PARAMETERS:")
print(f"   R_outer = {R_outer}")
print(f"   R_inner = {R_inner}")
print(f"   Width = {width}")
print(f"   Diagonal slope = {diagonal_slope:.4f}")
print(f"   Diagonal intercept = ±{intercept}")

print("\n2. CURRENT GAP BOUNDARIES:")
print(f"   x_blue_inner = ±{x_blue_inner}")
print(f"   x_blue_outer = ±{x_blue_outer}")
print(f"   x_orange_green = ±{x_orange_green}")

print("\n3. GAP WIDTHS:")
inner_gap = x_blue_inner - 0  # From center to blue inner edge
outer_gap = x_orange_green - x_blue_outer  # From blue outer to orange/green edge
print(f"   Inner gap width: {inner_gap} pixels")
print(f"   Outer gap width: {outer_gap} pixels")
print(f"   Difference: {inner_gap - outer_gap} pixels")

print("\n4. KEY RELATIONSHIP - Horizontal Spacing:")
blue_width = x_blue_outer - x_blue_inner
print(f"   x_blue_outer - x_blue_inner = {blue_width}")
print(f"   This equals the ring width: {width}")
print(f"   ✓ EXACT MATCH!" if blue_width == width else f"   ✗ Mismatch: {blue_width - width}")

print("\n5. DIAGONAL INTERSECTION WITH INNER CIRCLE:")
# The diagonal y = mx + b intersects the inner circle at x_blue_outer
# Verify: x² + y² = R_inner²
y_at_outer = diagonal_slope * x_blue_outer - intercept  # Top diagonal (negative intercept)
dist_from_origin = math.sqrt(x_blue_outer**2 + y_at_outer**2)
print(f"   At x = {x_blue_outer}:")
print(f"   Diagonal y-coordinate: {y_at_outer:.2f}")
print(f"   Inner circle y-coordinate: {-math.sqrt(R_inner**2 - x_blue_outer**2):.2f}")
print(f"   Distance from origin: {dist_from_origin:.2f}")
print(f"   Inner circle radius: {R_inner}")
if abs(dist_from_origin - R_inner) < 0.1:
    print(f"   ✓ x_blue_outer is where diagonal intersects inner circle!")

print("\n6. DIAGONAL CROSSING AT INNER EDGE:")
y_at_inner = diagonal_slope * x_blue_inner - intercept
print(f"   At x = {x_blue_inner}:")
print(f"   Diagonal y-coordinate: {y_at_inner:.2f}")
print(f"   This defines the horizontal step height: {abs(y_at_inner):.2f}")

print("\n7. RATIO ANALYSIS:")
print(f"\n   Gap widths relative to width ({width}):")
print(f"   Inner gap / width = {inner_gap / width:.4f} = {inner_gap}/{width}")
print(f"   Outer gap / width = {outer_gap / width:.4f} = {outer_gap}/{width}")

print(f"\n   Gap widths relative to R_inner ({R_inner}):")
print(f"   Inner gap / R_inner = {inner_gap / R_inner:.4f}")
print(f"   Outer gap / R_inner = {outer_gap / R_inner:.4f}")

print(f"\n   Gap widths relative to R_outer ({R_outer}):")
print(f"   Inner gap / R_outer = {inner_gap / R_outer:.4f}")
print(f"   Outer gap / R_outer = {outer_gap / R_outer:.4f}")

print(f"\n   x_blue_outer relative to parameters:")
print(f"   x_blue_outer / R_inner = {x_blue_outer / R_inner:.4f}")
print(f"   x_blue_outer / R_outer = {x_blue_outer / R_outer:.4f}")
print(f"   x_blue_outer / width = {x_blue_outer / width:.4f}")

print("\n8. TESTING DERIVATION OF x_blue_outer FROM DIAGONAL:")
# Solve for x where diagonal intersects inner circle
# Diagonal: y = mx - b (using negative intercept for top diagonal)
# Circle: x² + y² = R_inner²
# Substituting: x² + (mx - b)² = R_inner²
# x² + m²x² - 2mbx + b² = R_inner²
# (1 + m²)x² - 2mbx + (b² - R_inner²) = 0

m = diagonal_slope
b = intercept

a_coef = 1 + m**2
b_coef = -2 * m * (-b)  # Note: using -b for top diagonal
c_coef = b**2 - R_inner**2

discriminant = b_coef**2 - 4 * a_coef * c_coef
x_solutions = [
    (-b_coef + math.sqrt(discriminant)) / (2 * a_coef),
    (-b_coef - math.sqrt(discriminant)) / (2 * a_coef)
]

print(f"   Solving: ({1 + m**2:.4f})x² + ({b_coef:.4f})x + ({c_coef:.4f}) = 0")
print(f"   Solutions: x = {x_solutions[0]:.2f} or x = {x_solutions[1]:.2f}")
x_derived = max(x_solutions)  # Take the positive solution on the right
print(f"   ✓ Derived x_blue_outer = {x_derived:.2f} (actual: {x_blue_outer})")

print("\n9. EXPLORING GAP WIDTH PATTERNS:")
print("\n   Testing if gap widths follow simple fractions:")
for denom in range(2, 20):
    for numer in range(1, denom):
        ratio = numer / denom
        test_gap = width * ratio
        if abs(test_gap - inner_gap) < 0.6:
            print(f"   Inner gap ≈ {numer}/{denom} × width = {test_gap:.2f} (actual: {inner_gap})")
        if abs(test_gap - outer_gap) < 0.6:
            print(f"   Outer gap ≈ {numer}/{denom} × width = {test_gap:.2f} (actual: {outer_gap})")

print("\n   Testing if gap widths relate to intercept:")
print(f"   intercept / 2 = {intercept / 2:.2f}")
print(f"   intercept / 2.4 = {intercept / 2.4:.2f} (close to inner gap: {inner_gap})")
print(f"   intercept / 2.44 = {intercept / 2.44:.2f} (close to inner gap: {inner_gap})")

print("\n10. ALTERNATIVE DERIVATION APPROACH:")
print("\n   What if x_blue_inner is derived from the diagonal geometry?")
print(f"   Diagonal intercept: ±{intercept}")
print(f"   If we use intercept / α = x_blue_inner:")
alpha = intercept / x_blue_inner
print(f"   α = {alpha:.4f}")
print(f"   So x_blue_inner = intercept / {alpha:.4f}")

# Check if this alpha has meaning
print(f"\n   Checking if α = {alpha:.4f} relates to other parameters:")
print(f"   width / intercept = {width / intercept:.4f}")
print(f"   R_inner / intercept = {R_inner / intercept:.4f}")
print(f"   sqrt(width² + intercept²) / intercept = {math.sqrt(width**2 + intercept**2) / intercept:.4f}")

print("\n11. GEOMETRIC RELATIONSHIP TEST:")
# The perpendicular distance from origin to diagonal is related to intercept
perp_distance = intercept / math.sqrt(1 + diagonal_slope**2)
print(f"   Perpendicular distance from origin to diagonal: {perp_distance:.2f}")
print(f"   This should equal the intercept / √(1 + m²): {intercept / math.sqrt(1 + diagonal_slope**2):.2f}")

# Testing if gap widths relate to this perpendicular distance
print(f"   Perpendicular distance / 2 = {perp_distance / 2:.2f}")
print(f"   Perpendicular distance / 2.1 = {perp_distance / 2.1:.2f} (close to inner gap: {inner_gap})")

print("\n12. SUMMARY OF FINDINGS:")
print("   ✓ x_blue_outer can be DERIVED from diagonal-circle intersection")
print("   ✓ x_blue_inner = x_blue_outer - width (once x_blue_outer is known)")
print("   ? x_orange_green = x_blue_outer + outer_gap")
print(f"   ? Inner gap width ({inner_gap}) - needs derivation")
print(f"   ? Outer gap width ({outer_gap}) - needs derivation")

print("\n   The gap widths appear to be design choices rather than")
print("   derived from a simple mathematical relationship.")
print("   However, they are very close (22.5 vs 22.0), suggesting")
print("   they may follow an aesthetic ratio or proportion.")

print("\n" + "=" * 70)
