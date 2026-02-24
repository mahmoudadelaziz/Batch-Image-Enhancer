import cv2
import numpy as np

def reduce_noise(imageObject: np.ndarray) -> np.ndarray:
    """
    This function reduces the noise in the image 
    using the Gaussian filtering approach.
    
    Args:
        imageObject (np.ndarray): The image data of a single image,
        as an OpenCV image (that is, a np.ndarray)

    Returns:
        np.ndarray: the image data of the enhanced image
    """

    # Apply Gaussian blur for noise reduction
    adjusted_image = cv2.GaussianBlur(imageObject, (5, 5), 0)
    return adjusted_image