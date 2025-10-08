import cv2
import numpy as np

def adjust_brightness_contrast(imageObject: np.ndarray) -> np.ndarray:
    """
    This function adjusts the brightness and contrast of a given image.
    """
    # Adjust brightness and contrast
    alpha = 1.25  # Contrast control (1.0 means no change)
    beta = 32.5    # Brightness control (0-100, with 0 being black)
    adjusted_image = cv2.convertScaleAbs(imageObject, alpha=alpha, beta=beta)
    return adjusted_image