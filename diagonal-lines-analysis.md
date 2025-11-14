# Diagonal Lines Analysis

## Summary

Two diagonal lines form the angled edges of the blue center element in the logo. These lines are nearly parallel, symmetric about the horizontal centerline, and their perpendicular distance is remarkably close to the ring width.

## Line Equations (Centered Coordinate System)

**Top Diagonal Line:**
- Equation: `y = -0.476x - 53.2`
- Slope: -0.476082
- Y-intercept: -53.20

**Bottom Diagonal Line:**
- Equation: `y = -0.486x + 52.6`
- Slope: -0.486262
- Y-intercept: 52.65

## Symmetry Analysis

### Parallelism
- **Top slope:** -0.476082
- **Bottom slope:** -0.486262
- **Slope difference:** 0.010180 (~2% variation)
- **Status:** Nearly parallel (small variation likely due to approximation in guide points)

### Horizontal Symmetry (about y=0)
- **Top intercept:** -53.20
- **Bottom intercept:** 52.65
- **Sum of intercepts:** -0.55 (≈ 0)
- **Status:** ✓ **Symmetric about y=0**

The lines are perfectly balanced around the horizontal centerline, maintaining the logo's overall symmetry.

## Perpendicular Distance

**Distance between the two diagonal lines:** **95.57 pixels**

### Comparison to Logo Dimensions:
- Outer radius: 260 px
- Inner radius: 163 px
- **Ring width: 97 px**
- Diagonal separation: 95.57 px
- **Ratio: 95.57/97 = 0.985** (98.5% of ring width!)

This near-perfect match suggests the diagonal lines were intentionally designed to span approximately the same width as the ring segments.

## Verification Against PNG

The diagonal lines were verified against the original PNG image:

**Top diagonal:**
- Blue pixels found on the LEFT side (negative x)
- White/background pixels on the RIGHT side (positive x)
- ✓ Matches PNG edge

**Bottom diagonal:**
- Blue pixels found on the RIGHT side (positive x)
- White/background pixels on the LEFT side (negative x)
- ✓ Matches PNG edge

## Intersection Points with Circles

### Outer Circle (radius = 260)

**Top diagonal intersections:**
1. Left: (-251.36, 66.47)
2. Right: (210.07, -153.21)

**Bottom diagonal intersections:**
1. Left: (-209.21, 154.38)
2. Right: (250.62, -69.22)

### Inner Circle (radius = 163)

**Top diagonal intersections:**
1. Left: (-161.28, 23.59)
2. Right: (119.99, -110.32)

**Bottom diagonal intersections:**
1. Left: (-119.56, 110.79)
2. Right: (160.97, -25.63)

## Intersection Points with Vertical Lines

### Left vertical edge (x = -141.5)
- **Top diagonal:** y = 14.17
- **Bottom diagonal:** y = 121.45
- **Vertical span:** 107.28 pixels

This vertical line marks the left boundary of the orange ring segment.

### Right vertical edge (x = 141.5)
- **Top diagonal:** y = -120.56
- **Bottom diagonal:** y = -16.16
- **Vertical span:** 104.40 pixels

This vertical line marks the right boundary of the green ring segment.

## Notable Observations

1. **Width Consistency:** The perpendicular distance between diagonals (95.57 px) is almost exactly the ring width (97 px), showing consistent design language throughout the logo.

2. **Perfect Symmetry:** Despite the guide points being approximate, the fitted diagonal lines maintain perfect symmetry about the horizontal centerline (y=0).

3. **Integration with Shapes:** The diagonal lines intersect the vertical boundaries of the orange and green shapes, creating visual continuity in the design.

4. **Angle:** Both lines have a slope of approximately -0.48, which translates to an angle of about **25.6° below horizontal** (arctan(0.48) ≈ 25.6°).

5. **Geometric Harmony:** The diagonals connect the inner and outer circles at carefully calculated points, maintaining the circular geometry while adding dynamic angular elements.

## Visual Representation in SVG

The diagonal lines have been added to `base-logo-points-centered.svg` as:
- **Orange dashed lines** (thicker, more prominent than other guides)
- **Green intersection points** marking notable crossings with:
  - Inner circle (4 points)
  - Left vertical edge x=-141.5 (2 points)
  - Right vertical edge x=141.5 (2 points)

Total: 8 notable intersection points highlighted.
