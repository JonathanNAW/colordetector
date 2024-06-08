import numpy as np
import cv2

def detect_color(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixels = image.reshape((-1, 3))

    unique, counts = np.unique(pixels, axis=0, return_counts=True)

    most_frequent_color = unique[np.argmax(counts)]

    return most_frequent_color