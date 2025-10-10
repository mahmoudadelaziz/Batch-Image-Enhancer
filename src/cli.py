# The command line handler (currently the entry point of the application)
import argparse
from adjust_brightness import adjust_brightness_contrast
from input_loader import load_images_from_directory
from output_saver import save_output_images
from sharpen import sharpen_image

# Instantiating the command line argument parser
parser = argparse.ArgumentParser(description="Batch image enhancer.")

# Defining the main arguments (source dir, destination dir)
parser.add_argument("SourceDirectory",
                    type=str, 
                    help="The source directory containing the input images.")
parser.add_argument("OutputDirectory", 
                    type=str,
                    help="The output directory to save the enhanced images into.")

# Parsing the arguments
args = parser.parse_args()

# Defining the dictionary of the input images
myImgs_dict = load_images_from_directory(args.SourceDirectory)

# Processing... Enhancing...
for filename, image_info in myImgs_dict.items():
    myImgs_dict[filename] = sharpen_image(image_info)

# Saving the enhanced images
save_output_images(myImgs_dict, args.OutputDirectory)