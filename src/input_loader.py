import os
import cv2
import numpy as np
from typing import Dict
from rich import print

def load_images_from_directory(directory: str) -> Dict[str, np.ndarray]:
    """
    Loads all valid image files from a specified directory.

    This function iterates through all files in the given directory,
    filters for common image extensions (.png, .jpg, .jpeg, .bmp),
    and returns a dictionary of successfully loaded images.

    Args:
        directory (str): The path to the directory containing images.

    Returns:
        Dict[str, np.ndarray]: A dictionary of images formatted as:
        {fileName: imageArray}
        or an empty dict if no valid images.
    """
    SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
    images = {}

    # Check if the provided path is actually a directory
    if not os.path.isdir(directory):
        print(f"Error: Directory not found at '{directory}'")
        return {}

    print(f"Scanning for images in '{directory}'...")
    for file in os.listdir(directory):
        # Get the file name (as is)
        # fileName = os.path.splitext(file)[0].lower()
        # Get the file extension and convert to lower case
        extension = os.path.splitext(file)[1].lower()

        if extension in SUPPORTED_EXTENSIONS:
            # Create the file path
            image_path = os.path.join(directory, file)
            # Load the image
            image = cv2.imread(image_path)
            # Check if the image was loaded successfully
            if image is not None:
                images[file] = image
            else:
                print(f"Warning: Could not read file,\
                       it might be corrupted: {image_path}")
    return images