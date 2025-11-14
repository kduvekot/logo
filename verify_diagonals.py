#!/usr/bin/env python3
"""Verify diagonal lines against the PNG image"""

from PIL import Image
import math

# Load the PNG
img = Image.open('base-logo.png')
pixels = img.load()
width, height = img.size

# Center from analysis: (511.5, 454)
center_x, center_y = 511.5, 454

# Diagonal line equations (in centered coordinates)
top_slope = -0.476082
top_intercept = -53.198557

bottom_slope = -0.486262
bottom_intercept = 52.648349

def is_blue(pixel):
    """Check if pixel is blue (blue-gray color)"""
    r, g, b = pixel[:3]
    return b > 100 and r < 150

def centered_to_image(x_centered, y_centered):
    """Convert centered coordinates to image coordinates"""
    # In centered coords: y increases upward
    # In image coords: y increases downward
    x_img = x_centered + center_x
    y_img = center_y - y_centered
    return int(round(x_img)), int(round(y_img))

def image_to_centered(x_img, y_img):
    """Convert image coordinates to centered coordinates"""
    x_centered = x_img - center_x
    y_centered = center_y - y_img
    return x_centered, y_centered

print("=" * 60)
print("VERIFYING DIAGONAL LINES AGAINST PNG")
print("=" * 60)
print()

# Sample points along the top diagonal line in the blue region
print("TOP DIAGONAL LINE VERIFICATION:")
print("(Checking if pixels along the line are blue)")
print()

x_samples = range(-20, 25, 5)
for x in x_samples:
    y_centered = top_slope * x + top_intercept
    x_img, y_img = centered_to_image(x, y_centered)

    if 0 <= x_img < width and 0 <= y_img < height:
        pixel = pixels[x_img, y_img]
        is_blue_pixel = is_blue(pixel)
        status = "✓ BLUE" if is_blue_pixel else f"✗ RGB{pixel[:3]}"
        print(f"  x={x:4.0f}, y={y_centered:6.2f} → img({x_img:4d}, {y_img:4d}): {status}")

print()
print("BOTTOM DIAGONAL LINE VERIFICATION:")
print("(Checking if pixels along the line are blue)")
print()

for x in x_samples:
    y_centered = bottom_slope * x + bottom_intercept
    x_img, y_img = centered_to_image(x, y_centered)

    if 0 <= x_img < width and 0 <= y_img < height:
        pixel = pixels[x_img, y_img]
        is_blue_pixel = is_blue(pixel)
        status = "✓ BLUE" if is_blue_pixel else f"✗ RGB{pixel[:3]}"
        print(f"  x={x:4.0f}, y={y_centered:6.2f} → img({x_img:4d}, {y_img:4d}): {status}")

print()
print("=" * 60)
print("CHECKING DIAGONAL EDGES IN PNG")
print("=" * 60)
print()

# Scan along the diagonals to find the blue edges
print("Scanning for blue edges along diagonal paths...")
print()

# For the top diagonal, scan from left to right
print("TOP DIAGONAL - Finding blue region boundaries:")
for x in range(-100, 100, 10):
    y_centered = top_slope * x + top_intercept
    x_img, y_img = centered_to_image(x, y_centered)

    if 0 <= x_img < width and 0 <= y_img < height:
        # Check pixels above and below the diagonal
        pixel_center = pixels[x_img, y_img]
        pixel_above = pixels[x_img, max(0, y_img-2)] if y_img > 0 else pixel_center
        pixel_below = pixels[x_img, min(height-1, y_img+2)] if y_img < height-1 else pixel_center

        blue_center = is_blue(pixel_center)
        blue_above = is_blue(pixel_above)
        blue_below = is_blue(pixel_below)

        if blue_center and not blue_above:
            print(f"  Top edge near x={x:4.0f}, y={y_centered:6.2f} img({x_img}, {y_img})")
        if blue_center and not blue_below:
            print(f"  Bottom edge near x={x:4.0f}, y={y_centered:6.2f} img({x_img}, {y_img})")

print()
print("BOTTOM DIAGONAL - Finding blue region boundaries:")
for x in range(-100, 100, 10):
    y_centered = bottom_slope * x + bottom_intercept
    x_img, y_img = centered_to_image(x, y_centered)

    if 0 <= x_img < width and 0 <= y_img < height:
        # Check pixels above and below the diagonal
        pixel_center = pixels[x_img, y_img]
        pixel_above = pixels[x_img, max(0, y_img-2)] if y_img > 0 else pixel_center
        pixel_below = pixels[x_img, min(height-1, y_img+2)] if y_img < height-1 else pixel_center

        blue_center = is_blue(pixel_center)
        blue_above = is_blue(pixel_above)
        blue_below = is_blue(pixel_below)

        if blue_center and not blue_above:
            print(f"  Top edge near x={x:4.0f}, y={y_centered:6.2f} img({x_img}, {y_img})")
        if blue_center and not blue_below:
            print(f"  Bottom edge near x={x:4.0f}, y={y_centered:6.2f} img({x_img}, {y_img})")

print()
