# Base Logo Analysis - PNG Observations

## Image Properties

- **Format**: PNG
- **Dimensions**: 1024 x 1024 pixels
- **Color depth**: 8-bit RGB

## Logo Bounding Box

When ignoring white pixels (RGB ≥ 250,250,250):

- **Left edge**: x = 252
- **Right edge**: x = 771
- **Top edge**: y = 194
- **Bottom edge**: y = 714
- **Width**: 520 pixels
- **Height**: 521 pixels
- **Center of bounding box**: (511.5, 454.0)

## Geometric Structure

### Circle Parameters

**Center point**: (511.5, 454.0)

**Outer circle**:
- Radius: 260 pixels
- Top point: (511.5, 194)
- Bottom point: (511.5, 714)
- Left point: (251.5, 454)
- Right point: (771.5, 454)

**Inner circle**:
- Radius: 163 pixels
- Top point: (511.5, 291)
- Bottom point: (511.5, 617)
- Left point: (348.5, 454)
- Right point: (674.5, 454)

**Ring width**: 97 pixels (260 - 163)

**Mid-radius**: 215 pixels (used for analysis)

## Color Identification

Three primary colors detected:

1. **Red-Orange** (#E4572E)
   - RGB range: r > 180, g < r-30, b < 100

2. **Soft Green** (#A1C181)
   - RGB range: g > 140, g > r, g > b

3. **Blue-Gray** (#4F6D7A)
   - RGB range: b > 100, r < 150

## Shape Segments (at mid-radius 215px)

Scanning the mid-radius circle reveals clean segment boundaries:

### Green Segment
- **Angular span**: 0° to 90° and 311° to 360° (wraps around)
- **Total coverage**: ~139°

### Orange Segment
- **Angular span**: 131° to 271°
- **Coverage**: 140°

### Blue Segments
- **Upper section**: 277° to 304° (27°)
- **Lower section**: 96° to 123° (27°)

### Gaps (White space)
1. Gap 1: 90° to 95° (5°)
2. Gap 2: 124° to 131° (7°)
3. Gap 3: 271° to 276° (5°)
4. Gap 4: 304° to 311° (7°)

## Vertical Edge Lines

The logo features **vertical straight edges** (constant x-coordinate) at the gaps, not radial lines.

### Key Vertical Boundaries

**Left side (Orange segment)**:
- Center vertical line: x = 511.5 (top of logo)
- Right edge of orange: x = 370 (gap boundary)

**Right side (Green segment)**:
- Center vertical line: x = 511.5 (bottom of logo)
- Left edge of green: x = 653 (gap boundary)

**Middle section (Blue stepped element)**:
- Multiple vertical edges at: x ≈ 395, 493, 534, 631

### Vertical Edge Intersections with Circles

**Orange segment at x = 370**:
- Outer circle intersection: y ≈ 672.1
- Inner circle intersection: y ≈ 534.9

**Green segment at x = 653**:
- Outer circle intersection: y ≈ 235.9
- Inner circle intersection: y ≈ 373.1

## Shape Descriptions

### Left Shape (Orange)
- Starts at top center of outer circle (511.5, 194)
- Has vertical edge at x = 511.5 going down to inner circle
- Follows inner circle arc counter-clockwise
- Has vertical edge at x = 370
- Follows outer circle arc clockwise back to start
- **Structure**: 2 vertical lines + 2 circular arcs

### Right Shape (Green)
- Starts at bottom center of outer circle (511.5, 714)
- Has vertical edge at x = 511.5 going up to inner circle
- Follows inner circle arc clockwise
- Has vertical edge at x = 653
- Follows outer circle arc counter-clockwise back to start
- **Structure**: 2 vertical lines + 2 circular arcs

### Middle Shape (Blue)
- **Structure**: 10 edges total (6 straight, 4 arcs)
- **Outer vertical edges**: x = ±119.5
- **Inner vertical edges**: x = ±22.5
- **Width**: 97 pixels (matching ring width)
- **Components**:
  - 2 outer circle arcs (radius 260) at top and bottom
  - 2 outer vertical edges extending from outer arcs
  - 2 "pie arcs" (radius 97) tangent to diagonal lines
  - 2 diagonal connectors bridging upper/lower sections
  - 2 inner vertical edges
- Creates dynamic stepped pattern connecting upper and lower sections
- Maintains same width (97px) as orange and green ring segments

## Horizontal Scan Results

Scanning along y = 454 (horizontal centerline):

| X-coordinate | Color Transition |
|-------------|-----------------|
| 252 | White → Orange |
| 349 | Orange → White (gap) |
| 418 | White → Blue |
| 606 | Blue → Green |
| 607 | Green → White (gap) |
| 677 | White → Green |
| 772 | Green → White |

## Symmetry Observations

The orange (left) and green (right) shapes are **approximately symmetric** around the vertical centerline (x = 511.5):

- Orange edges: centerline to x = 370 (distance: -141.5)
- Green edges: centerline to x = 653 (distance: +141.5)
- Both shapes span approximately 140° of arc
- Both have vertical edges at their boundaries
- Both follow the circular ring structure

## Gap Measurements (Centered Coordinate System)

In the centered system (origin at 511.5, 454):

**Four symmetric gaps** where blue shape interrupts orange/green rings:

**Top center gap** (between orange and blue):
- From x = 0 to x = 22.5
- Width: **22.5 pixels**

**Top outer gap** (between blue and green):
- From x = 119.5 to x = 141.5
- Width: **22.0 pixels**

**Bottom center gap** (between green and blue):
- From x = 0 to x = -22.5
- Width: **22.5 pixels**

**Bottom outer gap** (between blue and orange):
- From x = -119.5 to x = -141.5
- Width: **22.0 pixels**

All gaps are perfectly symmetric (180° rotational symmetry about origin).

## Blue Shape Vertical Edge Analysis (Centered Coordinates)

Precise vertical edge locations:

**Inner vertical edges** (center of blue shape):
- x = **±22.5**
- These edges connect the upper and lower sections vertically

**Outer vertical edges** (sides of blue shape):
- x = **±119.5**
- These edges extend from outer circle arcs down/up to the diagonal crossing points

**Geometric properties**:
- Width between inner edges: 45 pixels
- Width between outer edges: 239 pixels
- Standard width (outer to inner on same side): **97 pixels** (matches ring width)
- Outer edges reach from outer circle arcs to y = ±64.50 (diagonal crossings)
- Creates symmetric stepped pattern with 180° rotational symmetry

## Complete Geometric Formulas

All logo points can be precisely calculated from these fundamental parameters:

### Primary Input Parameters
1. **R_outer = 260 px** (outer circle radius)
2. **R_inner = 163 px** (inner circle radius)
3. **Width = 97 px** (standard width = R_outer - R_inner)
4. **Center = (0, 0)** (in transformed coordinates)
5. **Diagonal intercept = 53.75** (y-intercept of diagonal lines)
6. **Gap ratio = 0.232** (gap_width / width)

### Derived Blue Shape Parameters (see gap-derivation-findings.md)
- **Diagonal slope**: m = -√((2 × 53.75 / 97)² - 1) = -0.4777
- **x_blue_outer = ±119.5** - DERIVED from diagonal ∩ inner circle intersection
- **x_blue_inner = ±22.5** - DERIVED as x_blue_outer - width

### Derived Orange/Green Shape Parameters
- **gap_width = 22.5** - DERIVED as width × gap_ratio (or intercept / 2.39)
- **x_boundaries = ±141.5** - DERIVED as x_blue_outer + gap_width

### Diagonal Line Equations
- Top: y = -0.4778x - 53.75
- Bottom: y = -0.4778x + 53.75

### Documentation References
- See `diagonal-lines-analysis.md` for complete diagonal derivation formulas
- See `gap-derivation-findings.md` for gap position derivation analysis

## Additional Notes

- All gaps feature vertical boundaries (straight up-down lines)
- No angled/radial lines at gap edges
- The blue stepped element occupies the central area
- Anti-aliasing creates slight color gradients at edges
- The design maintains clean separation between colored segments
- Perfect 180° rotational symmetry about the origin
- All three shape segments maintain the same width (97 pixels)
