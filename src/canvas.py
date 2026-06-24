import numpy as np
import cv2

def create_canvas(shape):
    return np.zeros(shape, dtype=np.uint8)

def draw_line(canvas, pt1, pt2, color=(0, 255, 0), thickness=5):
    if pt1 is None or pt2 is None:
        return canvas

    cv2.line(canvas, pt1, pt2, color, thickness)
    return canvas