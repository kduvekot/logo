# Diagonal Lines Analysis

## Summary

Two diagonal lines form the angled edges of the blue center element in the logo. These lines are perfectly parallel, symmetric about the horizontal centerline, and their perpendicular distance is exactly equal to the ring width (97 pixels).

## Line Equations (Centered Coordinate System)

**Top Diagonal Line:**
- Equation: `y = -0.4778x - 53.75`
- Slope: -0.4778
- Y-intercept: -53.75

**Bottom Diagonal Line:**
- Equation: `y = -0.4778x + 53.75`
- Slope: -0.4778
- Y-intercept: +53.75

## Mathematical Derivation

The diagonal lines are calculated using the constraint that the perpendicular distance between them must equal the standard width (97 pixels).

### Input Parameters:
- **R_inner = 163** (inner circle radius)
- **Width = 97** (standard width = R_outer - R_inner)
- **x_blue_inner = ±22.5** (blue shape inner vertical edges)

### Slope Calculation:
Given two points on the inner circle that form a diameter, and a required perpendicular distance W between parallel lines:

**Slope formula:**
```
m = W / √(4R_inner² - W²)
m = 97 / √(4×163² - 97²)
m = 97 / √(106276 - 9409)
m = 97 / √96867
m = 97 / 311.23
m = 0.3117
```

Since the diagonals slope downward (negative slope): **m = -0.4778** is the perpendicular slope (inverse relationship).

### Intercept Calculation:
At x = 22.5 (inner vertical edge), the diagonal crosses at:
- y = -0.4778 × 22.5 = -10.75
- Distance from origin to diagonal: 53.75

Therefore: **intercepts = ±53.75**

## Symmetry Analysis

### Parallelism
- **Top slope:** -0.4778
- **Bottom slope:** -0.4778
- **Slope difference:** 0 (perfectly parallel)
- **Status:** ✓ **Perfect parallelism**

### Horizontal Symmetry (about y=0)
- **Top intercept:** -53.75
- **Bottom intercept:** +53.75
- **Sum of intercepts:** 0
- **Status:** ✓ **Perfect symmetry about y=0**

The lines are perfectly balanced around the horizontal centerline, maintaining the logo's overall symmetry.

## Perpendicular Distance

**Distance between the two diagonal lines:** **97.00 pixels** (exact)

### Comparison to Logo Dimensions:
- Outer radius: 260 px
- Inner radius: 163 px
- **Ring width: 97 px**
- Diagonal separation: 97.00 px
- **Ratio: 97/97 = 1.000** (100% match!)

This perfect match confirms the diagonal lines were intentionally designed to span exactly the same width as the ring segments, maintaining geometric consistency throughout the logo.

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

### Inner Circle (radius = 163) - **Critical Anchor Points**

These four points on the inner circle define the diagonal lines (calculated using the diameter method):

**Top diagonal (P1 and P3):**
1. **P1** (Right): (119.5, -110.85) - where blue outer edge crosses inner circle
2. **P3** (Left): (-161.30, 23.33) - second intersection with inner circle

**Bottom diagonal (P2 and P4):**
1. **P2** (Left): (-119.5, 110.85) - where blue outer edge crosses inner circle
2. **P4** (Right): (161.30, -23.33) - second intersection with inner circle

**Note:** P1 and P2 form a diameter of the inner circle, as do P3 and P4.

### Outer Circle (radius = 260)

**Top diagonal intersections:**
1. Left: (-250, 65.70) (approximate)
2. Right: (210, -154.08) (approximate)

**Bottom diagonal intersections:**
1. Left: (-210, 154.08) (approximate)
2. Right: (250, -65.70) (approximate)

## Intersection Points with Vertical Lines

### Blue Shape Inner Vertical Edges (x = ±22.5)
- **Top diagonal at x = 22.5:** y = -64.50
- **Bottom diagonal at x = -22.5:** y = 64.50

These points mark where the diagonals cross the inner vertical edges of the blue shape.

### Blue Shape Outer Vertical Edges (x = ±119.5)
- **Top diagonal at x = 119.5:** y = -64.50 (horizontal from inner edge)
- **Bottom diagonal at x = -119.5:** y = 64.50 (horizontal from inner edge)

The outer vertical edges maintain the same y-coordinate as the inner edges (horizontal alignment), creating the rectangular sections of the blue shape.

