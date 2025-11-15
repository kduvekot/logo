#!/usr/bin/env python3
"""
Generate a 4x4 grid of logos with mathematically pleasing parameter relationships.
Includes golden ratio, simple fractions, Fibonacci, square roots, and special angles.
"""

import math

# Golden ratio
PHI = (1 + math.sqrt(5)) / 2

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
        s, c = calculate_diagonal_slope_and_intercept(W, Ri, G)

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

        p6_x, p6_y = -p1_x, -p1_y
        p7_x, p7_y = -p2_x, -p2_y
        p8_x, p8_y = -p3_x, -p3_y
        p9_x, p9_y = -p4_x, -p4_y
        p10_x, p10_y = -p5_x, -p5_y

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

    for color in ["orange", "green", "blue"]:
        path = generate_logo_path(W, Ri, G, color)
        colors = {"orange": "#E4572E", "green": "#A1C181", "blue": "#4F6D7A"}
        svg += f'    <path d="{path}" fill="{colors[color]}"/>\n'

    svg += '  </g>\n'
    return svg

def generate_grid():
    """Generate 4x4 grid with mathematically pleasing parameter combinations."""

    # Define 16 special parameter combinations
    # Format: (W, Ri, G, label, description)
    W = 100

    special_cases = [
        # Row 1: Golden ratio variations
        (W, 161, (PHI-1)/2 - 0.05, "φ ratio", "Ri/W=φ, G≈φ-1"),
        (W, 161, 0.20, "φ ratio", "Ri/W=φ, G=1/5"),
        (W, 186, (PHI-1)/PHI, "φ inv", "G=(φ-1)/φ"),
        (W, 150, 1/PHI - 0.4, "φ inv", "Ri/W=3/2, G≈1/φ-0.4"),

        # Row 2: Simple fractions
        (W, 150, 1/6, "3/2", "Ri/W=3/2, G=1/6"),
        (W, 166, 1/6, "5/3", "Ri/W=5/3, G=1/6"),
        (W, 160, 1/5, "8/5 Fib", "Ri/W=8/5, G=1/5"),
        (W, 200, 1/6, "2/1", "Ri/W=2/1, G=1/6"),

        # Row 3: Square roots
        (W, 141, 0.15, "√2", "Ri/W=√2, G=0.15"),
        (W, 141, 0.20, "√2", "Ri/W=√2, G=1/5"),
        (W, 173, 0.15, "√3", "Ri/W=√3, G=0.15"),
        (W, 173, 0.20, "√3", "Ri/W=√3, G=1/5"),

        # Row 4: Special angles and Pythagorean
        (W, 170, 0.15, "30°", "Diagonal ≈30°"),
        (W, 210, 0.10, "45°", "Diagonal ≈45°"),
        (W, 162, 1/6, "13/8 Fib", "Ri/W=13/8, G=1/6"),
        (W, 400, 0.15, "5:4", "Ro/Ri=5/4"),
    ]

    # Grid layout
    cell_size = 400
    total_size = 4 * cell_size

    svg = f'<svg width="{total_size}" height="{total_size}" viewBox="0 0 {total_size} {total_size}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += '  <!-- 4x4 Mathematically Pleasing Logo Grid -->\n'
    svg += '  <!-- Golden ratio, Fibonacci, simple fractions, square roots, special angles -->\n'
    svg += '  <!-- W = 100 (constant) -->\n\n'

    # Background
    svg += f'  <rect width="{total_size}" height="{total_size}" fill="#f5f5f5"/>\n\n'

    # Title
    svg += f'  <text x="{total_size/2}" y="30" text-anchor="middle" font-family="serif" font-size="20" font-weight="bold">'
    svg += 'Mathematically Pleasing Parameter Combinations</text>\n\n'

    # Generate all 16 logos
    for idx, (W, Ri, G, label, desc) in enumerate(special_cases):
        row = idx // 4
        col = idx % 4

        # Calculate position
        tx = col * cell_size + cell_size / 2
        ty = row * cell_size + cell_size / 2 + 30  # Offset for title

        # Calculate scale
        Ro = Ri + W
        logo_diameter = 2 * Ro
        available_space = cell_size - 140
        scale = available_space / logo_diameter

        # Generate logo
        svg += generate_single_logo(W, Ri, G, tx, ty, scale)

        # Labels in upper left
        label_x = col * cell_size + 10
        label_y = row * cell_size + 50

        svg += f'  <text x="{label_x}" y="{label_y}" font-family="monospace" font-size="11" font-weight="bold" fill="#c00">'
        svg += f'{label}</text>\n'
        svg += f'  <text x="{label_x}" y="{label_y + 14}" font-family="monospace" font-size="9" fill="#333">'
        svg += f'{desc}</text>\n'
        svg += f'  <text x="{label_x}" y="{label_y + 26}" font-family="monospace" font-size="9" fill="#666">'
        svg += f'W={W}</text>\n'
        svg += f'  <text x="{label_x}" y="{label_y + 38}" font-family="monospace" font-size="9" fill="#666">'
        svg += f'Ri={Ri}</text>\n'
        svg += f'  <text x="{label_x}" y="{label_y + 50}" font-family="monospace" font-size="9" fill="#666">'
        svg += f'G={G:.3f}</text>\n'

        # Show ratio
        ratio = Ri / W
        s, c = calculate_diagonal_slope_and_intercept(W, Ri, G)
        angle = abs(math.atan(s)) * 180 / math.pi
        svg += f'  <text x="{label_x}" y="{label_y + 62}" font-family="monospace" font-size="8" fill="#999">'
        svg += f'ratio={ratio:.3f}</text>\n'
        svg += f'  <text x="{label_x}" y="{label_y + 72}" font-family="monospace" font-size="8" fill="#999">'
        svg += f'∠{angle:.1f}°</text>\n'

    # Grid lines
    svg += '\n  <!-- Grid lines -->\n'
    for i in range(1, 4):
        pos = i * cell_size
        svg += f'  <line x1="{pos}" y1="40" x2="{pos}" y2="{total_size}" stroke="#ccc" stroke-width="1"/>\n'
    for i in range(4):
        pos = i * cell_size + 40
        svg += f'  <line x1="0" y1="{pos}" x2="{total_size}" y2="{pos}" stroke="#ccc" stroke-width="1"/>\n'

    svg += '</svg>'
    return svg

if __name__ == "__main__":
    svg_content = generate_grid()

    output_file = "logo-special-ratios-4x4.svg"
    with open(output_file, 'w') as f:
        f.write(svg_content)

    print(f"Generated {output_file}")
    print("\n4x4 Grid - Mathematically Pleasing Combinations")
    print("=" * 60)
    print("Row 1: Golden ratio (φ) variations")
    print("Row 2: Simple fractions (3/2, 5/3, 8/5, 2/1)")
    print("Row 3: Square roots (√2, √3)")
    print("Row 4: Special angles (30°, 45°) and Pythagorean")
    print("\nAll parameters chosen for mathematical beauty!")
