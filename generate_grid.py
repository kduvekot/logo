#!/usr/bin/env python3
"""
Generate a 3x3 grid of logo variations exploring the parameter space.
Rows vary Ri (inner radius), columns vary G (gap proportion), W is constant.
"""

import math

def calculate_diagonal_slope_and_intercept(W, Ri, G):
    """Calculate diagonal line slope and intercept."""
    H = math.sqrt(Ri**2 - W**2 * (G + 1)**2)

    # Quadratic coefficients: a*s^2 + b*s + c = 0
    a = W**2 * (0.25 - (G + 1)**2)
    b = -2 * W * (G + 1) * H
    c = W**2 / 4 - H**2

    # Solve quadratic
    discriminant = b**2 - 4*a*c
    s1 = (-b + math.sqrt(discriminant)) / (2*a)
    s2 = (-b - math.sqrt(discriminant)) / (2*a)

    # Choose the slope with smaller absolute value (gentler slope)
    s = s2 if abs(s2) < abs(s1) else s1

    # Calculate intercept
    intercept = W * math.sqrt(1 + s**2) / 2

    return s, intercept

def generate_logo_path(W, Ri, G, color):
    """Generate SVG path for one logo shape."""
    Ro = Ri + W
    GW = G * W

    if color == "orange":
        # Orange shape (left, top)
        x_boundary = -W * (2*G + 1)
        y1 = -Ro
        y2 = -Ri
        y3 = math.sqrt(Ri**2 - x_boundary**2)
        y4 = math.sqrt(Ro**2 - x_boundary**2)

        path = f"M 0,{y1} L 0,{y2} "
        path += f"A {Ri},{Ri} 0 0 0 {x_boundary},{y3} "
        path += f"L {x_boundary},{y4} "
        path += f"A {Ro},{Ro} 0 0 1 0,{y1} Z"

    elif color == "green":
        # Green shape (right, bottom) - 180° rotation of orange
        x_boundary = W * (2*G + 1)
        y1 = Ro
        y2 = Ri
        y3 = -math.sqrt(Ri**2 - x_boundary**2)
        y4 = -math.sqrt(Ro**2 - x_boundary**2)

        path = f"M 0,{y1} L 0,{y2} "
        path += f"A {Ri},{Ri} 0 0 0 {x_boundary},{y3} "
        path += f"L {x_boundary},{y4} "
        path += f"A {Ro},{Ro} 0 0 1 0,{y1} Z"

    elif color == "blue":
        # Blue shape (center, complex)
        s, c = calculate_diagonal_slope_and_intercept(W, Ri, G)

        # Calculate perpendicular unit vector
        u_perp_x = -s / math.sqrt(s**2 + 1)
        u_perp_y = 1 / math.sqrt(s**2 + 1)

        # Top section vertices
        p1_x = GW
        p1_y = -math.sqrt(Ro**2 - GW**2)

        p2_x = W * (G + 1)
        p2_y = -math.sqrt(Ro**2 - p2_x**2)

        p3_x = p2_x
        p3_y = s * GW - c

        p4_x = GW - W * s / math.sqrt(s**2 + 1)
        p4_y = s * GW - c + W / math.sqrt(s**2 + 1)

        p5_x = -GW
        p5_y = -s * GW + c

        # Bottom section vertices (180° rotation)
        p6_x = -p1_x
        p6_y = -p1_y

        p7_x = -p2_x
        p7_y = -p2_y

        p8_x = -p3_x
        p8_y = -p3_y

        p9_x = -p4_x
        p9_y = -p4_y

        p10_x = -p5_x
        p10_y = -p5_y

        # Build path
        path = f"M {p1_x},{p1_y} "
        path += f"A {Ro},{Ro} 0 0 1 {p2_x},{p2_y} "
        path += f"L {p3_x},{p3_y} "
        path += f"A {W},{W} 0 0 1 {p4_x},{p4_y} "
        path += f"L {p5_x},{p5_y} "
        path += f"L {p6_x},{p6_y} "
        path += f"A {Ro},{Ro} 0 0 1 {p7_x},{p7_y} "
        path += f"L {p8_x},{p8_y} "
        path += f"A {W},{W} 0 0 1 {p9_x},{p9_y} "
        path += f"L {p10_x},{p10_y} Z"

    return path

def generate_single_logo(W, Ri, G, tx, ty, scale):
    """Generate SVG group for a single logo at position (tx, ty) with scaling."""
    svg = f'  <g transform="translate({tx},{ty}) scale({scale})">\n'

    # Orange shape
    path = generate_logo_path(W, Ri, G, "orange")
    svg += f'    <path d="{path}" fill="#E4572E"/>\n'

    # Green shape
    path = generate_logo_path(W, Ri, G, "green")
    svg += f'    <path d="{path}" fill="#A1C181"/>\n'

    # Blue shape
    path = generate_logo_path(W, Ri, G, "blue")
    svg += f'    <path d="{path}" fill="#4F6D7A"/>\n'

    svg += '  </g>\n'
    return svg

