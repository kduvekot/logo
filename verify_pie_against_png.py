#!/usr/bin/env python3
"""Verify pie shape against PNG"""

from PIL import Image
import math

# Load PNG
img = Image.open('base-logo.png')
pixels = img.load()

# Center from analysis
center_x, center_y = 511.5, 454

# Pie shape in centered coordinates
pie_center = (-18.5, 61.59)
pie_start = (-116.5, 61.59)
pie_end = (-60.33, -24.48)
pie_radius = 98

def centered_to_image(x_c, y_c):
    """Convert centered coords to image coords"""
    x_img = x_c + center_x
    y_img = center_y - y_c
    return int(round(x_img)), int(round(y_img))

def is_blue(pixel):
    """Check if pixel is blue"""
    r, g, b = pixel[:3]
    return b > 100 and r < 150

def point_in_pie(x_c, y_c, center, start, end, radius):
    """Check if point is inside pie slice"""
    # Vector from center to point
    dx = x_c - center[0]
    dy = y_c - center[1]
    dist = math.sqrt(dx**2 + dy**2)

    # Must be within radius
    if dist > radius:
        return False

    # Calculate angles
    angle_point = math.atan2(dy, dx)
    angle_start = math.atan2(start[1] - center[1], start[0] - center[0])
    angle_end = math.atan2(end[1] - center[1], end[0] - center[0])

    # Normalize to [0, 2π]
    def normalize(a):
        while a < 0:
            a += 2 * math.pi
        while a >= 2 * math.pi:
            a -= 2 * math.pi
        return a

    angle_point = normalize(angle_point)
    angle_start = normalize(angle_start)
    angle_end = normalize(angle_end)

    # Check if point is in the arc (counter-clockwise from start to end)
    if angle_end > angle_start:
        return angle_start <= angle_point <= angle_end
    else:
        # Arc wraps around 0
        return angle_point >= angle_start or angle_point <= angle_end

print("=" * 70)
print("VERIFYING PIE SHAPE AGAINST PNG")
print("=" * 70)
print()

print(f"Pie center: {pie_center}")
print(f"Pie start: {pie_start}")
print(f"Pie end: {pie_end}")
print(f"Pie radius: {pie_radius}")
print()

# Sample points along the pie edge
print("Checking pie edge points against PNG:")
print()

# Sample along the arc
num_samples = 20
start_angle = math.atan2(pie_start[1] - pie_center[1], pie_start[0] - pie_center[0])
end_angle = math.atan2(pie_end[1] - pie_center[1], pie_end[0] - pie_center[0])

# Counter-clockwise from start to end
angle_diff = end_angle - start_angle
if angle_diff < 0:
    angle_diff += 2 * math.pi

blue_count = 0
total_count = 0

for i in range(num_samples + 1):
    t = i / num_samples
    angle = start_angle + t * angle_diff

    x_c = pie_center[0] + pie_radius * math.cos(angle)
    y_c = pie_center[1] + pie_radius * math.sin(angle)

    x_img, y_img = centered_to_image(x_c, y_c)

    if 0 <= x_img < img.width and 0 <= y_img < img.height:
        pixel = pixels[x_img, y_img]
        is_blue_pixel = is_blue(pixel)
        total_count += 1
        if is_blue_pixel:
            blue_count += 1

        if i % 5 == 0:  # Print every 5th sample
            status = "✓ BLUE" if is_blue_pixel else f"✗ RGB{pixel[:3]}"
            print(f"  t={t:.2f}, centered ({x_c:6.1f}, {y_c:6.1f}) → img ({x_img:4d}, {y_img:4d}): {status}")

print()
print(f"Blue pixel match: {blue_count}/{total_count} ({100*blue_count/total_count:.1f}%)")
print()

# Check along the straight edges
print("Checking straight edge (center to start):")
edge_blue = 0
edge_total = 0
for i in range(11):
    t = i / 10
    x_c = pie_center[0] + t * (pie_start[0] - pie_center[0])
    y_c = pie_center[1] + t * (pie_start[1] - pie_center[1])

    x_img, y_img = centered_to_image(x_c, y_c)

    if 0 <= x_img < img.width and 0 <= y_img < img.height:
        pixel = pixels[x_img, y_img]
        is_blue_pixel = is_blue(pixel)
        edge_total += 1
        if is_blue_pixel:
            edge_blue += 1

print(f"  Blue pixels: {edge_blue}/{edge_total}")
print()

print("Checking closing edge (end to center):")
close_blue = 0
close_total = 0
for i in range(11):
    t = i / 10
    x_c = pie_end[0] + t * (pie_center[0] - pie_end[0])
    y_c = pie_end[1] + t * (pie_center[1] - pie_end[1])

    x_img, y_img = centered_to_image(x_c, y_c)

    if 0 <= x_img < img.width and 0 <= y_img < img.height:
        pixel = pixels[x_img, y_img]
        is_blue_pixel = is_blue(pixel)
        close_total += 1
        if is_blue_pixel:
            close_blue += 1

print(f"  Blue pixels: {close_blue}/{close_total}")
print()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

if blue_count / total_count > 0.7:
    print("✓ Arc edge mostly matches blue pixels in PNG")
else:
    print("✗ Arc edge does not match blue pixels well")

print()
print("Visual check: Open the SVG to see the semi-transparent pie overlay")
print("with red outline to compare with the underlying design.")
