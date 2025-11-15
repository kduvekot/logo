# Logo Design Documentation

## Overview

This logo consists of three colored shapes (orange, green, and blue) arranged in a circular pattern with vertical gaps between them. The design exhibits perfect 180° rotational symmetry about the origin.

## Coordinate System

**All coordinates use the center of the circles as the origin (0, 0).**

This ensures that mirrored points have opposite coordinates, making the symmetry immediately apparent:
- Points on the left have negative x-coordinates
- Points on the right have positive x-coordinates
- Top points have negative y-coordinates
- Bottom points have positive y-coordinates
- Rotationally symmetric points differ only by sign: (x, y) ↔ (-x, -y)

## Parameterization

The entire logo is defined by three independent parameters:

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Ring width | **W** | The radial thickness of all three shapes |
| Inner radius | **Ri** | Radius of the inner circle |
| Gap proportion | **G** | Gap size as a fraction of W (gap = G × W) |

### Original PNG Image Parameters

The original PNG image (base-logo.png) uses these values:

```
W  = 97
Ri = 163
G  = 22.5/97 ≈ 0.2319587629 (approximately 0.232)
```

### Current Experimental Parameters

The experimental SVG (experiment-logo-w100.svg) uses:

```
W  = 100
Ri = 200
G  = 1/3 ≈ 0.3333333333
```

## Derived Parameters

All other dimensions are calculated from W, Ri, and G:

### Circle Radii

```
Ro = Ri + W                    (outer circle radius)
```

### Vertical Edge Positions

```
gap            = G × W         (gap width between shapes)
x_blue_inner   = ±GW          (blue shape inner vertical edges)
x_blue_outer   = ±W(G + 1)    (blue shape outer vertical edges)
x_orange_green = ±W(2G + 1)   (orange/green boundary edges)
```

Note the ± notation indicates both positive and negative x-coordinates (mirrored positions).

## Shape Descriptions

### Orange Shape (Left)

A ring segment spanning from the top center to the left side.

**Structure:** 4 edges
1. Vertical line at x = 0 (from outer to inner circle)
2. Counter-clockwise arc along inner circle
3. Vertical line at x = -W(2G + 1) (from inner to outer circle)
4. Clockwise arc along outer circle back to start

**Vertices:**

| Point | Formula | Description |
|-------|---------|-------------|
| P1 | (0, -Ro) = (0, -(Ri + W)) | Top center, outer circle |
| P2 | (0, -Ri) | Top center, inner circle |
| P3 | (-W(2G+1), √[Ri² - W²(2G+1)²]) | Left boundary, inner circle |
| P4 | (-W(2G+1), √[Ro² - W²(2G+1)²]) | Left boundary, outer circle |

### Green Shape (Right)

A ring segment spanning from the bottom center to the right side (180° rotation of orange).

**Structure:** 4 edges (same as orange, rotated 180°)
1. Vertical line at x = 0 (from outer to inner circle)
2. Clockwise arc along inner circle
3. Vertical line at x = W(2G + 1) (from inner to outer circle)
4. Counter-clockwise arc along outer circle back to start

**Vertices:**

| Point | Formula | Description |
|-------|---------|-------------|
| P1 | (0, Ro) = (0, Ri + W) | Bottom center, outer circle |
| P2 | (0, Ri) | Bottom center, inner circle |
| P3 | (W(2G+1), -√[Ri² - W²(2G+1)²]) | Right boundary, inner circle |
| P4 | (W(2G+1), -√[Ro² - W²(2G+1)²]) | Right boundary, outer circle |

**Symmetry:** Green point j = -1 × Orange point j (180° rotation)

### Blue Shape (Center)

A complex stepped shape with diagonal edges connecting the upper and lower sections.

**Structure:** 10 edges with 180° rotational symmetry
- 2 outer circle arcs (radius Ro)
- 4 vertical lines
- 2 diagonal lines
- 2 pie arcs (radius W)

## Diagonal Line Equations

