import numpy as np
import cv2
from collections import Counter

def rgb_to_name(rgb_tuple):
    # Convert RGB to HEX
    hex_color = "#{:02x}{:02x}{:02x}".format(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
    
    # Define some common color names
    color_names = {
        "#000000": "Black", "#FFFFFF": "White", "#FF0000": "Red", "#00FF00": "Green", "#0000FF": "Blue",
        "#FFFF00": "Yellow", "#FFA500": "Orange", "#800080": "Purple", "#00FFFF": "Cyan", "#A52A2A": "Brown",
        "#808080": "Gray", "#FFC0CB": "Pink"
    }
    
    # Return the color name if found, otherwise return the HEX value
    return color_names.get(hex_color, hex_color)

def detect_colors(image, num_colors=5):
    # Convert image to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to be a list of pixels
    pixels = image.reshape((-1, 3))

    # Count the unique colors and their frequencies
    pixel_counts = Counter(map(tuple, pixels))

    # Get the most common colors
    common_colors = pixel_counts.most_common(num_colors)

    # Convert to a list of (RGB, Name) tuples
    result = [(color, rgb_to_name(color)) for color, count in common_colors]

    return result
