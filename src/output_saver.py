import os
import cv2
import numpy as np
from typing import Dict
from rich import print

def save_output_images(output_images: Dict[str, np.ndarray],
                       output_directory: str) -> None:
    """
    Saves the output images to a specified directory.

    This function saves the output images to a directory
    specified by the user.

    Args:
        images (List[np.ndarray]): The list of enhanced images.
        outputDirectory (str): The path to the output directory.

    Returns:
        List[np.ndarray]: A list of images loaded as OpenCV/NumPy arrays.
                          Returns an empty list if the directory is not found
                          or contains no valid images.
    """

    # Create the destination directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    print(f"Saving the images in '{output_directory}'...")
    for filename, image_data in output_images.items():
        full_path = os.path.join(output_directory, "enhanced_" + filename)
        cv2.imwrite(full_path, image_data)