The diagonal lines are the most complex part of the design. They are derived from geometric constraints.

### Constraints

1. **Point on inner circle:** The diagonal must pass through point P1 on the inner circle at x = W(G+1)
   ```
   P1 = (W(G+1), -√[Ri² - W²(G+1)²])
   ```

2. **Perpendicular distance:** The perpendicular distance between the two parallel diagonals must equal W
   ```
   For lines y = sx ± c: distance = 2c/√(1 + s²)
   Therefore: c = W√(1 + s²)/2
   ```

3. **Line passes through P1:** The top diagonal passes through P1
   ```
   -√[Ri² - W²(G+1)²] = s × W(G+1) - c
   ```

### Derivation

Let H = √[Ri² - W²(G+1)²] (y-coordinate of P1)

Combining constraints 2 and 3:
```
W√(1 + s²)/2 = s × W(G+1) + H
```

Squaring both sides:
```
W²(1 + s²)/4 = [s × W(G+1) + H]²
W²(1 + s²)/4 = s²W²(G+1)² + 2s × W(G+1) × H + H²
```

Rearranging into standard quadratic form:
```
s²W²[1/4 - (G+1)²] - 2s × W(G+1) × H + [W²/4 - H²] = 0
```

This quadratic equation in s yields the slope of the diagonal lines.

### Equations

```
Top diagonal:    y = sx - c
Bottom diagonal: y = sx + c
```

where:
- s = slope (calculated from quadratic above)
- c = intercept (calculated from constraint 2)

### Example Values

**For W=100, Ri=200, G=1/3:**
- H = √[200² - 100²(4/3)²] = 100√20/3 ≈ 149.071
- s ≈ -0.6672
- c ≈ 60.107

**For original PNG (W=97, Ri=163, G≈0.232):**
- H = √[163² - 97²(1.232)²] ≈ 110.85
- s ≈ -0.4778
- c ≈ 53.75

## Blue Shape Vertices

### Perpendicular Unit Vector

For diagonal slope s, the perpendicular unit vector is:
```
u_perp = (-s, 1) / √(s² + 1)
```

This vector points perpendicular to the diagonal, used for calculating pie arc endpoints.

### Top Section (5 vertices)

| Point | Formula | Description |
|-------|---------|-------------|
| P1 | (GW, -√[(Ri+W)² - G²W²]) | Start at outer circle, x = x_blue_inner |
| P2 | (W(G+1), -√[(Ri+W)² - W²(G+1)²]) | Outer arc endpoint, x = x_blue_outer |
| P3 | (W(G+1), s×GW - c) | Vertical line to diagonal crossing |
| P4 | (GW - Ws/√(s²+1), s×GW - c + W/√(s²+1)) | Pie arc endpoint on bottom diagonal |
| P5 | (-GW, -s×GW + c) | Diagonal line to opposite inner edge |

### Bottom Section (5 vertices)

| Point | Formula | Description |
|-------|---------|-------------|
| P6 | (-GW, √[(Ri+W)² - G²W²]) | Vertical line to outer circle |
| P7 | (-W(G+1), √[(Ri+W)² - W²(G+1)²]) | Outer arc endpoint |
| P8 | (-W(G+1), -s×GW + c) | Vertical line to diagonal crossing |
| P9 | (-GW + Ws/√(s²+1), -s×GW + c - W/√(s²+1)) | Pie arc endpoint on top diagonal |
| P10 | (GW, s×GW - c) | Diagonal line back to starting side |

**Symmetry:** Bottom point (P6-P10) = -1 × Top point (P1-P5)

### Arc Parameters

- **Outer circle arcs:** radius = Ro = Ri + W
- **Pie arcs:** radius = W

## Symmetry Properties

### 180° Rotational Symmetry

Every point (x, y) in the logo has a corresponding point (-x, -y):

