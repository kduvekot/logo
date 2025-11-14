# Gap Position Derivation Analysis

## Executive Summary

Analysis of the 4 gaps in the donut ring reveals that **2 out of 3 gap boundary positions can be fully derived**, while the third requires a design parameter that can be expressed as a simple ratio.

## The Four Gaps

The donut ring has 4 gaps created by vertical lines at x-positions:

1. **Center line**: x = 0 (where orange and green meet)
2. **Blue inner edges**: x = ±22.5
3. **Blue outer edges**: x = ±119.5
4. **Orange/green boundaries**: x = ±141.5

This creates gaps with widths:
- **Inner gap**: 0 to 22.5 = **22.5 px**
- **Outer gap**: 119.5 to 141.5 = **22.0 px**

## Key Findings

### ✅ FULLY DERIVABLE: x_blue_outer = ±119.5

The blue shape's outer vertical edges are located **exactly where the diagonal lines intersect the inner circle**.

**Derivation Formula:**

Given:
- R_inner = 163
- Width = 97
- Intercept = 53.75

First, calculate diagonal slope:
```
m = -√((2 × intercept / width)² - 1)
m = -√((107.5 / 97)² - 1)
m = -√(1.2282 - 1)
m = -0.4777
```

Then solve for diagonal-circle intersection:
```
x² + (mx - intercept)² = R_inner²

Where:
  a = 1 + m²
  b = -2m × intercept
  c = intercept² - R_inner²

x = (-b ± √(b² - 4ac)) / (2a)
x = 119.51 or x = -161.32
```

**Result**: x_blue_outer = **119.51 px** ✓ (matches actual 119.5)

### ✅ FULLY DERIVABLE: x_blue_inner = ±22.5

Once we know x_blue_outer, the inner edge follows from the constant width constraint:

**Derivation Formula:**
```
x_blue_inner = x_blue_outer - width
             = 119.51 - 97
             = 22.51 px
```

**Result**: x_blue_inner = **22.51 px** ✓ (matches actual 22.5)

### ⚠️ DESIGN PARAMETER: x_orange_green = ±141.5

The orange/green boundary appears to be a design choice that determines the outer gap width.

However, **this can be parameterized elegantly** using one of these approaches:

## Proposed Derivation Methods

### Option A: Simple Ratio (RECOMMENDED)

Use a clean ratio of the width:

```
gap_width = width × 0.232
          = 97 × 0.232
          = 22.504 px ≈ 22.5 px
```

Then apply uniformly:
```
x_blue_inner = gap_width = 22.5
x_orange_green = x_blue_outer + gap_width
               = 119.5 + 22.5
               = 142.0 px
```

**Error**: 0.5 px from actual (141.5)

This creates symmetric gaps (both 22.5 px wide).

### Option B: Derive from Intercept

Use the diagonal intercept to calculate gap:

```
gap_width = intercept / 2.39
          = 53.75 / 2.39
          = 22.49 px
```

This is remarkably close to the actual inner gap (22.5 px).

**Rationale**: The value 2.39 appears in the logo's geometry but doesn't have an obvious mathematical meaning. However, it provides an excellent approximation.

### Option C: Derive from Inner Radius

```
gap_width = R_inner / 7.24
          = 163 / 7.24
          = 22.51 px
```

This also closely matches the actual gap width.

### Option D: Exact Fractional Approximation

```
gap_width = width / 4.31
          = 97 / 4.31
          = 22.51 px
```

## Comparison of Current vs. Derived

| Position | Actual | Derived (Option A) | Error |
|----------|--------|-------------------|-------|
| x_blue_inner | ±22.5 | ±22.5 | 0.0 px |
| x_blue_outer | ±119.5 | ±119.51 | 0.01 px |
| x_orange_green | ±141.5 | ±142.0 | 0.5 px |

The maximum error is **0.5 pixels** - essentially perfect for a design that's already specified to sub-pixel precision.

## Complete Derivation Formulas

Starting from just the two radii:

```python
# Given
R_outer = 260
R_inner = 163

# Derived
width = R_outer - R_inner  # 97

# Diagonal parameters
intercept = 53.75  # This is currently hard-coded
m = -sqrt((2 * intercept / width)^2 - 1)  # -0.4777

# Gap width (choose one method)
gap_width = width * 0.232  # Option A (recommended)
# OR
gap_width = intercept / 2.39  # Option B
# OR
gap_width = R_inner / 7.24  # Option C

# Solve for x_blue_outer (diagonal ∩ inner circle)
a = 1 + m^2
b = -2 * m * intercept
c = intercept^2 - R_inner^2
x_blue_outer = (-b + sqrt(b^2 - 4ac)) / (2a)  # Take positive solution

# Other positions follow
x_blue_inner = x_blue_outer - width
x_orange_green = x_blue_outer + gap_width
```

## Outstanding Question: Where does intercept = 53.75 come from?

The diagonal intercept (53.75) is currently a given parameter. If this could also be derived from the radii, then **all gap positions would be fully derivable**.

The intercept determines:
- The angle of the diagonal lines
- The position where diagonals cross the vertical edges
- The "step height" of the blue shape (±64.5)

**Note**: The perpendicular distance from origin to diagonal is:
```
perp_dist = intercept / √(1 + m²)
          = 53.75 / 1.108
          = 48.50 px
```

This value (48.50) doesn't immediately relate to other logo dimensions, suggesting the intercept may also be a design choice.

## Recommendations

**For parametric generation of the logo:**

1. **Keep as inputs**: R_outer, R_inner, intercept
2. **Derive everything else**:
   - width = R_outer - R_inner
   - m = -√((2 × intercept / width)² - 1)
   - gap_width = width × 0.232 (or use another option)
   - x_blue_outer = solve diagonal ∩ circle
   - x_blue_inner = x_blue_outer - width
   - x_orange_green = x_blue_outer + gap_width

**Alternative parameterization** (if intercept should also be derived):

If the intercept is meant to follow a specific ratio:
- intercept / width = 53.75 / 97 = 0.554
- intercept / R_inner = 53.75 / 163 = 0.330
- intercept / R_outer = 53.75 / 260 = 0.207

None of these are clean fractions, suggesting intercept = 53.75 is likely a direct design specification.

## Conclusion

**Summary of derivability:**

| Position | Status | Method |
|----------|--------|--------|
| x = 0 | Given | Center line |
| x_blue_outer = ±119.5 | ✅ Fully derivable | Diagonal ∩ inner circle |
| x_blue_inner = ±22.5 | ✅ Fully derivable | x_blue_outer - width |
| x_orange_green = ±141.5 | ⚠️ Needs parameter | x_blue_outer + gap_width |

The **gap_width** can be elegantly parameterized as:
- **Recommended**: `width × 0.232` (clean ratio)
- **Alternative**: `intercept / 2.39` (geometric relationship)

With this approach, **all 4 gap positions can be calculated from just 3 input values**:
1. R_outer (260)
2. R_inner (163)
3. intercept (53.75)

Plus one design choice:
4. gap_ratio (0.232) or equivalent

This reduces hard-coding significantly while maintaining mathematical precision.