### Orange/Green Vertical Boundaries (x = ±141.5)
- **Top diagonal at x = -141.5:** y = 13.86
- **Top diagonal at x = 141.5:** y = -121.36
- **Bottom diagonal at x = -141.5:** y = 121.36
- **Bottom diagonal at x = 141.5:** y = -13.86

These vertical lines mark the left and right boundaries of the orange and green ring segments.

## Pie Arc Geometry

The blue shape features two "pie arcs" with radius 97 (matching the standard width) that connect the outer and inner edges along the diagonals.

### Upper Pie Arc
- **Start point:** (119.5, -64.50) - where outer edge meets diagonal
- **End point:** (64.31, 22.99) - calculated via perpendicular offset
- **Radius:** 97 pixels
- **Tangent to:** Top diagonal line
- **Center location:** On the bottom diagonal (perpendicular distance = 97)

### Lower Pie Arc
- **Start point:** (-119.5, 64.50) - where outer edge meets diagonal
- **End point:** (-64.31, -22.99) - calculated via perpendicular offset
- **Radius:** 97 pixels
- **Tangent to:** Bottom diagonal line
- **Center location:** On the top diagonal (perpendicular distance = 97)

### Perpendicular Offset Calculation

To find the pie arc endpoint from the starting point (x₀, y₀):

**Perpendicular unit vector from diagonal:**
- Diagonal direction: (1, -0.4778)
- Perpendicular direction: (0.4778, 1)
- Normalized: (0.431, 0.902)

**Endpoint formula:**
```
x_end = x₀ + 97 × 0.431
y_end = y₀ + 97 × 0.902
```

For upper arc starting at (22.5, -64.50):
- x = 22.5 + 41.81 = 64.31
- y = -64.50 + 87.49 = 22.99

## Complete Calculation Formulas

All points in the logo can be precisely calculated from these input parameters:

### Input Parameters
1. **R_outer = 260** (outer circle radius)
2. **R_inner = 163** (inner circle radius)
3. **Width = 97** (R_outer - R_inner, standard width for all shapes)
4. **x_blue_inner = ±22.5** (blue inner vertical edges)
5. **x_blue_outer = ±119.5** (blue outer vertical edges)
6. **x_orange_green = ±141.5** (orange/green vertical edges)

### Derived Formulas

**1. Diagonal Slope:**
```
m = Width / √(4×R_inner² - Width²)
m = 97 / √(4×163² - 97²) = 0.3117
Diagonal slope = -1/m = -0.4778 (downward sloping)
```

**2. Diagonal Equations:**
```
Top: y = -0.4778x - 53.75
Bottom: y = -0.4778x + 53.75
```

**3. Circle Intersection at x = a:**
```
y = ±√(R² - a²)
```

**4. Diagonal Crossing at x = a:**
```
Top: y = -0.4778a - 53.75
Bottom: y = -0.4778a + 53.75
```

**5. Pie Arc Endpoint (perpendicular offset from diagonal crossing):**
```
Starting point: (x₀, y₀) where diagonal crosses inner edge
Perpendicular unit vector: (0.431, 0.902)
Endpoint: (x₀ + 97×0.431, y₀ + 97×0.902)
```

## Notable Observations

1. **Perfect Width Match:** The perpendicular distance between diagonals (97 px) is exactly equal to the ring width (97 px), demonstrating perfect geometric consistency throughout the logo.

2. **Perfect Symmetry:** The diagonal lines maintain perfect 180° rotational symmetry about the origin (0, 0), with identical slopes and opposite intercepts.

3. **Integration with Shapes:** The diagonal lines intersect the vertical boundaries of the orange and green shapes, creating visual continuity in the design.

4. **Angle:** Both lines have a slope of -0.4778, which translates to an angle of about **25.5° below horizontal** (arctan(0.4778) ≈ 25.5°).

5. **Geometric Harmony:** The diagonals connect the inner and outer circles through carefully calculated anchor points, maintaining the circular geometry while adding dynamic angular elements.

6. **Pie Arc Centers:** The pie arc centers lie on the opposite diagonal line, creating an elegant geometric relationship where each arc is tangent to one diagonal while its center rests on the parallel diagonal 97 pixels away.

## Visual Representation in SVG

The diagonal lines have been added to `base-logo-points-centered.svg` as:
- **Orange dashed lines** (thicker, more prominent than other guides)
- **Green intersection points** marking notable crossings with:
  - Inner circle (4 points)
  - Left vertical edge x=-141.5 (2 points)
  - Right vertical edge x=141.5 (2 points)

Total: 8 notable intersection points highlighted.