```
Orange P3 = -Green P3
Orange P4 = -Green P4
Blue P1 = -Blue P6
Blue P2 = -Blue P7
Blue P3 = -Blue P8
Blue P4 = -Blue P9
Blue P5 = -Blue P10
```

### Mirror Symmetry in Formulas

Notice how formulas naturally show symmetry:
- Top diagonal: y = sx - c
- Bottom diagonal: y = sx + c (only sign of c changes)
- Left edge: x = -W(2G+1)
- Right edge: x = +W(2G+1) (only sign changes)

## Gap Structure

There are **four gaps** in the logo where white space separates the colored shapes:

| Gap | Location | Width | Formula |
|-----|----------|-------|---------|
| 1 | Top center (between orange and blue) | GW | From x=0 to x=GW |
| 2 | Top right (between blue and green) | GW | From x=W(G+1) to x=W(2G+1) |
| 3 | Bottom center (between green and blue) | GW | From x=0 to x=-GW |
| 4 | Bottom left (between blue and orange) | GW | From x=-W(G+1) to x=-W(2G+1) |

All gaps have the same width: **GW**

Gap 3 = -Gap 1 (mirrored)
Gap 4 = -Gap 2 (mirrored)

## Design Philosophy

1. **Single width throughout:** All three shapes maintain the same radial width W, creating visual consistency.

2. **Vertical boundaries:** Gaps between shapes use vertical lines (constant x), not radial lines, creating a modern stepped appearance.

3. **Dynamic diagonals:** The blue shape's diagonal edges add visual interest while maintaining geometric precision.

4. **Perfect symmetry:** 180° rotational symmetry ensures balance and harmony.

5. **Parametric flexibility:** The W, Ri, G parameterization allows easy experimentation with proportions while maintaining all geometric relationships.

## Comparison: Original vs. Experimental

| Property | Original PNG | Experimental |
|----------|-------------|--------------|
| W | 97 | 100 |
| Ri | 163 | 200 |
| Ro | 260 | 300 |
| G | ≈0.232 | ≈0.333 |
| Gap width | ≈22.5 | ≈33.3 |
| Diagonal slope | -0.4778 | -0.6672 |
| Ri/W ratio | 1.680 | 2.000 |
| Gap/W ratio | 0.232 | 0.333 |

**Visual differences:**
- Experimental version has **larger inner circle** relative to width (Ri/W = 2.0 vs 1.68)
- Experimental version has **wider gaps** (44% increase)
- Experimental version has **steeper diagonal lines** (slope -0.67 vs -0.48)
- Experimental version appears more "open" with more white space

## Mathematical Constraints

These constraints define the valid parameter space where the logo geometry remains well-defined.

### Basic Positivity

All parameters must be positive:

```
W > 0    (positive width)
Ri > 0   (positive inner radius)
G > 0    (positive gap proportion)
```

### Geometric Constraint (Binding)

The critical constraint comes from the orange/green shapes. Their boundaries at x = ±W(2G+1) must lie inside the inner circle of radius Ri:

```
W(2G+1) ≤ Ri
```

**Primary constraint: Ri > W(2G+1)**

This is the binding constraint that determines the valid parameter space.

### Derived Constraints

The binding constraint can be rearranged to express limits on any parameter:

**Minimum inner radius** (for given W and G):
```
Ri > W(2G+1)
Ri > W(1 + 2G)
```

**Maximum width** (for given Ri and G):
```
W < Ri/(2G+1)
W < Ri/(1 + 2G)
```

**Maximum gap proportion** (for given Ri and W):
```
G < (Ri - W)/(2W)
G < Ri/(2W) - 1/2
```

### Ratio Constraints

The constraint can also be expressed as a minimum ratio:

```
Ri/W > 2G+1
```

This means:
- For **G = 0** (no gaps): Ri/W > 1.0
- For **G = 0.1**: Ri/W > 1.2
- For **G = 0.2**: Ri/W > 1.4
- For **G = 0.3**: Ri/W > 1.6
- For **G = 0.5**: Ri/W > 2.0
- For **G = 1.0**: Ri/W > 3.0

