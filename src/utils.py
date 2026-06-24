import cv2

def overlay(frame, canvas, alpha=0.6):
    return cv2.addWeighted(frame, 1 - alpha, canvas, alpha, 0)