def generate_grid():
    """Generate complete 4x4 grid SVG with two parameters varying."""
    # Parameter grid design for condensed logos:
    # W = 100 (CONSTANT - for direct comparison)
    # Rows: Ri varies (155, 170, 190, 210) - Ri/W = 1.55, 1.70, 1.90, 2.10
    # Columns: G varies (0.10, 0.15, 0.20, 0.25)
    #
    # This allows clear visual comparison:
    # - Moving DOWN a column: see effect of increasing Ri (G constant)
    # - Moving RIGHT across a row: see effect of increasing G (Ri constant)

    W = 100  # Constant for all logos
    Ri_values = [155, 170, 190, 210]  # Corresponds to Ri/W = 1.55, 1.70, 1.90, 2.10
    G_values = [0.10, 0.15, 0.20, 0.25]

    # Grid layout
    cell_size = 400
    total_size = 4 * cell_size

    svg = f'<svg width="{total_size}" height="{total_size}" viewBox="0 0 {total_size} {total_size}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += '  <!-- 4x4 Logo Parameter Exploration Grid -->\n'
    svg += '  <!-- Two parameters vary, one constant for direct comparison -->\n'
    svg += '  <!-- W = 100 (CONSTANT) -->\n'
    svg += '  <!-- Rows: Ri = 155, 170, 190, 210 (Ri/W ratio increases down) -->\n'
    svg += '  <!-- Columns: G = 0.10, 0.15, 0.20, 0.25 (gap proportion increases right) -->\n'
    svg += '  <!-- Slopes range from ~20° to ~38° (very gentle) -->\n\n'

    # Background
    svg += f'  <rect width="{total_size}" height="{total_size}" fill="#f5f5f5"/>\n\n'

    # Column headers
    svg += '  <!-- Column headers (G values) -->\n'
    for col, G in enumerate(G_values):
        x = col * cell_size + cell_size / 2
        svg += f'  <text x="{x}" y="30" text-anchor="middle" font-family="monospace" font-size="16" font-weight="bold">G = {G:.2f}</text>\n'

    # Row headers and logos
    for row, Ri in enumerate(Ri_values):
        # Row header
        y = row * cell_size + cell_size / 2
        svg += f'\n  <!-- Row {row+1}: Ri = {Ri} -->\n'
        svg += f'  <text x="15" y="{y}" text-anchor="start" font-family="monospace" font-size="16" font-weight="bold" transform="rotate(-90 15 {y})">Ri = {Ri}</text>\n'

        for col, G in enumerate(G_values):

            # Calculate position
            tx = col * cell_size + cell_size / 2
            ty = row * cell_size + cell_size / 2

            # Calculate scale to fit logo in cell
            Ro = Ri + W
            logo_diameter = 2 * Ro
            available_space = cell_size - 120  # Leave margin for labels
            scale = available_space / logo_diameter

            # Generate logo
            svg += generate_single_logo(W, Ri, G, tx, ty, scale)

            # Add parameter label in upper left corner of cell, outside outer circle
            label_x = col * cell_size + 10
            label_y = row * cell_size + 20
            svg += f'  <text x="{label_x}" y="{label_y}" text-anchor="start" font-family="monospace" font-size="10" fill="#333">'
            svg += f'W={W}</text>\n'
            svg += f'  <text x="{label_x}" y="{label_y + 12}" text-anchor="start" font-family="monospace" font-size="10" fill="#333">'
            svg += f'Ri={Ri}</text>\n'
            svg += f'  <text x="{label_x}" y="{label_y + 24}" text-anchor="start" font-family="monospace" font-size="10" fill="#333">'
            svg += f'G={G:.2f}</text>\n'

            # Calculate and display diagonal slope
            s, c = calculate_diagonal_slope_and_intercept(W, Ri, G)
            angle_deg = abs(math.atan(s)) * 180 / math.pi
            svg += f'  <text x="{label_x}" y="{label_y + 36}" text-anchor="start" font-family="monospace" font-size="9" fill="#999">'
            svg += f'slope={s:.3f}</text>\n'
            svg += f'  <text x="{label_x}" y="{label_y + 46}" text-anchor="start" font-family="monospace" font-size="9" fill="#999">'
            svg += f'angle={angle_deg:.1f}°</text>\n'

    # Grid lines
    svg += '\n  <!-- Grid lines -->\n'
    for i in range(1, 4):
        pos = i * cell_size
        svg += f'  <line x1="{pos}" y1="0" x2="{pos}" y2="{total_size}" stroke="#ccc" stroke-width="1"/>\n'
        svg += f'  <line x1="0" y1="{pos}" x2="{total_size}" y2="{pos}" stroke="#ccc" stroke-width="1"/>\n'

    svg += '</svg>'
    return svg

if __name__ == "__main__":
    svg_content = generate_grid()

    output_file = "logo-parameter-grid-4x4.svg"
    with open(output_file, 'w') as f:
        f.write(svg_content)

    print(f"Generated {output_file}")
    print("\n4x4 Grid - Condensed Logo Parameter Exploration")
    print("=" * 60)
    print("Two parameters vary, one constant for comparison:")
    print("  W (constant):     100")
    print("  Rows (Ri):        155, 170, 190, 210")
    print("  Columns (G):      0.10, 0.15, 0.20, 0.25")
    print("  Ri/W ratios:      1.55, 1.70, 1.90, 2.10")
    print("\nVisual comparison:")
    print("  - Down a column: effect of changing Ri (G constant)")
    print("  - Across a row: effect of changing G (Ri constant)")
    print("\nDiagonal slopes range from ~20° to ~38° (very gentle)")
    print("Text labels positioned in upper left corner of each cell")