**Practical minimum: Ri/W ≥ 1.0** (always required)

**Specific minimum: Ri/W > 1 + 2G** (depends on gap size)

### Boundary Cases

**Case 1: G → 0⁺** (minimum gap, shapes almost touching)
- Constraint becomes: Ri > W
- Gaps become infinitesimally small
- Shapes touch with zero white space
- Logo remains geometrically valid

**Case 2: G → (Ri-W)/(2W)** (maximum gap)
- Orange/green boundaries reach exactly to inner circle: W(2G+1) = Ri
- This is the limiting case
- Beyond this point, boundaries would exceed inner circle radius
- Geometry breaks

**Case 3: Ri → W⁺** (minimum inner radius)
- From Ri > W(2G+1) with Ri → W: W > W(2G+1)
- This gives: 1 > 2G+1, or G < 0
- Contradicts G > 0
- Therefore: **cannot have Ri arbitrarily close to W**
- Minimum Ri depends on chosen G: **Ri_min = W(1 + 2G)**

**Case 4: Ri → ∞** (very large inner radius)
- No upper bound on Ri
- Logo becomes a thin ring with large inner circle
- Geometrically valid, aesthetically questionable

### Validation Examples

**Original PNG: W=97, Ri=163, G≈0.232**

Check binding constraint:
```
Ri > W(2G+1)
163 > 97(2×0.232+1)
163 > 97(1.464)
163 > 142.0  ✓
```

Check ratio:
```
Ri/W = 163/97 ≈ 1.680
Required: > 2G+1 = 1.464  ✓
```

Check maximum G:
```
G_max = (Ri-W)/(2W) = (163-97)/(2×97) = 66/194 ≈ 0.340
G = 0.232 < 0.340  ✓
```

**Experimental: W=100, Ri=200, G=1/3**

Check binding constraint:
```
Ri > W(2G+1)
200 > 100(2×(1/3)+1)
200 > 100(5/3)
200 > 166.67  ✓
```

Check ratio:
```
Ri/W = 200/100 = 2.0
Required: > 2G+1 = 5/3 ≈ 1.667  ✓
```

Check maximum G:
```
G_max = (Ri-W)/(2W) = (200-100)/(2×100) = 100/200 = 0.5
G = 0.333 < 0.5  ✓
```

### Parameter Space Visualization

For a given choice of two parameters, the third is constrained:

**If you choose W and G:**
- Must have: **Ri > W(1 + 2G)**
- Example: W=100, G=0.3 → Ri must be > 160

**If you choose Ri and G:**
- Must have: **W < Ri/(1 + 2G)**
- Example: Ri=200, G=0.3 → W must be < 125

**If you choose Ri and W:**
- Must have: **G < (Ri-W)/(2W)**
- Example: Ri=200, W=100 → G must be < 0.5

### Breaking Points

The geometry **breaks** when:

1. **G ≥ (Ri-W)/(2W)** — gaps too large, orange/green boundaries exceed inner circle
2. **Ri ≤ W(1+2G)** — inner radius too small, points on inner circle become imaginary
3. **G ≤ 0** — negative or zero gaps, shapes overlap or collapse
4. **W ≤ 0** or **Ri ≤ 0** — negative dimensions, nonsensical

### Safe Parameter Ranges

For aesthetically pleasing and geometrically robust logos:

**Conservative recommendations:**
- **Ri/W**: between 1.5 and 3.0 (inner circle 1.5× to 3× the width)
- **G**: between 0.15 and 0.4 (gaps 15% to 40% of width)
- **Gap width (GW)**: between 0.15W and 0.4W

**Extreme but valid ranges:**
- **Ri/W**: from (1+2G) to ∞ (minimum depends on G, no maximum)
- **G**: from 0⁺ to (Ri-W)/(2W) (minimum near zero, maximum depends on Ri/W)

**Original and experimental both fall within conservative ranges.**
