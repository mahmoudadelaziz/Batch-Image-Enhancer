import cv2
import numpy as np

def sharpen_image(image: np.ndarray) -> np.ndarray:
    """
    Sharpens an input image using a 2D convolution kernel.

    This function applies a common 3x3 sharpening kernel to an image,
    enhancing the edges and details by subtracting a blurred version of the
    image from the original.

    Args:
        image (np.ndarray): The input image as a NumPy array. 
        Expected to be in a format readable by OpenCV (e.g., BGR).

    Returns:
        np.ndarray: The sharpened image as a NumPy array.
    """
    # Define a 3x3 sharpening kernel (a high-pass filter)
    kernel = np.array([[ 0, -1,  0],
                       [-1,  5, -1],
                       [ 0, -1,  0]], dtype=np.float32)
    
    # Apply the kernel to the image using 2D convolution.
    # The ddepth argument of -1 means the output image will have the same
    # depth (data type) as the input image.
    sharpened_image = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

    return sharpened_image